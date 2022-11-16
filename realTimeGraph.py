import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import pandas as pd
import random

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = []
y = []

def animate(i, x, y):
    x.append(datetime.datetime.now())
    y.append(random.randint(0, 10))
    if len(x) > 20:
        x = x[-20:]
        y = y[-20:]
    ax.clear()
    ax.plot(x, y)
    plt.subplots_adjust(bottom=0.30)

ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=100)

plt.show()