# coding=utf-8
from youtrackapipowerpack import youtrack_connection
from youtrackapipowerpack.asanautils import AsanaUtils

__author__ = 'davis.peixoto'


class YoutrackUtils(object):

    def __init__(self):
        self.issues_list = []
        self.asanaUtils = AsanaUtils()

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

<<<<<<< HEAD
    def mark_as_deployed(self, issueid):
        youtrack_connection.executeCommand("State Deployed")
=======
    @staticmethod
    def get_issues(filter_query, offset, limit):
        return youtrack_connection.getAllIssues(filter_query, offset, limit)

    @staticmethod
    def set_issue_status(issue_id, status):
        youtrack_connection.executeCommand(issue_id, ('State ' + status))

    @staticmethod
    def get_user(user):
        return youtrack_connection.getUser(user)

>>>>>>> 3133fae66923c40a974de9b8b52e80bcc0c8594a
