# coding=utf-8
__author__ = 'davis.peixoto'

import subprocess


class gitutils(object):
    cd = None

    def __init__(self):
        pass

    def get_commit_string(self, path):
        pass

    def get_tags_list(self):
        pass


proc_latest = subprocess.Popen("cd /home/davis.peixoto/projects/rentcars; git tag | sort --version-sort -r | head -n 1",
                               stdout=subprocess.PIPE, shell=True)
latest_tag = proc_latest.stdout.read()

# from http://stackoverflow.com/questions/7353054/call-a-shell-command-containing-a-pipe-from-python-and-capture-stdout
#
#p1 = subprocess.Popen(["cat", "file.log"], stdout=subprocess.PIPE)
#p2 = subprocess.Popen(["tail", "-1"], stdin=p1.stdout, stdout=subprocess.PIPE)
#p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
#output,err = p2.communicate()

proc_previous = subprocess.Popen(
    "cd /home/davis.peixoto/projects/rentcars; git tag | sort --version-sort -r | head -n 2 | tail -n 1",
    stdout=subprocess.PIPE, shell=True)
previous_tag = proc_previous.stdout.read()

proc_list = subprocess.Popen(
    "cd /home/davis.peixoto/projects/rentcars; git log --pretty=format:\"%aN%x09%ai%x09%s\" " + str(
        previous_tag) + ".." + str(latest_tag) + " | grep -E -o '[A-Z]{1,6}-[0-9]{1,9}' | sort | uniq ",
    stdout=subprocess.PIPE, shell=True)
commits_list = proc_list.stdout.read()

the_string = "git log --pretty=format:\"%aN%x09%ai%x09%s\" `git tag | sort --version-sort -r | head -n 2 | tail -n 1`..`git tag | sort --version-sort -r | head -n 1` | grep -E -o '[A-Z]{1,6}-[0-9]{1,9}' | sort | uniq"
other_string = "git log --pretty=format:\"%aN%x09%ai%x09%s\" Production..master | sort | grep erg | nl | grep -E '([A-Z]{1,6}-[0-9]{1,6})'"
