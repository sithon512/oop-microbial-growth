"""
This module acts as a tester for the classes designed in this project. Here
the classes can be referenced and used in isolation to ensure that they are
working properly.
"""

def test_nutrient():
	"""
	Test all aspects of the `Nutrient` class.
	"""

	from nutrient import Nutrient

	print('='*80)
	print('TESTING `Nutrient`\n')

	print('Testing class initialization:')
	new_nutrient = Nutrient()
	print(f'\tNew nutrient: {new_nutrient}')
	print(f'\thasMoved value: {new_nutrient.getMoved()}')

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

	print('='*80)

def test_microbe():
	"""
	Test all aspects of the `Microbe` class.
	"""

	from nutrient import Nutrient
	from microbe import Microbe

	print('='*80)
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

	print('='*80)

if __name__ == '__main__':
	"""
	If this module is run directly, then execute each of the testers in turn.
	"""

	test_nutrient()
	test_microbe()
