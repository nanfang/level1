import sys
import os
import yaml

DEFAULT_SETTING_YML = 'level1.yml'


def _get_default_settings():
    #
    # search PYTHONPATH
    for path in sys.path:
        file_path = os.path.join(path, DEFAULT_SETTING_YML)
        if os.path.exists(file_path):
            return yaml.load(open(file_path))

    return {}


def get_settings():
    # TODO support overridden settings from commandline
    return _get_default_settings()


settings = get_settings()
