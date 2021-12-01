#! /usr/bin/python3
from github import Github
from cfig import GithubToken
from config import (
    IssueTableHead,
    IssueTableTemplate
)

issueFileName = "index.md"

# using an access token
g = Github(GithubToken)
me = g.get_user().login


repo = g.get_repo("bgzocg/2021")
openIssues = repo.get_issues(state='open', creator=me, sort='updated')

# <class 'github.PaginatedList.PaginatedList'>
# openIssues.sort(key=issue.updated_at)


with open(issueFileName, "w+") as f:
    f.write( IssueTableHead )

    for issue in openIssues:
        issueName = str(issue.title)
        issueUpdate = str(issue.updated_at)
        issueUrl = '#'+ str(issue.number)

        f.write( IssueTableTemplate.format(
            issueName = issueName, 
            issueUpdate = issueUpdate, 
            issueUrl = issueUrl
        ) )

# print(repo.get_issue(number=1))
