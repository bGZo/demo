#! /usr/bin/python3
from github import Github
from cfig import githubToken

# using an access token
g = Github(githubToken)

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

# NOTE: if there's a archived repo for you, following error will show you.
# 'github.GithubException.GithubException: 403 {"message": "Repository was archived so is read-only.", "documentation_url": "https://docs.github.com/rest/reference/repos#update-a-repository"}'
#via https://github.com/PyGithub/PyGithub/issues/1115