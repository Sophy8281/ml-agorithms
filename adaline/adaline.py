"""
# SOPHIA WANJIKU NJOROGE
# MACHINE_LEARNING_ALGORITHMS
# ADALINE_ALGORITHM
"""

import random

w1 = random.random()
w2 = random.random()
w3 = random.random()
print("*********************ADALINE_ALGORITHM_OUTPUT******************")
print(f"Weight one: {w1}\nWeight two: {w2}\nweight three: {w3}")

Weights = [w1, w2, w3]

input = [-1, 0.5, -0.5]
output = [0]
summation = (Weights[0] * input[0]) + (Weights[1] * input[1]) + (Weights[2] * input[2])
print(f"Total Sum of weights: {summation}")

n = 0.1
t = 0.1

error = output[0] - summation
error_squared = error * error
print(f"The error: {error}")

if error >= 1:
    new_w1 = Weights[0] + (n * t * input[0])
    new_w2 = Weights[1] + (n * t * input[1])
    new_w3 = Weights[0] + (n * t * input[0])
else:
    Weights = Weights
