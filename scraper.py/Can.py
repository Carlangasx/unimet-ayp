import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
R0 = 3.3  # Nominal radius (cm)
delta_R = 0.2  # Waist depth (cm)
H = 12.3  # Height of cylindrical region (cm)
h = 1.0  # Height of hemispherical ends (cm)

# Create a grid of (x, y, z) points
z = np.linspace(-h, H + h, 500)  # z-axis range
theta = np.linspace(0, 2 * np.pi, 100)  # Angular range
z, theta = np.meshgrid(z, theta)

# Radius function
r = np.zeros_like(z)
r[(z >= 0) & (z <= H)] = R0 - delta_R * (0.5 + 0.5 * np.cos(2 * np.pi * z[(z >= 0) & (z <= H)] / H))  # Waist region
r[z > H] = np.sqrt(R0**2 - (z[z > H] - H)**2)  # Top hemisphere
r[z < 0] = np.sqrt(R0**2 - z[z < 0]**2)  # Base hemisphere

# Convert to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='red', alpha=0.8, edgecolor='none')

# Set axis labels and limits
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Z (cm)')
ax.set_xlim([-R0, R0])
ax.set_ylim([-R0, R0])
ax.set_zlim([-h, H + h])

# Set aspect ratio
ax.set_box_aspect([1, 1, 2])  # Adjust for better visualization

# Show the plot
plt.title("3D Model of a Coca-Cola Can")
plt.show()