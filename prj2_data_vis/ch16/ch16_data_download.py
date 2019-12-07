# -------------------------------------------------
# Extracting a Month of Weather data from CSV file
# -------------------------------------------------

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() # Draws labels diagonally so they don't overlap.
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

# -------------------------------------------------
# Extracting a Year of Weather data from CSV file
# -------------------------------------------------

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() # Draws labels diagonally so they don't overlap.
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

# -------------------------------------------------
# Plotting a Second Data Series
# -------------------------------------------------

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # returns the next row of data. 1st line of the file.

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and high/low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red')
ax.plot(dates,lows, c='blue')

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() # Draws labels diagonally so they don't overlap.
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

# -------------------------------------------------
# Shading an Area in the Chart
# -------------------------------------------------

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # returns the next row of data. 1st line of the file.

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and high/low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red',alpha=0.5)
ax.plot(dates,lows, c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() # Draws labels diagonally so they don't overlap.
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

# -------------------------------------------------
# Error Checking
# -------------------------------------------------
import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates, high temps, and low temps from csv file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red',alpha=0.5)
ax.plot(dates,lows, c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() # Draws labels diagonally so they don't overlap.
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

# -------------------------------------------------
# converting machine generated json into human readable format
# -------------------------------------------------
import json

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data_30day.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data,f,indent=4)


# -------------------------------------------------
# Mapping global Data Sets: JSON Format
# -------------------------------------------------
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/recent_eq_data_30days.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Make a list of all earthquakes
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts)) # Total number of earthquakes

# Extracting the magnitutes and locations
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
    },
}]

# To see other available colorscdales
# for key in colors.PLOTLY_SCALES.keys():
#   print(key)
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data':data,'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')

