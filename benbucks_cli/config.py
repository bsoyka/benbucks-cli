from pathlib import Path

from appdirs import user_data_dir

CONNECTION_FILE = (
    Path(user_data_dir("benbucks", "bsoyka", roaming=True)) / "connection.txt"
)

CONNECTION_FILE.parent.mkdir(parents=True, exist_ok=True)

CONNECTION_STRING = (
    CONNECTION_FILE.read_text().strip() if CONNECTION_FILE.exists() else None
)
