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

	def fit(self,features,labels):
		self.root = self.__train(features,labels,0)

	def __train(self,features,labels,depth):
		#find best feature to split
		if len(features) == 0 : return
		if features[0].count(None) == len(features[0]) : return 
		feature , condition = find_best_feature(features,labels)
		#assign it to the root and split the data
		root = Node(feature,condition)
		right_features,right_labels,left_features,left_labels = split_data(features,labels,feature,condition)
		# print('s',right_features,right_labels,left_features,left_labels, 'b', feature ,'d' ,depth)
		#train left node
		root.right = self.__train(right_features,right_labels,depth + 1)
		#train right node
		root.left = self.__train(left_features,left_labels,depth + 1)
		#return new node
		return root
		pass


	def predict(self,point):
			
		pass

	def to_string(self): 
		temp_root = self.root
		queue = [] 
		queue.append(temp_root)
		tree_rep = ""
		while len(queue) > 0 : 
			size  =  len(queue)
			s =  ""
			for i in range(size) : 
				node = queue.pop(0)	
				s += str(node.feature) + " "
				if node.right != None : queue.append(node.right)
				if node.left != None : queue.append(node.left)
			tree_rep += s + '\n'
		return tree_rep
		pass


def split_data(features,labels,feature,condition):
	right_features, right_labels = [] , []
	left_features, left_labels = [] , []
	for i in range(len(features)):
		point = features[i]
		if point[feature] != condition:
			left_labels.append(labels[i])
			point[feature] = None
			left_features.append(point)
		else:
			right_labels.append(labels[i])
			point[feature] = None
			right_features.append(point)
	return right_features,right_labels,left_features,left_labels 





def find_best_feature(features,labels):
	N_features = len(features[0])
	best_feature,condition, least_err  = -1 ,None,  float('inf') 
	for i in range(N_features):
		#find best err for that feature
		if features[0][i] is None : continue
		temp_err, split_condition  = find_best_split(i ,features,labels)
		if temp_err < least_err : 
			best_feature = i 
			condition = split_condition
			temp_err = least_err
	return (best_feature,condition)
	pass





def find_best_split(feature , features,labels):
	unique_records = set([f[feature] for f in features])
	gini_im , condition = float('-inf') , None
	for c in unique_records:
		if c is None : continue
		#finding best condition
		temp_gini = abs(gini_for_split(features,labels,feature,c))
		if temp_gini > gini_im : 
			gini_im = temp_gini
			condition = c
	return (gini_im,condition)
	pass



def gini_calc_node(labels):
	# Sum of probability ^ 2 for all classes
	# print(labels)
	total = len(labels)
	current_labels = set(labels)
	p = 0 
	for i in current_labels : 
		p += (labels.count(i)/total)**2
	return p 
	pass





def gini_for_split(features,labels,feature,condition):
	# 1 - (gini for left + right)
	root_gini = gini_calc_node(labels)
	left_data , right_data = [] , [] 
	for i in range(len(features)):
		point = features[i]
		if point[feature] != condition :
			left_data.append(labels[i])
		else: 
			right_data.append(labels[i])
	right_gini = gini_calc_node(right_data) 
	left_gini = gini_calc_node(left_data)
	# print(right_gini , left_gini ,right_data, left_data , labels  ,features) 
	return 1 - (right_gini + left_gini)		

	pass



