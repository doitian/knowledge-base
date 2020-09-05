import math
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(500, 1000, 100)

def y_generator(x):
    if x <= 50:
        return 1000
    if x <= 250:
        return 500 * math.pow(2, ((x + 49) // 50))
    if x <= 400:
        return 25000
    elif x <= 450:
        return 1600
    else:
        return 300

y = [y_generator(i - 500) for i in x]

# Plot the data
fig = plt.figure()
ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
ax.set_xlabel('block height')
ax.set_ylabel('kB')

ax.axhline(y=300, color="grey", linestyle=":")
ax.axhline(y=25000, color="green", linestyle="--", label="50 * effective_longterm_median")
ax.set_yticks([300, 2000, 4000, 8000, 16000, 25000])

ax.plot(x, y, label='cumulative_weights_median')

# Add a legend
plt.legend()

# Show the plot
plt.show()
