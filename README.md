# Getting started

1. Install poetry if it is not installed yet in your system
2. Run `poetry shell`
3. Run `poetry install` -> this will install all the packages in the .toml file
4. Change the name of the .env_example to .env and update the values in it
5. Run the server with `uvicorn app.main:app --reload`

Linting checks follow the black formatting style. You can add `"python.formatting.provider": "black"` in your settings.json in Visual Code Studio in order to automatically format according to black every time you save a file. 


