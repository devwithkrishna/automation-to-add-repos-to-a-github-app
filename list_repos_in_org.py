import  requests
import os
import argparse
from dotenv import load_dotenv

def list_repos_in_github_org(orgaization: str, search_string: str):
    """ get the repo id of repos natching the search string """

    # GitHub endpoint for listing repos under an organization
    repo_url = f"https://api.github.com/orgs/{orgaization}/repos"
    # print(f"github api endpoint url {repo_url}")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # Define pagination parameters
    per_page = 20  # Number of records per page
    page = 1  # Initial page number
    params = {'per_page': per_page, 'page': page}

    all_repositories = []
    while True:
        # Add pagination parameters to the URL
        response = requests.get(repo_url, headers=headers, params=params)
        if response.status_code == 200:
            # Parse the JSON response
            repositories = response.json()
            if not repositories:
                break
            all_repositories.extend(repositories)
            params["page"] += 1
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
            break

    # Get the repo names from the list of dictionaries and add to another list
    list_of_repo_names = []
    for repo in all_repositories:
        repo_dict = {}
        repo_dict['name'] = repo['full_name']
        repo_dict['id'] = repo['id']
        list_of_repo_names.append(repo_dict)

    # Finding repos starting with search string
    matching_repos = [repo for repo in list_of_repo_names if repo['name'].startswith(f'{orgaization}/{search_string}')]
    print(f"Matching repos {search_string} are: {matching_repos}")
    return matching_repos


def main():
    """ main function to test"""
    load_dotenv()
    organization = os.getenv('ORGANIZATION')
    parser = argparse.ArgumentParser(description="Add specific repos matching a string in repo names to a github teams")
    parser.add_argument("--search_string", required=True, type=str, help="github repo name search string")
    args = parser.parse_args()
    search_string = args.search_string
    matching_repos = list_repos_in_github_org(organization, search_string)

if __name__ == '__main__':
    main()