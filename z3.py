import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 100)
y = np.linspace(-0.5, 0.5, 100)

X, Y = np.meshgrid(x, y)

Z = np.tan(X + Y)

Z[Z > 10] = np.nan
Z[Z < -10] = np.nan

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_zlim(-10, 10)

ax.set_title('z = tg(x + y)')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')

plt.show()
