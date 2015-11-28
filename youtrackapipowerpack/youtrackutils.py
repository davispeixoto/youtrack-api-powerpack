# coding=utf-8
from youtrackapipowerpack import youtrack_connection

__author__ = 'davis.peixoto'


class YoutrackUtils(object):
    issues_list = None

    def __init__(self):
        pass

    def load_issues(self, project, filter_query, offset, limit):
        self.issues_list = youtrack_connection.getIssues(project, filter_query, offset, limit)

    def get_late_issues(self):
        late = []

        for i in self.issues_list:
            x = youtrack_connection.getIssue(i["id"])
            if x["Estimation"] and x["Spent time"]:
                if x["Spent time"] > x["Estimation"]:
                    late.append(x)

        return late
