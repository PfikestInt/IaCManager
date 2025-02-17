import os
import subprocess

import requests


def clone_to(repository, branch, path):
    command = [
        "gh",
        "repo",
        "clone",
        repository,
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
        "-A"
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
