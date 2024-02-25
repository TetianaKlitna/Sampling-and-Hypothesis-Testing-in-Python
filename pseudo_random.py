# Population parameter is a calculation made on the population dataset 
# Point estimate or sampeling statistic is a calculation made on the sample dataset 

import numpy as np

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low = -3, high = 3, size = 5000)
# Print uniforms
print(uniforms)

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc = 5, scale = 2, size = 5000)
# Print normals
print(normals)

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Plot a histogram of uniform values, binwidth 0.25
plt.hist(uniforms, bins = np.arange(-3, 3.25, 0.25))
plt.show()

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Plot a histogram of normal values, binwidth 0.5
plt.hist(normals, bins = np.arange(-2, 13.5, 0.5))
plt.show()