import re
import requests

# GitHub repository details
github_username = 'Rakul06'
github_repo = 'Batch-Process-POC'
github_token = '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'

# Specify the DAG file path and DAG ID
dag_file_path = 'Test_Batch_v003.py'
dag_id = 'Test_Batch_v003'

# Specify the new schedule interval
new_schedule_interval = '0 3 * * *'

# Pattern to search for in the DAG file
pattern = re.compile(r"schedule_interval\s*=\s*'[^\']*'", re.MULTILINE)

# Replacement string with the new schedule interval
replacement = f"schedule_interval = '{new_schedule_interval}'"

# GitHub API endpoint for updating a file
github_api_url = f'https://api.github.com/repos/{github_username}/{github_repo}/contents/{dag_file_path}'

# Fetch the current content of the file from GitHub
headers = {
    'Authorization': f'Token {github_token}',
    'Accept': 'application/vnd.github.v3+json',
}
response = requests.get(github_api_url, headers=headers)
response.raise_for_status()
file_content = response.json()['content']

# Decode the base64-encoded content
import base64
current_content = base64.b64decode(file_content).decode('utf-8')

# Perform the replacement in memory
updated_content = re.sub(pattern, replacement, current_content)

# Encode the updated content in base64
updated_content_base64 = base64.b64encode(updated_content.encode('utf-8')).decode('utf-8')

# Prepare data for updating the file
data = {
    'message': f'Update schedule interval for DAG {dag_id}',
    'content': updated_content_base64,
    'sha': response.json()['sha'],
}

# Make a PUT request to update the file on GitHub
response = requests.put(github_api_url, headers=headers, json=data)
response.raise_for_status()

print(f"Schedule interval for DAG '{dag_id}' updated to '{new_schedule_interval}' in '{dag_file_path}' on GitHub.")
