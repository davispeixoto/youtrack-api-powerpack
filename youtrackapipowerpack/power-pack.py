# coding=utf-8
import subprocess
from youtrackapipowerpack import youtrack_connection

__author__ = 'davis.peixoto'

# asd = connection.getIssues('MGT', '#Unresolved', 0, 10)

# for i in asd:
#    printissue(getissue(connection, i["id"]))

x = youtrack_connection.getIssue('MGT-64')

# if x["Estimation"] and x["Spent time"]:
#    if x["Spent time"] > x["Estimation"]:
#        delay = int(x["Spent time"]) - int(x["Estimation"])
