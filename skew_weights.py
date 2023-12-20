import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Set parameters for the skew-normal distribution
a = 1  # skewness parameter
loc = -3.5  # mean
scale = 1.5  # standard deviation

# Generate 100 numbers in a skew-normal distribution
numbers = np.linspace(-3, 3, 100)

# Calculate the PDF for each number
pdf_values = skewnorm.pdf(numbers, a, loc, scale)

# Normalize the probabilities to get weights
weights = pdf_values / pdf_values.sum()

# Create a table with numbers and weights
weight_table = list(zip(numbers, weights))

# Display the weight table
print("Number\tWeight")
for number, weight in weight_table:
    print(f"{number:.3f}\t{weight:.5f}")

print(list(weights))

# Create a plot
plt.plot(numbers, pdf_values, label=f'Skew-normal distribution (a={a})')
plt.title('Probability Density Function of Skew-normal Distribution')
plt.xlabel('Number')
plt.ylabel('Probability Density')
plt.legend()
plt.show()