class Nutrient:
	"""
	This class represents the nutrients that will transit the grid. Nutrients
	are passive classes that only concern themselves with whether they have
	moved and not any functions of the move or of being consumed.
	"""

	def __init__(self):
		"""
		Initialize the class instance. Initialization simply sets instance
		variable `hasMoved` to false.
		"""

		self.hasMoved = False

	def getMoved(self):
		"""
		Returns the current value of `hasMoved`.
		"""

		return self.hasMoved

	def setMoved(self):
		"""
		Sets the `hasMoved` variable to true.
		"""

		self.hasMoved = True

	def clearMoved(self):
		"""
		Sets the `hasMoved` variable to false.
		"""

		self.hasMoved = False
