import unittest
import average

class TestCase(unittest.TestCase):

	def test_average1(self):
		self.assertEqual(average.Average([1, 2, 3, 4, 5, 6, 7]), 4)

	def test_average2(self):
		self.assertEqual(average.Average([0, 1]), 0.5)

	def test_average3(self):
		self.assertEqual(average.Average([1, 2, 3, 'l']), None)

if __name__ == '__main__':
	unittest.main(verbosity=2)