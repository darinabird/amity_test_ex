import json


class Configs:
    def __init__(self):
        with open("common/test_config.json") as cfg:
            config = json.load(cfg)

        self.url_base_host = config["base_url"]
        self.user_admin = config["user_admin"]
