import unittest
import cube

class TestCase(unittest.TestCase):

	def test_cube1(self):
		self.assertEqual(cube.Cube(2), 8)

	def test_cube2(self):
		self.assertEqual(cube.Cube(-3), -27)

	def test_cube3(self):
		self.assertEqual(cube.Cube("l"), None)

if __name__ == '__main__':
	unittest.main(verbosity=2)