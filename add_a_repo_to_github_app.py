import  requests
import json
import os
import argparse
from dotenv import load_dotenv
from list_repos_in_org import list_repos_in_github_org
from list_github_app_matching_name import list_github_apps_in_organization_matching_name

def add_repository_to_github_app(organization:str,matching_repos: list[dict], app_short_list: list[dict] ):
    """
    add repos to github app using rest api
    :return:
    https://docs.github.com/en/rest/apps/installations?apiVersion=2022-11-28#add-a-repository-to-an-app-installation
    """
    # Assuming that the Github app name doesnot contain any special cgharacters and github app name is same as app_slug.
    print(f'Matching repos are:  {matching_repos}')
    print(f'GitHub App details are:  {app_short_list}')
    add_repo_to_github_app_endpoint = f'https://api.github.com/user/installations/{id}/repositories/REPOSITORY_ID
'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def main():
    """ to test the script"""
    load_dotenv()
    organization = os.getenv('ORGANIZATION')
    parser = argparse.ArgumentParser(description="Add specific repos matching a string in repo names to a github teams")
    parser.add_argument("--search_string", required=True, type=str, help="github repo name search string")
    parser.add_argument("--github_app_name", required=True, type=str, help="github repo name search string")
    args = parser.parse_args()
    search_string = args.search_string
    github_app_name = args.github_app_name
    # Function call for repo list
    matching_repos = list_repos_in_github_org(organization, search_string)
    # Function call for github app details
    app_short_list = list_github_apps_in_organization_matching_name(organization, github_app_name)
    # Fucntion call for adding repo to github app
    add_repository_to_github_app(organization, matching_repos, app_short_list)


if __name__ == "__main__":
    main()