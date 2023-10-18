# importing libraries 
import matplotlib.pyplot as plt 
import numpy as np 
import statistics
from scipy.stats import expon
from scipy.stats import erlang

x = (1,2,4,7)
y = (0.15,0.35,0.6,1.0)

#Answer to question 2 part c
print("here is the mean for the CDF question 2")
mean = sum(x * p for x, p in zip(x, y))
print(mean)
variance = sum(((x - mean) ** 2) * p for x, p in zip(x, y))
print("here is the stdd for the CDF question 2")
std_deviation = np.sqrt(variance)
print(std_deviation)

Hx = (2,5,17,50)
Hy = (0.15,0.2,0.25,0.4)

mean = sum(x * p for x, p in zip(Hx, Hy))
print("here is the mean for the CDF question 3")
print(mean)

variance = sum(((x - mean) ** 2) * p for x, p in zip(Hx, Hy))
print("here is the var for the CDF question 3 part C")
print(variance)

#plt.stem(1,statistics.stdev(y))
#plt.show()

cdf_values = np.cumsum(y)
plt.title('CDF')
plt.stairs(x, np.insert(cdf_values, 0, 0), baseline=0, fill=False, orientation='mid') 
#plt.show()

total_data_points = sum(y)
pmf = {x[i]: y[i] / total_data_points for i in range(len(x))}
# Plot PMF

pmf_x = list(pmf.keys())
pmf_y = list(pmf.values())
plt.stem(pmf_x, pmf_y, use_line_collection = True) 
#plt.show()


# Create the plot for question 4a
# Define the range of values for z
z = np.linspace(0, 20, 100)  # Adjust the range and resolution as needed
# Define the function f(z)
f_z = (1/3) * np.exp(-z/3)
plt.figure(figsize=(8, 6))
plt.plot(z, f_z, label=r'$f(z) = \frac{1}{3}e^{-\frac{z}{3}}$', color='blue', linewidth=2)
plt.xlabel('z')
plt.ylabel('f(z)')
plt.title('Create the plot for question 4a | Plot of $f(z) = \\frac{1}{3}e^{-\\frac{z}{3}}$ ')
plt.grid(True)
plt.legend()
plt.show()

# Define the range of values for z with wider bounds
a = 3 - 3 * np.sqrt(3)
b = 3 + 3 * np.sqrt(3)
z = np.linspace(a, b, 1000)

# Define the PDF function f(z)
f_z = 1 / (6 * np.sqrt(3))

# Create the plot for question 4b
plt.figure(figsize=(8, 6))
plt.plot(z, [f_z] * len(z), label=r'$f(z) = \frac{1}{6\sqrt{3}}$', color='blue', linewidth=2)
plt.xlabel('z')
plt.ylabel('f(z)')
plt.title(r'Create the plot for question 4b | Plot of $f(z) = \frac{1}{6\sqrt{3}}$ for $3 - 3\sqrt{3} < z < 3 + 3\sqrt{3}$')
plt.grid(True)
plt.legend()
plt.xlim(-10, 10)  # Set the wider x-axis limits
plt.ylim(0, 0.2)  # Adjust the y-axis limits as needed
plt.show()

#create the plot for question 4c
# Parameters for the Erlang distribution
k = 3  # Shape parameter
lambda_ = 1  # Rate parameter

# Define the range of values for z
z = np.linspace(0, 10, 1000)  # Adjust the range and resolution as needed

# Calculate the PDF using scipy.stats.erlang
pdf = erlang.pdf(z, k, scale=1/lambda_)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(z, pdf, label=f'Erlang PDF (k={k}, lambda={lambda_})', color='blue', linewidth=2)
plt.xlabel('z')
plt.ylabel('f(z)')
plt.title(f'Question 4c | Erlang Distribution PDF (k={k}, lambda={lambda_})')
plt.grid(True)
plt.legend()
plt.show()

