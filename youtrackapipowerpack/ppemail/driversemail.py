# coding=utf-8
from HTMLParser import HTMLParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mandrill
from pip._vendor.html5lib.sanitizer import HTMLSanitizerMixin

import settings

__author__ = 'gabriel.pereira'


class DriverMandrill(object):
    mandrill_client = None

    def __init__(self):
        pass

    def get_instance(self):
        if self.mandrill_client is None:
            import mandrill
            self.mandrill_client = mandrill.Mandrill(settings.MANDRIL_APIKEY)

    def send_mail(self, from_email, to_email, subject, body, options=[]):
        try:
            template_name = None
            template_content = None
            async = False
            ip_pool = None
            send_at = None
            result = None

            if from_email is None or from_email == '':
                from_email = settings.MAIL_FROM_ADDRESS

            # message structure
            message = {
                'html': body,
                'text': body,
                'subject': subject,
                'from_email': from_email,
                'to': []
            }

            # Parse e-mails that will receive the message
            if isinstance(to_email, dict) and len(to_email) <= 3:
                message['to'] = [to_email]
            elif isinstance(to_email, list):
                message['to'] = to_email
            elif isinstance(to_email, basestring):
                message['to'] = [{'email':to_email}]
            else:
                raise Exception('Unable to parse e-mail to')

            # Parse options
            if len(options) > 0:
                for option in options:
                    if option[0] == 'template_name':
                        template_name = option[1]
                    elif option[0] == 'template_content':
                        template_content = option[1]
                    elif option[0] == 'ip_pool':
                        ip_pool = option[1]
                    elif option[0] == 'async':
                        async = option[1]
                    elif option[0] == 'send_at':
                        send_at = option[1]
                    else:
                        message[option[0]] = option[1]

            self.get_instance()

            if template_name is None and template_content is None:
                result = self.mandrill_client.messages.send(message=message, async=async, ip_pool=ip_pool, send_at=send_at)
            else:
                pass
                result = self.mandrill_client.messages.send_template(template_name=template_name, template_content=template_content, message=message)

        except mandrill.Error, e:
            return dict(status='NOK', message='[ERROR] Problem to send mail with mandrill : ' + str(e))

        else:
            return dict(status='OK', message=result)


class DriverSmtp(object):
    smtp_client = None

    def __init__(self):
        self.config = None

    def send_mail(self, from_email, to_email, subject, body, options=[]):
        try:
            if from_email is None or from_email == '':
                from_email = settings.MAIL_FROM_ADDRESS

            self.get_instance()

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to_email

            # html detect
            #TODO: this should be better than this, but it's ok for while
            if is_html(body) is True:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            self.smtp_client.sendmail(from_email, to_email, msg.as_string(), options)
            self.smtp_client.close()

        except Exception, e:
            return dict(status='NOK', message='[ERROR] Problem to send mail with smtp : ' + str(e))
        else:
            return dict(status='OK', message='E-mail sent.')

    def get_instance(self):
        if self.smtp_client is None:
            import smtplib
            if settings.MAIL_PORT is not None and settings.MAIL_PORT != '':
                self.smtp_client = smtplib.SMTP(settings.MAIL_HOST, settings.MAIL_PORT)
            else:
                self.smtp_client = smtplib.SMTP(settings.MAIL_HOST)

            # TLS
            if settings.MAIL_TLS is True:
                self.smtp_client.starttls()

            self.smtp_client.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)


class TestHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)

        self.elements = set()

    def handle_starttag(self, tag, attrs):
        self.elements.add(tag)

    def handle_endtag(self, tag):
        self.elements.add(tag)


def is_html(text):
        elements = set(HTMLSanitizerMixin.acceptable_elements)

        parser = TestHTMLParser()
        parser.feed(text)

        return True if parser.elements.intersection(elements) else False
