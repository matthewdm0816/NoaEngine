from collections import defaultdict
import logging
import json
import itertools
from omegaconf import OmegaConf
logger = logging.getLogger(__name__)

DEFAULT_PROPERTY_TYPE = 'default'

Prompts = OmegaConf.load('prompts.yaml')


class InstanceCounterMeta(type):
    """ Metaclass to make instance counter not share count with descendants
    """
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._ids = itertools.count(1)

class Essence(metaclass=InstanceCounterMeta):
    def __init__(self, name, description, essence_name):
        self.id = next(self.__class__._ids)
        self.name = name if name is not None else f"{essence_name}-{self.id}"
        self.description = description
        self.property = defaultdict(list)
        self._init_essence(essence_name)

    def _init_essence(self, essence_name=None):
        # if essence_name is None:
        #     essence_name = self.__class__.__name__
        self.essence_name = essence_name
        setattr(self, f"add_{essence_name}", self.add_property)
        setattr(self, f"get_{essence_name}", self.get_property)

    def _check_type(self, type):
        if type is None:
            if len(self.property) == 1:
                return list(self.property.keys())[0]
            else:
                logger.warning(f"Not specify type for {self.name}, use default type {DEFAULT_PROPERTY_TYPE}")
                return DEFAULT_PROPERTY_TYPE
        else:
            return type
        

    def add_property(self, type=None, prop=None):
        type = self._check_type(type)
        # return a function if prop is None
        if prop is None:
            return lambda prop: self.property[type].append(prop)
        if isinstance(prop, list):
            self.property[type].extend(prop)
        else:
            self.property[type].append(prop)

    def get_property(self, type=None):
        result = self.property[type]
        if len(result) == 1:
            return result[0]
        else:
            return result
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def from_json(self, json_str):
        json_dict = json.loads(json_str)
        self.__dict__.update(json_dict)
        return self
    
    def get_essence_typeid(self):
        return f"[{self.essence_name}-{self.id}:{self.name}]"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'property': self.property,
            'essence_name': self.essence_name,
            'essence_typeid': self.get_essence_typeid(),
            **{
                type: self.get_property(type) for type in self.property
            }
        }
    
    def to_prompt(self):
        # NOTE: SUBCLASS SHOULD OVERRIDE THIS METHOD
        return getattr(Prompts, self.__class__.__name__.lower()).format(self.to_dict())
    
    
    
# StoryLine contains Dialog List
class StoryLine(Essence):
    def __init__(self, name, description):
        super().__init__(name, description, 'storyline')


# DialogTemplate = 

class Dialog(Essence):
    def __init__(self, description, place, characters, content, summary, next_place=None):
        super().__init__(None, description, 'dialog')
        self.add_property('place', place)
        self.add_property('characters', characters)
        self.add_property('content', content)
        self.add_property('summary', summary)
        self.add_property('next_place', next_place)

    def get_essence_typeid(self):
        return f"[{self.essence_name}-{self.id}]"


class Character(Essence):
    def __init__(self, name, description, appearance, personality, background, relationship, dialog, summary):
        super().__init__(name, description, 'character')
        self.add_property('appearance', appearance)
        self.add_property('personality', personality)
        self.add_property('background', background)
        self.add_property('relationship', relationship)
        self.add_property('dialog', dialog)
        self.add_property('summary', summary)

class Place(Essence):
    def __init__(self, name, description, dialog, summary):
        super().__init__(name, description, 'place')
        self.add_property('dialog', dialog)
        self.add_property('summary', summary)

class Flag(Essence):
    def __init__(self, name, description):
        super().__init__(name, description, 'flag')

class EssenceDB:
    def __init__(self):
        self.storyline = []
        self.character = []
        self.place = []
        self.flag = []
        self.dialog = []

    def query(self, essence_type, essence_name):
        return getattr(self, essence_type).get(essence_name)

    def add_dialog(self, dialog):
        # TODO
        # parse dialog

        # add dialog to place

        # add dialog to character

        # add dialog to storyline

        # add dialog to dialog

        pass