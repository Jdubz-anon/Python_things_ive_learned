import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore the structure of the data
filename = r'/home/jdubzanon/Documents/PythonCrashCourseData/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = '/home/jdubzanon/Documents/PythonCrashCourseData/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
#looping through dicts and finding magnitude

magnitudes, longitudes, latitudes, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    #multilayer dictionary key:value format
    mag = eq_dict['properties']['mag']
    magnitudes.append(mag)
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    longitudes.append(long)
    latitudes.append(lat)
    hover_text.append(title)

#map earthquakes
data =[{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout' : my_layout}
offline.plot(fig, filename='global_earthquakes.html')

