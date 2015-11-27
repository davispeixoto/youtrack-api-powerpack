from settings import YOUTRACK_ENDPOINT, YOUTRACK_USERNAME, YOUTRACK_PASSWORD
from youtrack.connection import Connection

__author__ = 'Davis Peixoto'
__version__ = '0.1.0'

youtrack_connection = Connection(YOUTRACK_ENDPOINT, YOUTRACK_USERNAME, YOUTRACK_PASSWORD)