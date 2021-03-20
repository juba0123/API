from github import Github
import json


g = Github("6a5e867f48c766c28e391038fc4fee91690f8d8a")
repo = g.get_repo("PyGithub/PyGithub")
open_issues = repo.get_issues(state='open')
for issue in open_issues:
    with open('personal.json', 'w') as json_file:
        json.dump(repo, json_file)
