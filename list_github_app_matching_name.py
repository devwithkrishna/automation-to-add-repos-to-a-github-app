# reference: https://docs.github.com/en/rest/orgs/orgs?apiVersion=2022-11-28#list-app-installations-for-an-organization
import  requests
import json
import argparse
import os
from dotenv import load_dotenv

def list_github_apps_in_organization_matching_name(organization: str, github_app_name: str):
    """
    list GitHub apps in the orgaization
    :param organization:
    :return:
 reference: https://docs.github.com/en/rest/orgs/orgs?apiVersion=2022-11-28#list-app-installations-for-an-organization
    """

    list_github_app_endpoint = f'https://api.github.com/orgs/{organization}/installations'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(list_github_app_endpoint, headers=headers)
    response_json = response.json()
    response_code = response.status_code

    if response_code == 200:
        print(f'Listing GitHub Apps in {organization} organization successful')
    else:
        print(f'Listing GitHub Apps in {organization} failed')

    total_num_of_github_app_installations = response_json['total_count']
    print(f'Found {total_num_of_github_app_installations} GitHub App in {organization} organization')

    # Extract the list of dictionaries
    list_of_installations = response_json["installations"]

    # Convert list of dictionaries to JSON string
    json_data = json.dumps(list_of_installations, indent=4)

    # Write JSON string to a file
    with open("list_of_github_installations.json", "w") as file:
        file.write(json_data)

    app_short_list = []
    for app in list_of_installations:
        app_dict = {}
        if app['app_slug'] == github_app_name:
            app_dict['id'] = app['id']
            app_dict['app_id'] = app['app_id']
            app_dict['app_slug'] = app['app_slug']
            app_short_list.append(app_dict)

    return app_short_list

def main():
    """ To test the code """
    load_dotenv()
    GH_TOKEN = os.getenv('gh_token')
    organization = os.getenv('ORGANIZATION')
    # organization = 'devwithkrishna'
    parser = argparse.ArgumentParser(description="Get the App installation id from name")
    parser.add_argument("--github_app_name", required=True, type=str, help="github repo name search string")
    args = parser.parse_args()
    github_app_name = args.github_app_name
    # Function call
    app_short_list = list_github_apps_in_organization_matching_name(organization, github_app_name)


if __name__ == '__main__':
    main()



