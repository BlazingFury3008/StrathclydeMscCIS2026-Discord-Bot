# StrathclydeMscCIS2026-Discord-Bot
This is a collaboration project between MsC CIS Students from Strathclyde 2026

- [Aiden Taylor](https://github.com/BlazingFury3008)
- [Andrew Kennedy](https://github.com/kennedyandrew18-blip)

### Features
`run.sh` - This will run the program on a Unix based OS, creating the structure required for the .env file. The first run will create the .env file, then it will need to be run again to run the program. Although you can run the application with `python app/main.py`, the code will not run properly

`/cogs` - This is the folder which will contain all the potential cogs for the application. When implementing Cogs, the *main_logger* in `/helper/logging.py` should be used, especially when complex events happen, incase of spam, or errors