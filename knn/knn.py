"""
# SOPHIA WANJIKU NJOROGE
# MACHINE_LEARNING_ALGORITHMS
# K-NEAREST NEIGHBOURS ALGORITHM
"""
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')  # used to display the grid
plt.xkcd()  # look like hand drawn

dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
new_features = [5, 7]

[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]

plt.title('K-NN')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
