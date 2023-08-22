# NoaEngine

NoaEngine is a visual novel / galgame engine utilizing LLM (e.g. GPT) to interactively write the story with the player. This project aims to create personal, creative and highly interactive stories that under full control of the player, while achieving the same level of immersion as traditional visual novels.

## Installation
- Install Python, and dependencies listed in `requirements.txt`
- Fill in the `config.yaml` file with your own settings
  - Replace the model_key with openai api key of your own. [Click here](https://platform.openai.com/account/api-keys) to manage your api keys.
- Run `export FLASK_APP=engine.py; flask run` to start the server, and visit `localhost:5000` to play the game.
  - Add your flask parameters to enable LAN access, DIY!
  - 

## Progress
- [ ] UI
  - [ ] Load Conversation
  - [ ] Save Conversation
  - [x] Basic UI
- [ ] LLM Interaction
  - [ ] Integrate with EssenceDB and Story Engine
  - [x] LLM Prompts
  - [x] Helpers
- [ ] Story Engine

## License
CC-BY-NC-SA 4.0
