# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:09:39 2024

@author: zzulk
"""

import pandas as pd

# Load your dataset
data = pd.read_csv(r"C:\Users\zzulk\Downloads\(2) GeoTech_HJ\New Folder\location_data1.csv")

# Display the first few rows and columns of the dataset
print(data.head())
print(data.columns)

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

# Display the DataFrame with classification
print(data[['Location', 'Gravels (%)', 'Sand (%)', 'Silt (%)', 'Clay (%)', 'Cu', 'Cc', 'USCS Classification']])

# Save the classified data to a new CSV file
data.to_csv(r"C:\Users\zzulk\Downloads\(2) GeoTech_HJ\New Folder\classified_location_data1.csv", index=False)
