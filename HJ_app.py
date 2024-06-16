# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:02:27 2024

@author: zzulk
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your datasets
field_lab_mc_2_data = pd.read_csv(r"C:\Users\zzulk\Downloads\(2) GeoTech_HJ\New Folder\Field vs Lab vs MC (2).csv")
cc_cu_d10_d30_d60_data = pd.read_csv(r"C:\Users\zzulk\Downloads\(2) GeoTech_HJ\New Folder\Cc, Cu, D10,D30,D60.csv")

# Title and description
st.title("Geotechnical Data Visualization")
st.write("This app visualizes the geotechnical data and correlations between various soil properties.")

# Select dataset to visualize
dataset = st.selectbox("Select Dataset", ["Field vs Lab vs MC (2)", "Cc, Cu, D10,D30,D60"])

# Display dataset
if dataset == "Field vs Lab vs MC (2)":
    data = field_lab_mc_2_data
else:
    data = cc_cu_d10_d30_d60_data

st.write("### Dataset")
st.write(data)

# Plotting
st.write("### Scatter Plot")
x_axis = st.selectbox("X-Axis", data.columns)
y_axis = st.selectbox("Y-Axis", data.columns)

fig, ax = plt.subplots()
sns.regplot(data=data, x=x_axis, y=y_axis, ax=ax)
st.pyplot(fig)
