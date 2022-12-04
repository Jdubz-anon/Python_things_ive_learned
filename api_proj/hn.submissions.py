import json
from operator import itemgetter
import requests

url =  'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
r = requests.get(url)

submission_ids = r.json()
submission_dicts = []
# file = 'topstories.json'
# with open(file, 'w') as f:
#     json.dump(response,f,indent=4)

for submission_id in submission_ids[:30]:
    urls = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json?"
    r = requests.get(urls)
    print(f"id: {submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    #build dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),
                              reverse=True)

    for submission_dict in submission_dicts:
        print(f"\n title: {submission_dict['title']}")
        print(f"Discusson link: {submission_dict['hn_link']}")
        print(f"comments: {submission_dict['comments']}")