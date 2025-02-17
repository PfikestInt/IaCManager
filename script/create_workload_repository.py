from os import environ
import pprint

from .repository import github

def build_repository():
    auth = environ["GH_TOKEN"]

    name = f"rg-{environ["ENVIRONMENT"]}-{environ["ROLE"]}-{environ["COUNTER"].zfill(3)}"
    repository_definition = github.create_repository_from_template(auth, name, environ["DESCRIPTION"])

    # pprint.pprint(repository_definition)

    html_url = repository_definition["html_url"]
    full_name = repository_definition["full_name"]
    github.clone_to(full_name, "develop", "new_repo")

if __name__ == "__main__":
    build_repository()
