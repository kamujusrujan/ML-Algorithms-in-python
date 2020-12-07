from collections import Counter
import pandas as pd

class ProbabilityModel():

	class Probability():
		def __init__(self,A,B,data):
			self.A, self.B = A,B
			self.data = data
			pass

	def __init__(self, header, data	):
		self.header = header
		self.data = data
		pass

	def initialize_param(self,A,B):
		data = self.data[A] , self.data[B]
		Probability(A,B,data)
		pass


	def conditional_proba(self, target, given):
		pass

	def marginal_proba(self, target):
		pass

	def joint_proba(self, target, given):
		pass



