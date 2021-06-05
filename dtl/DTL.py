"""
# SOPHIA WANJIKU NJOROGE
# MACHINE_LEARNING_ALGORITHMS
# DECISION_TREE_ALGORITHM
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('loan.csv', sep=',', header=0)

print("\n***************DECISION TREE LEARNING ALGORITHM****************")
print("Dataset Length::", len(data))
print("Dataset Shape::", data.shape)
print("Dataset::")
data.head()

# Separating the target variable
x = data.values[:, 0:4]
y = data.values[:, 5]

# Split dataset into test and train
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

# Function to perform training with entropy
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100,
                                     max_depth=3, min_samples_leaf=5)
clf_entropy.fit(x_train, y_train)


y_pred_en = clf_entropy.predict(x_test)
print(y_pred_en)

# In[11]:


print("Accuracy is", accuracy_score(y_test, y_pred_en) * 100)

# In[ ]:
