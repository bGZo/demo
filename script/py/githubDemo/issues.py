#! /usr/bin/python3
from github import Github

# using an access token
g = Github("")

repo = g.get_repo("bgzocg/2021")
open_issues = repo.get_issues(state='open')
for issue in open_issues:
    tmp="- "+issue.title
    print(tmp)

# print(repo.get_issue(number=1))

