from base64 import b64encode
import os
import subprocess

import requests


def clone_to(auth, repository, branch, path):
    """
                  git config --global user.email "hi@aliasifkhan.com"
                  git config --global user.name "aliasifk"
                  git config --global credential.helper cache
                  git clone https://${{secrets.ACCESS_TOKEN}}@github.com/aliasifk/xxxxxx
                  cp index.js clonedFolder/ -f
                  cd clonedFolder
                  git add .
                  git commit -m "$(date)"
                  git push 
    """   
    command = [
        "git",
        "config",
        "--global",
        "user.email",
        "repo.creator@noreply.github.com",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)

    command = [
        "git",
        "config",
        "--global",
        "user.name",
        "Repo Creator",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)

    command = [
        "git",
        "config",
        "--global",
        "credential.helper",
        "cache",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)

    command = [
        "git",
        "clone",
        f"https://{auth}@github.com/{repository}",
        path,
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)


def pull(path):
    cwd = os.curdir
    os.chdir(path)

    command = [
        "git",
        "pull",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)
        
    os.chdir(path)


def push(path, message):
    cwd = os.curdir
    os.chdir(path)

    command = [
        "git",
        "add",
        "-A"
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)

    command = [
        "git",
        "commit",
        "-am",
        message
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)

    command = [
        "git",
        "push",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)
    
    os.chdir(cwd)


def create_repository_from_template(authorization, name, description):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {authorization}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = [
        '"owner":"PfikestInt"',
        f'"name":"{name}"',
        f'"description":"{description}"',
        '"include_all_branches":true',
        '"private":false'
    ]

    response = requests.post(
        url="https://api.github.com/repos/PfikestInt/WorkloadTemplate/generate",
        headers=headers,
        data="{" + ",".join(data) + "}",
    ).json()

    if response.get("status", "200") != "200":
        for error in response["errors"]:
            print(error)
        exit(1)
    
    return response


def add_file_to_repository(authorization, url, filename, message):
    with open(filename, "r") as file_in:
        contents = file_in.read()

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {authorization}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = [
        '"owner":"PfikestInt"',
        f'"message":"{message}"',
        f'"content":"{b64encode(contents.encode()).decode()}',
    ]

    response = requests.put(
        url=f"{url}/{filename}",
        headers=headers,
        data="{" + ",".join(data) + "}",
    ).json()

    if response.get("status", "200") != "200":
        for error in response["errors"]:
            print(error)
        exit(1)
    
    return response


def submodule_init():
    command = [
        "git",
        "submodule",
        "update",
        "--init",
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode > 0:
        print(f"Return code: {result.returncode}")
        print(f"Error: {result.stderr}")
        exit(1)
