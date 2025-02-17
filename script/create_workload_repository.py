
import json
from os import environ

from repository import github

def build_repository():
    auth = environ["AUTH_TOKEN"]

    name = f"rg-{environ["ENVIRONMENT"]}-{environ["ROLE"]}-{environ["COUNTER"].zfill(3)}"
    repository_definition = github.create_repository_from_template(auth, name, environ["DESCRIPTION"])

    print(repository_definition)


if __name__ == "__main__":
    build_repository()
