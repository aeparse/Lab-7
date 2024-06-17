import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line,

fig, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

line, = ax.plot(x, y)

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

ani.save('sine_wave_animation.gif', writer=PillowWriter(fps=20))

plt.show()
