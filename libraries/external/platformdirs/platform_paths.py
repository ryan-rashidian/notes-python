"""This module contains filesystem path(s) used by this application."""

from pathlib import Path

from platformdirs import user_config_path, user_data_path

APP_NAME = 'name'
APP_AUTHOR = 'author'


def get_data_path() -> Path:
    """Returns the absolute Path object for data directory.

    If the directory does not exist, it will be created.
    """
    return user_data_path(
        appname = APP_NAME,
        appauthor = APP_AUTHOR,
        roaming = False,
        ensure_exists = True
    )


def get_config_path() -> Path:
    """Returns the absolute Path object for config directory.

    If the directory does not exist, it will be created.
    """
    return user_config_path(
        appname = APP_NAME,
        appauthor = APP_AUTHOR,
        roaming = False,
        ensure_exists = True
    )


DATA_DIR = get_data_path()
CONFIG_DIR = get_config_path()

DATA_FILE: Path = DATA_DIR / 'example.json'
DOTENV_PATH: Path = CONFIG_DIR / '.env'

