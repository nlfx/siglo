import configparser
import xdg.BaseDirectory
from pathlib import Path


class config:
    # Class constants
    default_config = {"mode": "singleton", "deploy_type": "quick"}
    config_dir = xdg.BaseDirectory.xdg_config_home
    config_file = config_dir + "/siglo.ini"

    def load_defaults(self):
        if not Path(self.config_dir).is_dir():
            Path.mkdir(Path(self.config_dir))
        # if config file is not valid, load defaults
        if not self.file_valid():
            config = configparser.ConfigParser()
            config["settings"] = self.default_config
            with open(self.config_file, "w") as f:
                config.write(f)

    def file_valid(self):
        if not Path(self.config_file).is_file():
            return False
        else:
            config = configparser.ConfigParser()
            config.read(self.config_file)
            for key in list(self.default_config.keys()):
                if not key in config["settings"]:
                    return False
            return True

    def get_property(self, key):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config["settings"][key]

    def set_property(self, key, val):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        config["settings"][key] = val
        with open(self.config_file, "w") as f:
            config.write(f)
        

