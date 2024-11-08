

import matplotlib.pyplot as plt
import pandas as pd
import mplcursors

# Sample spatial data for surface reflectance (SR) and temperature for multiple locations
spatial_data = {
    "Date": ["2023-01-01", "2023-02-01", "2023-03-01"],
    "Location_A_SR_Band_1": [0.1, 0.15, 0.2],
    "Location_A_SR_Band_2": [0.2, 0.25, 0.3],
    "Location_A_SR_Band_3": [0.3, 0.35, 0.4],
    "Location_A_SR_Band_4": [0.4, 0.45, 0.5],
    "Location_A_SR_Band_5": [0.5, 0.55, 0.6],
    "Location_B_SR_Band_1": [0.2, 0.25, 0.3],
    "Location_B_SR_Band_2": [0.3, 0.35, 0.4],
    "Location_B_SR_Band_3": [0.4, 0.45, 0.5],
    "Location_B_SR_Band_4": [0.5, 0.55, 0.6],
    "Location_B_SR_Band_5": [0.6, 0.65, 0.7],
    "Location_C_SR_Band_1": [0.15, 0.2, 0.25],
    "Location_C_SR_Band_2": [0.25, 0.3, 0.35],
    "Location_C_SR_Band_3": [0.35, 0.4, 0.45],
    "Location_C_SR_Band_4": [0.45, 0.5, 0.55],
    "Location_C_SR_Band_5": [0.55, 0.6, 0.65],
}

# Creating a DataFrame from the sample spatial data
sr_df = pd.DataFrame(spatial_data)
sr_df["Date"] = pd.to_datetime(sr_df["Date"])

# Function to calculate albedo for each location
def calculate_albedo(location_prefix):
    sr_bands = [f"{location_prefix}SR_Band{i}" for i in range(1, 6)]
    total_reflectance = sr_df[sr_bands].sum(axis=1)
    albedo = total_reflectance / len(sr_bands)  # No scaling factor
    return albedo

# Calculate Albedo for each location
sr_df["Location_A_Albedo"] = calculate_albedo("Location_A")
sr_df["Location_B_Albedo"] = calculate_albedo("Location_B")
sr_df["Location_C_Albedo"] = calculate_albedo("Location_C")

# Plotting the Albedo for each location
plt.figure(figsize=(12, 6), facecolor='#f7f7f7')

# Plot each location's Albedo
line_a, = plt.plot(sr_df["Date"], sr_df["Location_A_Albedo"], marker='o', linestyle='-', color='blue', 
                   linewidth=2, markersize=8, label='Location A')

line_b, = plt.plot(sr_df["Date"], sr_df["Location_B_Albedo"], marker='o', linestyle='-', color='orange', 
                   linewidth=2, markersize=8, label='Location B')

line_c, = plt.plot(sr_df["Date"], sr_df["Location_C_Albedo"], marker='o', linestyle='-', color='green', 
                   linewidth=2, markersize=8, label='Location C')

# Adding title and labels
plt.title('Spatial Comparison of Albedo Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=13, labelpad=10)
plt.ylabel('Albedo', fontsize=13, labelpad=10)
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)
plt.legend(loc='lower right', fontsize=12, frameon=True, shadow=True, borderpad=1)
plt.gca().set_facecolor('#eaeaf2')

# Adding interactive hover functionality with mplcursors
mplcursors.cursor([line_a, line_b, line_c], hover=True).connect("add", 
    lambda sel: sel.annotation.set_text(f'{sel.target[0]} Albedo: {sel.target[1]:.3f}'))

# Final adjustments and showing the plot
plt.tight_layout()
plt.show()