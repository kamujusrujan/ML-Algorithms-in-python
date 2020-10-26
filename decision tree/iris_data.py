import pandas as pd
from  decision_tree import DecisionTree	
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_pickle('modified_iris.pkl')
features = []
labels = list(df['class'])
for i in range(len(df)):
  features.append(list(df.loc[i]))


def start():
	X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3)
	print(y_test)
	dt = DecisionTree()
	dt.fit(X_train, y_train)
	true = 0
	for i in range(len(X_test)):
		true +=1 if dt.predict(X_test[i]) == y_test[i] else 0
	return true/len(y_test)


avg = []
try: 
	for i in range(10):
		avg.append(start())
except: 
	print('err')
print(avg,np.mean(avg))
