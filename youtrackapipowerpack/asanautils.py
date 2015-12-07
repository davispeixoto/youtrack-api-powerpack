# coding=utf-8
from settings import ASANA_PERSONAL_ACCESS_TOKEN
import asana
from datetime import datetime

__author__ = 'davis.peixoto'


class AsanaUtils(object):
    asana_client = None
    now = None
    message = None

    def __init__(self):
        self.asana_client = asana.Client.access_token(ASANA_PERSONAL_ACCESS_TOKEN)
        self.now = datetime.now()
        self.message = 'Deploy made at ' + self.now.strftime('%d/%m/%Y às %H:%M')
        self.message = self.message + "\r\n" + "Please verify and close this task."

    def send_notification(self, asana_id):
        return self.asana_client.stories.create_on_task(asana_id, {'text': self.message})

    def get_task(self, asana_id):
        return self.asana_client.tasks.find_by_id(asana_id)
