import openai
from config import Config, Prompts
import json
import logging
import pretty_errors

logger = logging.getLogger(__name__)


LLM_CONFIG = getattr(Config, Config.llm_type)

if Config.llm_type == 'openai':
    openai.api_key = LLM_CONFIG.api_key


def request_output(system_input, user_input, model_name=None, **kwargs):
    if model_name is None:
        model_name = LLM_CONFIG.model_name

    response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
            {
            "role": "system",
            "content": system_input
            },
            {
            "role": "user",
            "content": user_input
            }
        ],
        temperature=kwargs.get('temperature', LLM_CONFIG.temperature),
        max_tokens=kwargs.get('max_tokens', LLM_CONFIG.max_tokens),
        top_p=kwargs.get('top_p', LLM_CONFIG.top_p),
        frequency_penalty=kwargs.get('frequency_penalty', LLM_CONFIG.frequency_penalty),
        presence_penalty=kwargs.get('presence_penalty', LLM_CONFIG.presence_penalty),
    )

    # return response.choices[0].text
    return response.choices[0].message["content"]

def parse_conversation(conversation):
    # TODO
    # parse conversation
    # return parsed_conversation
    return conversation


if __name__ == "__main__":
    # test code
    print(request_output("你好", "你好"))



