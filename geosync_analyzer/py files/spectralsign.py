import matplotlib.pyplot as plt

wavelengths = [0.443, 0.483, 0.563, 0.655, 0.865, 1.610, 2.200]

reflectance_max_landsat = [14571, 16904, 17078, 18963, 20885, 20863, 20778]
reflectance_max_simulated = [14000, 16500, 17200, 18500, 20500, 20000, 19800]

plt.figure(figsize=(10, 6), facecolor='#f7f7f7')
plt.plot(wavelengths, reflectance_max_landsat, marker='o', linestyle='-', color='#1f77b4', 
         linewidth=2, markersize=8, markerfacecolor='white', label='Landsat Reflectance')
plt.plot(wavelengths, reflectance_max_simulated, marker='s', linestyle='--', color='#2ca02c', 
         linewidth=2, markersize=8, markerfacecolor='white', label='Simulated Reflectance')

plt.title("Reflectance vs Wavelength", fontsize=16, fontweight='bold')
plt.xlabel("Wavelength (micrometers)", fontsize=13, labelpad=10)
plt.ylabel("Reflectance (Max)", fontsize=13, labelpad=10)

plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)

plt.legend(loc='lower right', fontsize=12, frameon=True, shadow=True, borderpad=1)

plt.gca().set_facecolor('#eaeaf2')


plt.tight_layout()
plt.show()