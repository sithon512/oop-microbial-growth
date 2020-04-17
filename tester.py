"""
This module acts as a tester for the classes designed in this project. Here
the classes can be referenced and used in isolation to ensure that they are
working properly.
"""

from pprint import pprint

def test_nutrient():
	"""
	Test all aspects of the `Nutrient` class.
	"""

	from nutrient import Nutrient

	print('='*99)
	print('TESTING `Nutrient`\n')

	print('Testing class initialization:')
	new_nutrient = Nutrient()
	print(f'\tNew nutrient: {new_nutrient}')
	print(f'\thasMoved value: {new_nutrient.hasMoved}')

	print('Testing `setMoved`:')
	print(f'\tBefore move: {new_nutrient.getMoved()}')
	new_nutrient.setMoved()
	print(f'\tAfter move: {new_nutrient.getMoved()}')

	print('Testing `setMoved` with `hasMoved` already True:')
	print(f'\tBefore move: {new_nutrient.getMoved()}')
	new_nutrient.setMoved()
	print(f'\tAfter move: {new_nutrient.getMoved()}')

	print('Testing `clearMoved`:')
	print(f'\tBefore clear: {new_nutrient.getMoved()}')
	new_nutrient.clearMoved()
	print(f'\tAfter clear: {new_nutrient.getMoved()}')

	print('Testing `clearMoved` with `hasMoved` already False:')
	print(f'\tBefore clear: {new_nutrient.getMoved()}')
	new_nutrient.clearMoved()
	print(f'\tAfter clear: {new_nutrient.getMoved()}')

	print('='*99)

def test_microbe():
	"""
	Test all aspects of the `Microbe` class.
	"""

	from nutrient import Nutrient
	from microbe import Microbe

	print('='*99)
	print('TESTING `Microbe`\n')

	print('Testing class initialization:')
	new_microbe = Microbe()
	print(f'\tNew microbe: {new_microbe}')
	print(f'\theldNutrient value: {new_microbe.heldNutrient}')
	print(f'\thasNutrient: {new_microbe.hasNutrient()}')

	print('Taking nutrient:')
	new_nutrient = Nutrient()
	new_microbe.takeNutrient(new_nutrient)
	print(f'\theldNutrient: {new_microbe.heldNutrient}')
	print(f'\thasNutrient: {new_microbe.hasNutrient()}')
	print('\tIf `hasNutrient` test returned true, implies success of '
		'`takeNutrient`.')

	print('Consuming nutrient:')
	new_microbe.consumeNutrient()
	print(f'\theldNutrient: {new_microbe.heldNutrient}')
	print(f'\thasNutrient: {new_microbe.hasNutrient()}')
	print('\tIf `hasNutrient` test returned false, implies success of `consumeNutrient`.')

	# print('Testing `hasNutrient`:')

	print('='*99)

def test_petricell():
	"""
	Tests all aspects of the `PetriCell` class.
	"""

	from petri import PetriCell
	from nutrient import Nutrient

	print('='*99)
	print('TESTING `PetriCell`\n')

	print('Testing class initialization:')
	new_petricell = PetriCell()
	print(f'\tNew petricell: "{new_petricell}"')
	print(f'\tmicrobe value: {new_petricell.microbe}')
	print(f'\tnutrients value: {new_petricell.nutrients}')

	print('Adding microbe:')
	print('\tBefore adding microbe: hasMicrobe == '
		f'{new_petricell.hasMicrobe()}')
	new_petricell.createMicrobe()
	print('\tAfter adding microbe: hasMicrobe == '
		f'{new_petricell.hasMicrobe()}')
	print('Getting microbe:')
	print(f'\tMicrobe: {new_petricell.getMicrobe()}')
	print(f'\tNew string representation: {new_petricell}')

	n = 9
	print(f'Adding nutrients ({n}x):')
	print(f'\tHas nutrients (pre-add): {new_petricell.hasNutrients()}')
	# adding n nutrients
	for i in range(n):
		new_petricell.placeNutrient(Nutrient())
	print(f'\tHas nutrients: {new_petricell.hasNutrients()}')
	print(f'\tPetriCell status: {new_petricell}')

	m = 2
	print(f'Removing {m} nutrients, setting them moved, then replacing them:')
	for i in range(m):
		nutrient = new_petricell.getNutrient()
		nutrient.setMoved()
		new_petricell.placeNutrient(nutrient)
	nut_status = [nut.getMoved() for nut in new_petricell.nutrients]
	print(f'\tNutrients moved: {nut_status}')
	unmoved_nutrients = new_petricell.getUnmoved()
	print(f'\tUnmoved nutrients removed: {len(unmoved_nutrients)}')
	print(f'\tPetriCell without unmoved nutrients: {new_petricell}')
	print(f'\tMoving unmoved nutrients.')
	moved_nutrients = []
	for nutrient in unmoved_nutrients:
		nutrient.setMoved()
		moved_nutrients.append(nutrient)
	del unmoved_nutrients
	print(f'\tMarking remaining nutrients in PetriCell unmoved.')
	new_petricell.clearAllMoved()
	print(f'\tRe-adding nutrients.')
	for nutrient in moved_nutrients:
		new_petricell.placeNutrient(nutrient)
	nut_status = [nut.getMoved() for nut in new_petricell.nutrients]
	print(f'\tNutrients moved: {nut_status}')
	print(f'Clearing all nutrient move status.')
	new_petricell.clearAllMoved()
	nut_status = [nut.getMoved() for nut in new_petricell.nutrients]
	print(f'\tNutrients moved: {nut_status}')

	print('='*99)

if __name__ == '__main__':
	"""
	If this module is run directly, then execute each of the testers in turn.
	"""

	test_nutrient()
	test_microbe()
	test_petricell()
