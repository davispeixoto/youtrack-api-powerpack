from os.path import join, dirname
from os import environ
from dotenv import load_dotenv

__author__ = 'davis.peixoto'

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YOUTRACK_ENDPOINT = environ.get("YOUTRACK_ENDPOINT")
YOUTRACK_USERNAME = environ.get("YOUTRACK_USERNAME")
YOUTRACK_PASSWORD = environ.get("YOUTRACK_PASSWORD")

ASANA_PERSONAL_ACCESS_TOKEN = environ.get("ASANA_PERSONAL_ACCESS_TOKEN")
NOTIFICATION_EMAIL = environ.get("NOTIFICATION_EMAIL")
