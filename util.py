import json
import logging


def get_settings():
    try:
        with open("settings.json") as settings_file:
            return json.load(settings_file)
    except:
        logging.error("Error while loading the settings file")
