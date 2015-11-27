# coding=utf-8
from youtrackapipowerpack import youtrack_connection
from settings import ASANA_PERSONAL_ACCESS_TOKEN
import asana
from datetime import datetime

__author__ = 'davis.peixoto'

asana_client = asana.Client.access_token(ASANA_PERSONAL_ACCESS_TOKEN)
now = datetime.now()
string_to_asana = 'Deploy da task feito em ' + now.strftime('%d/%m/%Y às %H:%M')


def getissue(connection, issue_id):
    """

    :param connection:
    :param issue_id:
    :return:
    """
    return connection.getIssue(issue_id)


def printissue(data):
    """

    :param data:
    """
    print(data.__str__())


# asd = connection.getIssues('MGT', '#Unresolved', 0, 10)

# for i in asd:
#    printissue(getissue(connection, i["id"]))

x = getissue(youtrack_connection, 'MGT-64')

ret = asana_client.stories.create_on_task(x.AsanaID, {'text': string_to_asana})
print(ret.__str__())

# if x["Estimation"] >= x["Spent time"]:
#    atraso = int(x["Spent time"]) - int(x["Estimation"])
#    print "atraso %s minutos" % atraso
# else:
#    print 'em dia'
