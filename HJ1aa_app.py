# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:20:38 2024

@author: zzulk
"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load your dataset
data = pd.read_csv(r"C:\Users\zzulk\Downloads\(2) GeoTech_HJ\New Folder\location_data1.csv")

# Adjust the DataFrame index to start from 1 instead of 0
data.index = data.index + 1

# Calculate Cu and Cc
data['Cu'] = data['D60'] / data['D10']
data['Cc'] = (data['D30'] ** 2) / (data['D10'] * data['D60'])

# Handle NaN values resulting from zero division
data['Cu'].replace([float('inf'), -float('inf')], float('nan'), inplace=True)
data['Cc'].replace([float('inf'), -float('inf')], float('nan'), inplace=True)

# Function to classify soil using USCS without Atterberg Limits
def classify_soil(row):
    if row['Gravels (%)'] > 50:
        return 'Gravel (G)'
    elif row['Sand (%)'] > 50:
        if row['Cu'] > 6 and 1 <= row['Cc'] <= 3:
            return 'Well-graded Sand (SW)'
        else:
            return 'Poorly-graded Sand (SP)'
    elif row['Silt (%)'] + row['Clay (%)'] > 50:
        if row['Silt (%)'] > row['Clay (%)']:
            return 'Silt (M)'
        else:
            return 'Clay (C)'
    else:
        return 'Mixed Soil'

# Apply classification function
data['USCS Classification'] = data.apply(classify_soil, axis=1)

# Title and description
st.title("Geotechnical Data Visualization and Classification")
st.write("This app visualizes geotechnical data and classifies soil types based on various parameters.")

# Sidebar filters
st.sidebar.header("Filter Options")
location_filter = st.sidebar.multiselect("Select Location(s)", data['Location'].unique())
classification_filter = st.sidebar.multiselect("Select Soil Classification(s)", data['USCS Classification'].unique())

# Apply filters to data
if location_filter:
    filtered_data = data[data['Location'].isin(location_filter)]
else:
    filtered_data = data

if classification_filter:
    filtered_data = filtered_data[filtered_data['USCS Classification'].isin(classification_filter)]

# Create a folium map centered around Malaysia
m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Add data points to the map with detailed popups
for idx, row in filtered_data.iterrows():
    popup_text = (
        f"Location: {row['Location']}<br>"
        f"Clay (%): {row['Clay (%)']}<br>"
        f"Silt (%): {row['Silt (%)']}<br>"
        f"Sand (%): {row['Sand (%)']}<br>"
        f"Classification: {row['USCS Classification']}"
    )
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_text,
    ).add_to(m)

# Display the map in Streamlit
folium_static(m)

# Display the filtered dataframe
st.write("## Filtered Dataset with USCS Classification")
st.dataframe(filtered_data)
