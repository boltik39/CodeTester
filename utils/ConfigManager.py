from metaclasses.Singleton import SingletonMetaClass
from pathlib import Path
import json


class ConfigManager(metaclass=SingletonMetaClass):
    __GOOGLE_CONFIG_PATH = \
        Path(Path().cwd(), 'configs', 'google_sheets_config.json')
    __ERROR_MSG_CONFIG_PATH = Path(Path().cwd(), 'configs', 'error_msg_config.json')

    def __init__(self):
        self.__google_config_dict = self.__get_info_from_config(
            self.__GOOGLE_CONFIG_PATH)
        self.__error_msg_config_dict = self.__get_info_from_config(
            self.__ERROR_MSG_CONFIG_PATH)

    @staticmethod
    def __get_info_from_config(config_path):
        with open(config_path, 'r') as config_file:
            return json.load(config_file)

    def get_from_google_config(self, param):
        return self.__google_config_dict[param]

    def get_from_error_msg_config(self, param):
        return self.__error_msg_config_dict[param]



