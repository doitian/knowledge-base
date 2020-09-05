import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 2, 100)

base = 1

y = [base if i < 1 else base * (1 - (i - 1) * (i - 1)) for i in x]

# Plot the data
fig = plt.figure()
ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
ax.set_xlabel('block weight / cumulative_weights_median')
ax.set_ylabel('block reward / base reward')

ax.axhline(y=1, color="grey", linestyle="--")
ax.axvline(x=1, color="grey", linestyle="--")
ax.axvline(x=2, color="grey", linestyle="--")

ax.plot(x, y, label='block reward')

# Add a legend
plt.legend()

# Show the plot
plt.show()
