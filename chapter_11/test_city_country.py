#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

import unittest

from city_country import city_country

class CityTestCase(unittest.TestCase):
	"""Test the city country function."""
	def test_city_country(self):
		"""Will the function work?"""
		output = city_country('santiago', 'chile')
		#Test if the result of city_country (output) is the same as 'Santiago, Chile'
		self.assertEqual(output,'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()