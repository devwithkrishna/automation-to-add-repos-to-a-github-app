# automation-to-add-repos-to-a-github-app
create an automation to add repos to a github app

* Reference : [list-app-installations-for-an-organization](https://docs.github.com/en/rest/orgs/orgs?apiVersion=2022-11-28#list-app-installations-for-an-organization)

# Credentials used for authorization

| credential | purpose | check              |
|------------|---------|--------------------|
| fine grained personal access token | this is used for all purpose like listing repos, github app detailsetc | :heavy_check_mark: |
| personal access token classic | this is used for api call to add repos to github app | :heavy_check_mark: |

**personal access token classic - provide `all repo access`**
![Screenshot_3-5-2024_234236_github com](https://github.com/devwithkrishna/automation-to-add-repos-to-a-github-app/assets/108367225/cc853576-127e-4b17-8059-8417c766d23b)


# parameters 

| input name | type | description |
|------------|------|-------------|
| organization | string | Github organizarion name. Default - `devwithkrishna` |
| search-string | string | name of github repo starts with |
| github-app-name | string | name of github app to which repositories will be added |


# How code works

* Based on the search string, the code will use the end point `https://api.github.com/orgs/{orgaization}/repos` to list all
  repositories and get the ones matching. matching is done in a way that the seach string is considered as begining word of
  Github repository name. - _list_repos_in_org.py_ & _list_github_app_matching_name.py_

* Once its listed, later script pulls down all available github apps installed across the organization using the 
  endpoint `https://api.github.com/orgs/{organization}/installations` - _list_all_github_app_in_org.py_

* Based on the Github app name provided as input it gathers the installation id. This is later used.

* using the matching repos based on search string and github app name provded, the script will use these details to the
  endpoint `https://api.github.com/user/installations/{github_app_installation_id}/repositories/{repo_id}`. This uses 
  the personal access token classic to add repositories to github app - _add_a_repo_to_github_app.py_
