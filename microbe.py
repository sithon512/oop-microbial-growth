class Microbe:
	"""
	This class represents the microbes that will sit stationary in the grid.
	Microbes are semi-active classes that are acted upon by the grid, but also
	take action themselves when prompted to consume nutrients.
	"""

	def __init__(self):
		"""
		Initialize the class instance. Initialization simply sets instance
		variable `heldNutrient` to None.
		"""

		self.heldNutrient = None

	def hasNutrient(self):
		"""
		Returns whether or not the microbe is holding a nutrient.
		"""

		return self.heldNutrient != None

	def takeNutrient(self, nutrient):
		"""
		Assigns `nutrient` to the `heldNutrient` instance variable.
		"""

		self.heldNutrient = nutrient

	def consumeNutrient(self):
		"""
		Sets held nutrient to None. In `petri.py` this be called during the
		reproduction phase, but the generation of offspring and the placement
		of that offspring is handled by `petri.py`
		"""

		self.heldNutrient = None
