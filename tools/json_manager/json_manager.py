import json


class JsonManager:

    def __init__(self):
        pass

    @staticmethod
    def load_config(config_file: str) -> dict:
        with open(config_file, "r") as _j:
            config = json.load(_j)
        return config

    @staticmethod
    def save_config(config: dict, config_file: str):
        with open(config_file, "w") as _o:
            json.dump(config, _o, indent=2, sort_keys=True)

    @staticmethod
    def get_enumerated_keys(config: dict) -> dict[int, str]:
        return {
            i+1: key for i, key in enumerate(sorted(config.keys()))
        }
