import os

API_PORT = int(os.environ.get("API_PORT", 8000))
API_HOST = os.environ.get("API_PORT", "0.0.0.0")

TEXT_IO_FILE_PATH = "database.csv"
TEXT_IO_MODE = "a+"
