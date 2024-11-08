import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO

# Sample data for demonstration
data = {
    "Date": pd.date_range(start="2021-01-01", periods=10, freq='ME'),
    "Total_Reflectance": [0.1, 0.15, 0.2, 0.18, 0.22, 0.25, 0.3, 0.28, 0.35, 0.4]
}
sr_df = pd.DataFrame(data)
sr_bands = ["SR_B1", "SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B6", "SR_B7"]

# Calculate Albedo
sr_df["Albedo"] = sr_df["Total_Reflectance"] / len(sr_bands)

plt.figure(figsize=(10, 5), facecolor='#f7f7f7')
line, = plt.plot(sr_df["Date"], sr_df["Albedo"], marker='o', linestyle='-', color='green', 
                 linewidth=2, markersize=8, markerfacecolor='white', label='Albedo')

plt.title('Albedo Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=13, labelpad=10)
plt.ylabel('Albedo', fontsize=13, labelpad=10)
plt.xticks(rotation=45) 
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)
plt.legend(loc='lower right', fontsize=12, frameon=True, shadow=True, borderpad=1)
plt.gca().set_facecolor('#eaeaf2')

plt.tight_layout()

# Save the plot to a BytesIO object
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)

# Encode the image to base64
img_str = base64.b64encode(buffer.read()).decode('utf-8')
print(img_str, end='')  # Ensure no additional characters are printed

# Optionally, close the plot to free up memory
plt.close()