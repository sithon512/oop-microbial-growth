"""
The classes contained in this module define a petri dish instance.
"""

from microbe import Microbe
from nutrient import Nutrient

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
		take place during initialization and the reproduction stage of the
		simulation.
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
			if not nutrient.getMoved()]

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

class PetriDish:
	"""
	This class defines the dish grid in which `PetriCell` instances sit.
	"""

	def __init__(self, x, y, concentration, microbes):
		"""
		Initialize the class instance. Create the grid as a 2D list, place
		PetriCell instances in each index, then begin assigning nutrients to
		PetriCells based on concentration. Finally, place microbes according
		to the locations described in the list of tuples passed as the
		`microbes` argument.
		"""

		# define base grid
		self.grid = [[None for j in range(y)] for i in range(x)]
		# record x and y for easy reference later
		self.x = x
		self.y = y

		# populate grid with lists of PetriCells
		for i in range(x):
			# self.grid[i] = []
			for j in range(y):
				self.grid[i][j] = PetriCell()

		# import random for nutrient placement
		from random import randint
		# calculate number of nutrients
		nutrients_to_place = int(concentration * x * y)
		# place nutrients, may overlap
		for i in range(nutrients_to_place):
			place_x = randint(0, x-1)
			place_y = randint(0, y-1)
			self.grid[place_x][place_y].placeNutrient(Nutrient())

		# place microbes
		for coordx, coordy in microbes:
			# note: ignores duplicate coords
			self.grid[coordx][coordy].createMicrobe()

	def __str__(self):
		"""
		Prints the grid of cells.
		"""

		output = ''

		# x should iterate within y to create rows
		for j in range(self.y):
			row = ''
			for i in range(self.x):
				row += f'{self.grid[i][j]} '
			row = f'{row.strip()}\n'
			output += row

		return output

	def moveNutrients(self):
		"""
		Iterate through each cell in grid, moving nutrients that have not
		moved yet.
		"""

		from random import randint

		def coord_in_bounds(x, y):
			"""
			Checks if a position is on the grid or out of bounds.
			"""

			# if one of these conditions is true, then coord is not in bounds
			return not (x < 0 or y < 0 or x > self.x - 1 or y > self.y - 1)

		for i in range(self.x):
			for j in range(self.y):
				for nutrient in self.grid[i][j].getUnmoved():
					shiftx = randint(-1, 1)
					shifty = randint(-1, 1)
					# if the coord was invalid, re-roll it
					while not coord_in_bounds(i + shiftx, j + shifty):
						shiftx = randint(-1, 1)
						shifty = randint(-1, 1)

					# place nutrient into the selected adjacent cell
					self.grid[i+shiftx][j+shifty].placeNutrient(nutrient)
					# mark the nutrient as having moved
					nutrient.setMoved()

	def checkMicrobes(self):
		"""
		For each microbe, check if it has a nutrient or has a nutrient in its
		cell. If a nutrient is found, consume it. Records the position of the
		offspring, then moves on to the next microbe. Once all microbes have
		had a chance to try reproduction, the new microbes are placed onto the
		grid.
		"""

		return

	def step(self, iterations):
		"""
		Run through a number of iterations where one iteration is a call to
		`moveNutrients` followed by a call to `checkMicrobes`.
		"""

		return
