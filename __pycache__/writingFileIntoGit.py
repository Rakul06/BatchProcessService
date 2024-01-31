import requests
import base64

def upload_to_github(repo_owner, repo_name, file_path, github_token, file_content, dag_name):
    # API endpoint for creating or updating a file in a repository
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{dag_name}.py'

    # Headers with the GitHub token for authentication
    headers = {
        'Authorization': f'token {github_token}',
        'Content-Type': 'application/json',
    }

    # Base64 encode the file content
    content_base64 = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

    # Prepare the request payload
    payload = {
        'message': 'Upload file via API',
        'content': content_base64,
    }

    # If the file already exists, get its current SHA
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        current_sha = response.json()['sha']
        payload['sha'] = current_sha

    # Make the request to create or update the file
    response = requests.put(api_url, headers=headers, json=payload)

    # Check the response
    if response.status_code == 200 or response.status_code == 201:
        print(f'Successfully uploaded file to {file_path} in {repo_owner}/{repo_name}.')
    else:
        print(f'Failed to upload file. Status code: {response.status_code}, Response: {response.text}')

# Example usage
repo_owner = 'Rakul06'
repo_name = 'Batch-Process-POC'
file_path = 'Z:\dags\Creating_dags_using_python_operator.py'
github_token = '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'

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

upload_to_github(repo_owner, repo_name, file_path, github_token, file_content,"newDag")


