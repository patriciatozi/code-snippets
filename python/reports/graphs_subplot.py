import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0.01, 10.01, 0.01)
y = 2 ** x

# Generate image for subplot graphs: lines -> 2, columns -> 1	
fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)
ax1.loglog(y, x, 'r')
ax2.loglog(x, y, 'b')

# Separate subplot titles
ax1.set_title('ax1.title')
ax2.set_title('ax2.title')

# Axis labels
ax1.set_ylabel('ax1.ylabel')
ax1.set_xlabel('time')

ax2.set_ylabel('ax2.ylabel')
ax2.set_xlabel('time')

plt.show()