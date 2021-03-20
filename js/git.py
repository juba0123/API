from github import Github

# using an access token
g = Github("6a5e867f48c766c28e391038fc4fee91690f8d8a")

# Github Enterprise with custom hostname
# g = Github(base_url="https://juba0123/api/v3", login_or_token="6a5e867f48c766c28e391038fc4fee91690f8d8a")

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
