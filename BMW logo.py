import sys
import matplotlib
matplotlib.use('Agg')



import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
import numpy as np

# Figure setup
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_facecolor('black')

# Outer black ring
outer_circle = Circle((0, 0), 1, facecolor='black',
                      edgecolor='white', linewidth=4)
ax.add_patch(outer_circle)

# Inner circle (for the blue-white quarters)
inner_radius = 0.55
start_angle = 90

# Blue and White quarters
ax.add_patch(Wedge((0, 0), inner_radius, start_angle, start_angle+90,
                   facecolor='#0066B1', edgecolor='white', linewidth=2))
ax.add_patch(Wedge((0, 0), inner_radius, start_angle+90, start_angle+180,
                   facecolor='white', edgecolor='white', linewidth=2))
ax.add_patch(Wedge((0, 0), inner_radius, start_angle+180, start_angle+270,
                   facecolor='#0066B1', edgecolor='white', linewidth=2))
ax.add_patch(Wedge((0, 0), inner_radius, start_angle+270, start_angle+360,
                   facecolor='white', edgecolor='white', linewidth=2))

r = 0.76  

# B, M, W 
angles = [122, 90, 58]  
labels = ['B', 'M', 'W']

for angle, label in zip(angles, labels):
    rad = np.radians(angle)
   
    x = r * np.cos(rad)
    y = r * np.sin(rad)
    
    
    rot = angle - 90
    
    ax.text(x, y, label, fontsize=30, fontweight='bold', color='white',
            ha='center', va='center', rotation=rot)

# Final touches
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
