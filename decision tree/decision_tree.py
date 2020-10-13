class Node: 
	def __init__(self,feature,condition):
		self.feature = feature
		self.condition = condition
		self.right , self.left  = [] , [] 
		pass


class DecisionTree:
	'''
	considering right is true, and left is false
	'''
	def __init__(self):
		self.root = None
		pass

	def train(self,features,labels):
		if len(labels) == 0 : return 
		#find best feature to split
		feature , condition = find_best_feature(features,labels)
		#assign it to the root and split the data
		root = Node(feature,condition)
		right_features,right_labels,left_features,left_labels = split_data(features,labels,feature,condition)
		#train left node
		root.right = self.train(right_features,right_labels)
		#train right node
		root.left = self.train(left_features,left_labels)
		#return new node
		return root

		pass

	def predict(self,point):
		pass



def split_data(features,labels,feature,condition):
	right_features, right_labels = [] , []
	left_features, left_labels = [] , []
	for i in range(len(features)):
		point = features[i]
		if point[feature] != condition:
			left_labels.append(labels[i])
			left_features.append(point)
		else:
			right_labels.append(labels[i])
			right_features.append(point)
	return right_features,right_labels,left_features,left_labels 





def find_best_feature(features,labels):
	N_features = len(features[0])
	best_feature,condition, least_err  = -1 ,None,  float('inf') 
	for i in range(N_features):
		#find best err for that feature
		temp_err, split_condition  = find_best_split(feature ,features,labels)
		if temp_err < least_err : 
			best_feature = i 
			condition = split_condition
			temp_err = least_err
	return (best_feature,condition)
	pass

def find_best_split(feature , features,labels):
	unique_records = set([f[feature] for f in features])
	gini_im , condition = float('inf') , None
	for c in unique_records:
		#finding best condition
		temp_gini = gini_for_split(features,labels,feature,c)
		if temp_gini < gini_im : 
			gini_im = temp_gini
			condition = c
	return (gini_im,condition)
	pass



def gini_calc_node(labels):
	# Sum of probability ^ 2 for all classes
	total = len(labels)
	current_labels = set(labels)
	p = 0 
	for l in current_labels : 
		p += (labels.count(i)/total)**2
	return p 
	pass

def gini_for_split(features,labels,feature,condition):
	# 1 - (gini for left + right)
	root_gini = gini_calc_node(features,labels)
	left_data , right_data = [] , [] 
	for i in range(len(features)):
		point = features[i]
		if point[feature] != condition :
			left_data.append(labels[i])
		else: 
			right_data.append(labels[i])
	right_gini = gini_calc_node(right_data) 
	left_gini = gini_calc_node(left_data) 
	return 1 - (right_gini + left_gini)		

	pass