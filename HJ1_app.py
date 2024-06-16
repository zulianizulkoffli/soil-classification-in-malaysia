# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:28:32 2024

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

# Title and description
st.title("Geotechnical Data Visualization on Malaysia Map")
st.write("This app visualizes geotechnical data collected from various locations in Malaysia.")

# Column names
location_col = 'Location'
latitude_col = 'Latitude'
longitude_col = 'Longitude'

# Additional columns for detailed information
clay_col = 'Clay (%)'
silt_col = 'Silt (%)'
sand_col = 'Sand (%)'
resistivity_col = data.columns[13]  # Use the exact column name if necessary

# Filter options
st.sidebar.header("Filter Options")
clay_filter = st.sidebar.slider("Clay (%)", float(data[clay_col].min()), float(data[clay_col].max()), (float(data[clay_col].min()), float(data[clay_col].max())))
silt_filter = st.sidebar.slider("Silt (%)", float(data[silt_col].min()), float(data[silt_col].max()), (float(data[silt_col].min()), float(data[silt_col].max())))
sand_filter = st.sidebar.slider("Sand (%)", float(data[sand_col].min()), float(data[sand_col].max()), (float(data[sand_col].min()), float(data[sand_col].max())))

# Apply filters to data
filtered_data = data[
    (data[clay_col] >= clay_filter[0]) & (data[clay_col] <= clay_filter[1]) &
    (data[silt_col] >= silt_filter[0]) & (data[silt_col] <= silt_filter[1]) &
    (data[sand_col] >= sand_filter[0]) & (data[sand_col] <= sand_filter[1])
]

# Create a folium map centered around Malaysia
m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Add data points to the map with detailed popups
for idx, row in filtered_data.iterrows():
    popup_text = (
        f"Location: {row[location_col]}<br>"
        f"Clay (%): {row[clay_col]}<br>"
        f"Silt (%): {row[silt_col]}<br>"
        f"Sand (%): {row[sand_col]}<br>"
        f"Resistivity: {row[resistivity_col]}"
    )
    folium.Marker(
        location=[row[latitude_col], row[longitude_col]],
        popup=popup_text,
    ).add_to(m)

# Display the map in Streamlit
folium_static(m)

# Display the entire dataframe at the bottom
st.write("## Full Dataset")
st.dataframe(data)
