import requests

#make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code : {r.status_code}')

#store api response in a variable
reponse_dict = r.json()
print(f'Total repsoitories: {reponse_dict["total_count"]}')

#get the keys in the dictionary results
#print(reponse_dict.keys())

#explore info about repositories
repo_dicts = reponse_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

#examine first repository
#repo_dict = repo_dicts[0]
for repo_dict in repo_dicts:
    print('\nSelected information about repositories')
    print(f'Name: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    print(f'Created: {repo_dict["created_at"]}')
    print(f'Updated: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')

#print(f'\nKeys: {len(repo_dict)}')
#for key in sorted(repo_dict.keys()):
    #print(key)
#print(type(repo_dicts))
#print(type(reponse_dict))