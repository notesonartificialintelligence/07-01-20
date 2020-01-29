#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test for the employee class."""

	def setUp(self):
		"""
		Create an employee instance to be run in all tests.
		"""
		self.james = Employee('james','falcon','20000')

	def test_give_default_raise(self):
		"""Test the default value works."""
		self.james.give_raise()

		self.assertEqual(self.james.salary, 21000)

	def test_give_custom_raise(self):
		"""Test the custom value works."""
		self.james.give_raise('3000')

		self.assertEqual(self.james.salary, 23000)


if __name__ == '__main__':
	unittest.main()

