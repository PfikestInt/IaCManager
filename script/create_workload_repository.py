
from os import environ

from github import Auth, Github

def build_repository():
    auth = Auth(environ["AUTH_TOKEN"])
    gh = Github(auth=auth)

    for repo in gh.get_user().get_repos():
        print(repo.name)

    gh.close()


if __name__ == "__main__":
    build_repository()
