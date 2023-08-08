import numpy as np

time = np.array([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
temperature = np.array([70.7, 72.58, 73.96, 75.0, 75.8, 76.42, 76.92, 77.33, 77.69, 78.0, 78.28, 78.54, 78.79, 79.02, 79.25, 79.47, 79.69, 79.91, 80.12, 80.34, 80.55, 80.76, 80.97, 81.18])

# Adjust temperatures that are below 70.7°C to be 70.7°C
temperature = np.where(temperature < 70.7, 70.7, temperature)

# Calculate the integral using the trapezoidal rule
integral = np.trapz(temperature - 70.7, time)

print(f"The integral value is: {integral}")
