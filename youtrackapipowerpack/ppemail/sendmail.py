# coding=utf-8
import settings

__author__ = 'gabriel.pereira'


class SendMail(object):
    def __init__(self):
        self.driver = settings.MAIL_DRIVER
        self.configure()

    def send_mail(self, from_email, to_email, subject, body, options=[]):
            return self.dispatcher.send_mail(from_email, to_email, subject, body, options=[])

    def configure(self):
        if self.driver == 'smtp':
            from driversemail import DriverSmtp
            self.dispatcher = DriverSmtp()

        elif self.driver == 'mandrill':
            from driversemail import DriverMandrill
            self.dispatcher = DriverMandrill()
        else:
            raise Exception('No mail driver found')
