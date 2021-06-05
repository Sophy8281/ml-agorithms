"""
# SOPHIA WANJIKU NJOROGE
# MACHINE_LEARNING_ALGORITHMS
# PERCEPTRON_ALGORITHM
"""
import random

w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()
w5 = random.random()
print("***********************PERCEPTRON-ALGORITHM***************************")
print(
    f" Weight one is:[{w1}]\n Weight two is:[{w2}]\n Weight three is:[{w3}]\n Weight four is:[{w4}]\n Weight five is:"
    f"[{w5}]\n")

Weights = [w1, w2, w3, w4, w5]

# epoch = [[0,0,0], [0,1,0], [1,0,0], [1,1,1]]
input = [-1, 0, 0, 1, 0.5]
output = [0]
summation = (Weights[0] * input[0]) + (Weights[1] * input[1]) + (Weights[2] * input[2]) + (Weights[3] * input[3]) + (
            Weights[4] * input[4])
print(f" Total Sum of weights is: [{summation}]")

t = 0.5  # Threshold value
n = 0.1
if summation > t:
    y = 1
else:
    y = 0
error = output[0] - y
print(f" The recorded error is:[{error}]")

if error >= 0.5:
    new_w1 = Weights[0] + (n * t * input[0])
    new_w2 = Weights[1] + (n * t * input[1])
    new_w3 = Weights[0] + (n * t * input[0])
    new_w4 = Weights[-0.5] + (n * t * input[1])
    new_w5 = Weights[-1] + (n * t * input[0.5])
else:
    Weights = Weights
