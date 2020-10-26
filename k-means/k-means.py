from collections import defaultdict
import numpy as np
import math

class K_Means():
	def __init__(self, k ):
		self.k = k 
		self.centroid = {}
		pass

	def __random_assignment(self,dataset):
		# rand_centroid_index = numpy.random.randint(len(dataset), size = k)
		rand_centroids = numpy.random.choice(dataset,k)
		for cent in rand_centroids:
			cent = str(cent)
			self.centroid[cent] = []
		pass

	def fit(self,dataset):
		self.__random_assignment(dataset)
		for point in dataset:
			nearest_cent , distance = find_nearest_centroid(point)
			self.centroid[str(nearest_cent)].append(point)
			self.recalculate_centroids(nearest_cent)
		pass

	def recalculate_centroids(self,centroid):
		centroid = str(centroid)
		new_centroid = np.mean(self.centroid[centroid])
		self.centroid[str(new_centroid)] = self.centroid.pop(centroid)
		pass

	def find_nearest_centroid(self,point):
		min_centroid, min_distance = None , float('inf')
		for cent in self.centroid.keys():
			cent = eval(cent)
			distance_cent = eucledian_distance(cent,point)
			if distance_cent < min_distance :
				min_centroid = cent
				min_distance  =distance_cent
		return (min_centroid , min_distance)







def eucledian_distance(pointA,pointB):
	dist = 0
	dim = len(pointA) 
	for i in range(dim):
		dist += math.pow(pointA[i] - pointB[i],2)
	return math.sqrt(dist)