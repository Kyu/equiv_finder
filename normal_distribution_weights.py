import numpy as np
from scipy.stats import norm

# Set mean and standard deviation
mu = 0
sigma = 1

# Generate 100 numbers in a normal distribution
numbers = np.linspace(-3, 3, 100)

# Calculate the PDF for each number
pdf_values = norm.pdf(numbers, mu, sigma)

# Normalize the probabilities to get weights
weights = pdf_values / pdf_values.sum()

# Create a table with numbers and weights
weight_table = list(zip(numbers, weights))

print(weight_table)
# Display the weight table
print("Number\tWeight")
for number, weight in weight_table:
    print(f"{number:.3f}\t{weight:.5f}")

print(list(weights))
print(len(weights))
