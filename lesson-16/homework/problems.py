import numpy as np
# Task 1
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temperatures_f = np.array([32, 68, 100, 212, 77])
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
temperatures_c = vectorized_conversion(temperatures_f)

print("Temperatures in Celsius:", temperatures_c)

# Task 2
def power(base, exponent):
    return base ** exponent

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

vectorized_power = np.vectorize(power)
results = vectorized_power(bases, exponents)

print("Power results:", results)

# Task 3

A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

solution = np.linalg.solve(A, b)
print("Solution for (x, y, z):", solution)

# Task 4

A_circuit = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b_circuit = np.array([12, -5, 15])

currents = np.linalg.solve(A_circuit, b_circuit)
print("Currents (I1, I2, I3):", currents)