from os import environ

from .repository import github

def build_repository():
    auth = environ["GH_TOKEN"]

    name = f"rg-{environ["ENVIRONMENT"]}-{environ["ROLE"]}-{environ["COUNTER"].zfill(3)}"
    repository_definition = github.create_repository_from_template(auth, name, environ["DESCRIPTION"])

    html_url = repository_definition["html_url"]
    full_name = repository_definition["full_name"]
    contents_url = repository_definition["contents_url"].replace("{+path}", "")
    github.add_file_to_repository(auth, contents_url, "main.bicep", "initial commit")


if __name__ == "__main__":
    build_repository()
