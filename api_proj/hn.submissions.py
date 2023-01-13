import json
from operator import itemgetter
import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
# r stores the response which is a list for this particular api request
# see top-stories.json
r = requests.get(url)

# puts values in r into a json format
submission_ids = r.json()
# empty list
submission_dicts = []

# file = 'top-stories.json'
# with open(file, 'w') as f:
#     json.dump(submission_ids,f,indent=4)

# process information about each submission
# line 18 is looping through a list see top-stories.json
for submission_id in submission_ids[:10]:
    # print(submission_id)
    urls = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json?"
    r = requests.get(urls)
    response_dict = r.json()


# build dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
# print(submission_dicts)

# key=itemgetter(comments) is sorting by the number of comments
# this line of code(below here) is saying sort submission_dicts(list of dictionaries
# that we made; see code above here) by the number of comments(key=). we get the value
# of comments by using itemgetter(comments), then reverse the sort returning the largest comment value first
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)
# print('after sorted and itemgetter: ',submission_dicts)

for submission_dict in submission_dicts:
    print(f"\n title: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"comments: {submission_dict['comments']}")
