#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

#The testing library.
import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'"""
	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name("Janis", "joplin")
		#Test if the result of formatted_name is the same as 'Janis Joplin'
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like "Wolfgang Amadeus Mozart" work?"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()