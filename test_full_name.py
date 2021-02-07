import unittest
import full_name

class TestCase(unittest.TestCase):

	def test_full_name1(self):
		self.assertEqual(full_name.full_name("Ming", "Wei"), "Ming Wei")

	def test_full_name2(self):
		self.assertEqual(full_name.full_name("Ming1", "Wei1"), "Invalid name")

	def test_full_name3(self):
		self.assertEqual(full_name.full_name("Cathy", "Du"), "Cathy Du")

if __name__ == '__main__':
	unittest.main(verbosity=2)