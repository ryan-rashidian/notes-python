"""This module contains filesystem path(s) used by this application."""

from pathlib import Path
from platformdirs import user_data_path


APP_NAME = 'APP'
APP_AUTHOR = 'Author Name'
FILE_NAME = 'example.json'


def get_data_path(file_name: str) -> Path:
    """Returns the absolute Path object for given data file.

    If the directory does not exist, it will be created.
    """
    data_path = user_data_path(
        appname = APP_NAME,
        appauthor = APP_AUTHOR,
        roaming = False,
        ensure_exists = True
    )
    return data_path / file_name


def ensure_file_exists(file_path: Path) -> None:
    """Checks if the data file exists. If not, it will be created."""
    if not file_path.exists():
        print(f'Creating new task file at: {file_path}')
        file_path.write_text('{}', encoding='UTF-8')


DATA_PATH = get_data_path(FILE_NAME)
ensure_file_exists(DATA_PATH)

