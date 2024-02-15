import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

FILE_PATH = os.getenv("FILE_PATH")
IMAGE_DIR = os.getenv("IMAGE_DIR")
