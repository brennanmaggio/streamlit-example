"""
Name: Brennan Maggio
CS230: Section 5
Data: Volcanoes
URL: http://localhost:8501/

Description:

This program is my final project. I begin by using a bar chart that shows the number
of volcanoes at different elevations. The color of this graph can also be changed.
Next, I used Folium to create a map of volcano names and eruption dates. This is
accompanied by a table showing volcano names as well as their latitude and
longitude. Next I used a drop down menu to show how many volcanoes are in each
geographic region. Finally, I ended with a pie chart displaying the dominant rock
type percentages of all volcanoes across the world.
"""

import pandas as pd
import numpy as np
import streamlit as st
import csv
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium

csv = pd.read_csv("volcanoes.csv", encoding='latin-1')

st.title("Welcome to my Volcanoes Page!")

# Bar Chart

elevation = csv.iloc[:,10]

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in elevation:
    if i < 500:
        a = a + 1
    elif i < 1000:
        b = b + 1
    elif i < 1500:
        c = c + 1
    elif i < 2000:
        d = d + 1
    elif i < 3000:
        e = e + 1
    else:
        f = f + 1

ele_Y = [a,b,c,d,e,f]
ele_X = ["<500","500:999","1000:1499","1500:1999","2000:2999",">3000"]

st.header("Volcano Elevation Ranges (in meters):")
st.sidebar.title("Color Selector")

colors = {"Red":"r","Green":"g","Yellow":"y","Blue":"b"}
color_names = list(colors.keys())
selected_color = st.sidebar.radio("Color", color_names)

fig,ax = plt.subplots()

ax.bar(ele_X,ele_Y, width=0.75, color = selected_color)
st.pyplot(fig)

st.image("Volcano.jfif", caption="Ojos del Salado, Chile", width=600)

ele_max = str(elevation.max())
ele_min = str(elevation.min())
ele_mean = str(elevation.mean().round())

if st.button("Can you guess how high the volcano at the highest elevation is?"):
    st.subheader("The volcano at the highest elevation is at " + ele_max + " meters")
if st.button("Can you guess how low the volcano at the lowest elevation is?"):
    st.subheader("The volcano at the lowest elevation is at " + ele_min + " meters")
if st.button("Can you guess the average volcano height?"):
    st.subheader("The average volcano height is " + ele_mean + " meters")
if st.button("Click to reset questions"):
    st.subheader("")

# Map (Using Folium)

st.header("Map with Volcano names and last known Eruptions:")

csv.head()

center = [0,0]
map_volcanoes = folium.Map(location=center, zoom_start=1)

for index, volcano in csv.iterrows():
    location = [volcano['Latitude'], volcano['Longitude']]
    folium.Marker(location, popup = f'Name: {volcano["Volcano Name"]}\n\n\n Last Known Eruption: {volcano["Last Known Eruption"]}').add_to(map_volcanoes)

folium_static(map_volcanoes)

# Table with lat, long, and name

name = csv.iloc[:,1]

lat = csv.iloc[:,8]
lat_np = lat.to_numpy()
lat_list = lat_np.tolist()

long = csv.iloc[:,9]
long_np = long.to_numpy()
long_list = long_np.tolist()

zip_iterator = zip(lat_list, long_list)
lat_long_dict = dict(zip_iterator)

dataframes = {"Names":name, "Latitude":lat_list,"Longitude":long_list}
st.dataframe(dataframes)

# Interactive Selectbox

st.header("")

regions_counter = csv['Region'].value_counts()
regioncounts = csv['Region'].value_counts().to_dict()

regions = []
for i in regions_counter:
    regions.append(i)

option = st.selectbox(
    'Select the Region you would like to know the total number of volcanoes for:',
    ['None','South America', 'Japan, Taiwan, Marianas', 'Kamchatka and Mainland Asia', 'Indonesia', 'Africa and Red Sea',
     'Mexico and Central America', 'Alaska', 'Melanesia and Australia', 'Canada and Western USA', 'New Zealand to Fiji',
     'Philippines and SE Asia', 'Middle East and Indian Ocean', 'Kuril Islands', 'Mediterranean and Western Asia',
     'Iceland and Arctic Ocean', 'Hawaii and Pacific Ocean', 'Antarctica', 'Atlantic Ocean', 'West Indies'])

if 'None' in option:
    st.subheader("")
if 'South America' in option:
    st.subheader("There are " + str(regions[0]) + " volcanoes in this region")
if 'Japan, Taiwan, Marianas' in option:
    st.subheader("There are " + str(regions[1]) + " volcanoes in this region")
if 'Kamchatka and Mainland Asia' in option:
    st.subheader("There are " + str(regions[2]) + " volcanoes in this region")
if 'Indonesia' in option:
    st.subheader("There are " + str(regions[3]) + " volcanoes in this region")
if 'Africa and Red Sea' in option:
    st.subheader("There are " + str(regions[4]) + " volcanoes in this region")
if 'Mexico and Central America' in option:
    st.subheader("There are " + str(regions[5]) + " volcanoes in this region")
if 'Alaska' in option:
    st.subheader("There are " + str(regions[6]) + " volcanoes in this region")
if 'Melanesia and Australia' in option:
    st.subheader("There are " + str(regions[7]) + " volcanoes in this region")
if 'Canada and Western USA' in option:
    st.subheader("There are " + str(regions[8]) + " volcanoes in this region")
if 'New Zealand to Fiji' in option:
    st.subheader("There are " + str(regions[9]) + " volcanoes in this region")
if 'Philippines and SE Asia' in option:
    st.subheader("There are " + str(regions[10]) + " volcanoes in this region")
if 'Middle East and Indian Ocean' in option:
    st.subheader("There are " + str(regions[11]) + " volcanoes in this region")
if 'Kuril Islands' in option:
    st.subheader("There are " + str(regions[12]) + " volcanoes in this region")
if 'Mediterranean and Western Asia' in option:
    st.subheader("There are " + str(regions[13]) + " volcanoes in this region")
if 'Iceland and Arctic Ocean' in option:
    st.subheader("There are " + str(regions[14]) + " volcanoes in this region")
if 'Hawaii and Pacific Ocean' in option:
    st.subheader("There are " + str(regions[15]) + " volcanoes in this region")
if 'Antarctica' in option:
    st.subheader("There are " + str(regions[16]) + " volcanoes in this region")
if 'Atlantic Ocean' in option:
    st.subheader("There are " + str(regions[17]) + " volcanoes in this region")
if 'West Indies' in option:
    st.subheader("There are " + str(regions[18]) + " volcanoes in this region")

# Pie Chart

rocks_counter = csv['Dominant Rock Type'].value_counts()
total_rocks = []

for i in rocks_counter:
    total_rocks.append(i)

st.title("Dominant Rock Type Percentages")

labels = 'Andesite / Basaltic Andesite', 'Basalt / Picro-Basalt', 'Dacite', 'Trachybasalt / Tephrite Basanite', 'Rhyolite', 'No Data (checked)', 'Trachyte / Trachydacite', 'Trachyandesite / Basaltic Trachyandesite', 'Foidite', 'Phonolite', 'Phonotephrite / Tephri-phonolite'
sizes = [total_rocks[0], total_rocks[1], total_rocks[2], total_rocks[3], total_rocks[4],total_rocks[5], total_rocks[6], total_rocks[7], total_rocks[8], total_rocks[9], total_rocks[10]]
explode = (0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

st.pyplot(fig1)

st.write("The most common rock type is Andesite / Basaltic Andesite at 40.4%")

# Goodbye

st.subheader('Thank you! Have a great break :sunglasses:')

partytime = st.checkbox("Click for a surprise")

if partytime:
    st.balloons()

