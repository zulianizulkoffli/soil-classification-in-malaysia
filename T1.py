# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:50:27 2024

@author: zzulk
"""

import streamlit as st
import pandas as pd

# Load your dataset
data = pd.read_csv(r"C:\Users\zzulk\Downloads\(2) GeoTech_HJ\New Folder\location_data1.csv")  # Update this path to your actual data file path

# Display the first few rows and the column names to understand the data structure
st.write(data.head())
st.write(data.columns.tolist())
