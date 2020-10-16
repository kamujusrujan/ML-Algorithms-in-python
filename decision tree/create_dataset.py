from  decision_tree import DecisionTree	

features = [
		[0,0,0],
		[0,0,1],
		[0,1,0],
		[0,1,1],
		[1,0,0],
		[1,0,1],
		[1,1,0],
		[1,1,1]	
	]
labels = [1,1,0,1,0,0,0,1]

dt = DecisionTree()
dt.fit(features,labels)
print(features)
for i in range(len(features)):
	print(dt.predict(features[i]) == labels[i])
	