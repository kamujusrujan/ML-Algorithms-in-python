import pandas as pd
from  decision_tree import DecisionTree	
from sklearn.model_selection import train_test_split

df = pd.read_pickle('modified_iris.pkl')
features = []
labels = list(df['class'])
for i in range(len(df)):
  features.append(list(df.loc[i]))


def start():
	X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
	dt = DecisionTree()
	dt.fit(X_train, y_train)
	true = 0
	for i in range(len(X_test)):
		# print(y_test[i])
		true +=1 if dt.predict(X_test[i]) == y_test[i] else 0
	print(true/len(y_test)  )
	# print(dt.to_string())

start()
