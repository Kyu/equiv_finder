import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Set degrees of freedom (controls tail heaviness, larger values = heavier tails)
df = 3

# Generate 100 numbers in a t-distribution
numbers = np.linspace(-3, 3, 100)

# Calculate the PDF for each number
pdf_values = t.pdf(numbers, df)

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
plt.plot(numbers, pdf_values, label=f't-distribution (df={df})')
plt.title('Probability Density Function of t-Distribution')
plt.xlabel('Number')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
