import pandas as pd
import numpy as np
from datetime import datetime

# Sample Landsat data in dictionary format
landsat_data = {
    "id": "LANDSAT/LC08/C02/T1_L2/LC08_044034_20210321",
    "SR_B1": 0.123,  # Band 1 (coastal/aerosol)
    "SR_B2": 0.456,  # Band 2 (blue)W
    "SR_B3": 0.789,  # Band 3 (green)
    "SR_B4": 0.111,  # Band 4 (red)
    "SR_B5": 0.222,  # Band 5 (NIR)
    "SR_B6": 0.333,  # Band 6 (SWIR 1)
    "SR_B7": 0.444,  # Band 7 (SWIR 2)
    "ST_B10": 300.0, # Surface Temperature
    "version": 1629895794575101,  # Unix timestamp
}

def convert_timestamp(timestamp):
    timestamp=timestamp/1000000
    return datetime.fromtimestamp(timestamp,tz=datetime.now().astimezone().tzinfo)

def calculate_ndvi(sr_b5, sr_b4):
    return (sr_b5 - sr_b4) / (sr_b5 + sr_b4 + 1e-10)  

def calculate_ndwi(sr_b5, sr_b2):
    return (sr_b5 - sr_b2) / (sr_b5 + sr_b2 + 1e-10)

date_taken = convert_timestamp(landsat_data["version"])


ndvi = calculate_ndvi(landsat_data["SR_B5"], landsat_data["SR_B4"])
ndwi = calculate_ndwi(landsat_data["SR_B5"], landsat_data["SR_B2"])

# Create a DataFrame to summarize the analysis
data_summary = pd.DataFrame({
    "Date": [date_taken],
    "NDVI": [ndvi],
    "NDWI": [ndwi],
    "Surface Temperature (K)": [landsat_data["ST_B10"]]
})

# Print the summary of the analysis
print(data_summary)

# Example of adding more temporal data (this could be expanded for more dates)
# For demonstration, let's say we have another set of Landsat data for comparison
landsat_data_2024 = {
    "SR_B4": 0.130,
    "SR_B5": 0.250,
    "version": 1719895794575101,
    "ST_B10": 305.0,
}

# Convert timestamp for the new data
date_taken_2024 = convert_timestamp(landsat_data_2024["version"])

# Calculate NDVI and NDWI for new data
ndvi_2024 = calculate_ndvi(landsat_data_2024["SR_B5"], landsat_data["SR_B4"])  # Using previous Red band
ndwi_2024 = calculate_ndwi(landsat_data_2024["SR_B5"], landsat_data["SR_B2"])  # Using previous Blue band

# Add the new data to the summary
data_summary = data_summary.append({
    "Date": date_taken_2024,
    "NDVI": ndvi_2024,
    "NDWI": ndwi_2024,
    "Surface Temperature (K)": landsat_data_2024["ST_B10"]
}, ignore_index=True)

# Print the updated summary of the analysis
print("\nUpdated Summary with New Temporal Data:")
print(data_summary)