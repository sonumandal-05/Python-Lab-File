# Write a Python program to:
# a)	Plot sine and cosine curves
# b)	Plot histogram of given data


import numpy as np
import matplotlib.pyplot as plt
# a) Plot sine and cosine curves
x = np.linspace(0, 2 * np.pi, 100)  
sine_curve = np.sin(x)
cosine_curve = np.cos(x)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, sine_curve, label='Sine Curve', color='blue')
plt.plot(x, cosine_curve, label='Cosine Curve', color='orange')
plt.title('Sine and Cosine Curves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# b) Plot histogram of given data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.subplot(1, 2, 2)
plt.hist(data, bins=np.arange(0.5, 5.5, 1), color='green', edgecolor='black')
plt.title('Histogram of Given Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()