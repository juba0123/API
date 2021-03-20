from github import Github
import json


g = Github("09925086ebed882c045be5804beea5f46aaa5a1a")

data = []
repo = g.get_repo("PyGithub/PyGithub")
open_issues = repo.get_issues(state='open')
for issue in open_issues:
    data.append(issue)

data = str(data)
data2 = json.loads(data)
json.dumps(data2, separators=('issue(', ','))
#json.dump(data2)
