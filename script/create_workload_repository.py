
import json
from os import environ

import requests

def build_repository():
    """
        curl -L \
          -X POST \
          -H "Accept: application/vnd.github+json" \
          -H "Authorization: Bearer ${{ steps.app_token.outputs.token }}" \
          -H "X-GitHub-Api-Version: 2022-11-28" \
          https://api.github.com/repos/PfikestInt/WorkloadTemplate/generate \
          -d '{"owner":"PfikestInt","name":"rg-${{ github.event.inputs.environment-type }}-${{ github.event.inputs.role }}-${{ env.PADDED_COUNTER }}","description":"${{ github.event.inputs.description }}","include_all_branches":true,"private":false}' > results.json
        echo "REPO_URL=$(jq '.html_url' results.json)" >> "$GITHUB_OUTPUT"
    """
    auth = environ["AUTH_TOKEN"]

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {auth}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = [
        '"owner":"PfikestInt"',
        f'"name":"rg-{environ["ENVIRONMENT"]}-{environ["ROLE"]}-{environ["COUNTER"].zfill(3)}"',
        f'"description":"{environ["DESCRIPTION"]}"',
        '"include_all_branches":true',
        '"private":false'
    ]
    
    response = requests.post(
        url="https://api.github.com/repos/PfikestInt/WorkloadTemplate/generate",
        headers=headers,
        data="{" + ",".join(data) + "}",
    )
    print(response.text)


if __name__ == "__main__":
    build_repository()
