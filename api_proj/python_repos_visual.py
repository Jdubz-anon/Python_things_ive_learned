import requests

from plotly.graph_objs import Bar
from plotly import offline

#make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

#store api response in a variable
reponse_dict = r.json()

#'items' is a list inside the json file, which is basically a dictionary,
# that contains the information that was requested from the api call
repo_dicts = reponse_dict['items']

repo_links, stars, labels = [], [], []

#looping through the json file adding items in list to create plot points
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href= '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    #creating data for the 'hovertext' key in data variable/dictionary (see below)
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

#make visualization

color = (150,70,200)
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'autocolorscale': True,
        'line': {'width': 1.5, 'color': color},
        'colorbar': {'borderwidth': 3},

    },
    'opacity' : 0.6,
}]


my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont' : {'size': 24},
        'tickfont': {'size': 14}
              },
    'yaxis' : {
        'title': 'Stars',
        'titlefont': {'size': 24 },
        'tickfont': {'size': 14}

    },

}

fig = {'data':data,
       'layout': my_layout

       }
offline.plot(fig, filename='python_repos.html')
