
'''
Model working principles:
	1. Acylic graph
	2. Branches denote probabilites between nodes/features
	3.  
'''

import pandas as pd
from utils import Probability
from collections import Counter

class BaysienNetwork():





	class Node():
		def __init__(self,feature,target = [None] ,dataset):
			self.feature = feature
			proba_distributions = Counter(dataset[feature].values.tolist())
			self.values  = list(proba_distributions.keys())
			self.children = self.initialize_children(target, dataset)
			pass 

		def initialize_children(self,target,dataset):
			nodes = []
			for child in target:
				nodes.append(Node(child))
			return nodes 






    def __init__(self):
        pass

ProbabilityModel()


