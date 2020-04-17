"""
The classes contained in this module define a petri dish instance.
"""

from microbe import Microbe

class PetriCell:
	"""
	This class defines a cell in the grid that makes up the petri dish. Cells
	are acrive classes that handle the interaction between nutrients and
	microbes.
	"""

	def __init__(self):
		"""
		Initialize the class instance. Initialization simply sets the instance
		variables to None and [].
		"""

		self.microbe = None
		self.nutrients = []

	def __str__(self):
		"""
		String representation takes the form "M#N" where 'M' is only present
		if a microbe is present, otherwise it is replaced by '_', and '#' is
		replaced by the number of nutrients in the cell.
		"""
		
		if self.hasMicrobe():
			return f'M{len(self.nutrients)}N'
		else:
			return f'_{len(self.nutrients)}N'

	def getMicrobe(self):
		"""
		Returns the value of the microbe attribute.
		"""

		return self.microbe

	def hasMicrobe(self):
		"""
		Returns whether or not the cell has a microbe sitting in it.
		"""

		return self.microbe != None

	def createMicrobe(self):
		"""
		Creates a new microbe instance and places it in the cell. This should
		take place during the reproduction stage of the simulation.
		"""

		self.microbe = Microbe()

	def hasNutrients(self):
		"""
		Returns true if the nutrients instance variable has any nutrients and
		false otherwise.
		"""

		return len(self.nutrients) != 0

	def getNutrient(self):
		"""
		Removes a nutrient from the list of nutrients and returns it. Returns
		None if there are no nutrients.
		"""

		if not self.hasNutrients():
			return None
		else:
			# chose to use queue style arbitrarily, LIFO would have worked fine
			return self.nutrients.pop(0)

	def getUnmoved(self):
		"""
		Removes all nutrients from the cell that have not moved and returns
		them in a list.
		"""

		# get list of unmoved nutrients
		unmoveds = [nutrient for nutrient in self.nutrients
			if not nutrient.hasMoved()]

		# remove unmoved nutrients from nutrients instance variable
		self.nutrients = [nutrient for nutrient in self.nutrients
			if nutrient not in unmoveds]

		# return the list of unmoveds
		return unmoveds

	def clearAllMoved(self):
		"""
		Calls the `clearMoved` method on each nutrient contained in
		`nutrients`.
		"""

		for nutrient in self.nutrients:
			nutrient.clearMoved()

	def placeNutrient(self, nutrient):
		"""
		Adds the given `nutrient` to the list of nutrients in the cell.
		"""

		self.nutrients.append(nutrient)
