from os import environ
import pprint
import shutil

from .repository import github

def build_repository():
    auth = environ["GH_TOKEN"]

    name = f"rg-{environ["ENVIRONMENT"]}-{environ["ROLE"]}-{environ["COUNTER"].zfill(3)}"
    repository_definition = github.create_repository_from_template(auth, name, environ["DESCRIPTION"])

    # pprint.pprint(repository_definition)

    html_url = repository_definition["html_url"]
    full_name = repository_definition["full_name"]
    github.clone_to(auth, full_name, "develop", "new_repo")
    github.submodule_init()

    shutil.copy2("bicep-modules/main.bicep", "new_repo/main.bicep")
    github.push("new_repo", "initial commit")


if __name__ == "__main__":
    build_repository()
