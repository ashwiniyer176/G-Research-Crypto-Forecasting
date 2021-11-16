from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
metric = metrics.accuracy_score
test_size = 0.3
