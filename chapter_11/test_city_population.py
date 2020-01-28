#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

import unittest

from population import city_country

class populationTestCase(unittest.TestCase):
	"""Test the city_country Function."""
	def test_city_country(self):
		"""Test the output includes the population."""
		output = city_country('santiago', 'chile')

		self.assertEqual(output,'Santiago, Chile - Population 500000')


if __name__ == '__main__':
	unittest.main()