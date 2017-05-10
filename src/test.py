import unittest
from contacts import ContactManager

class TestCases(unittest.TestCase):
	def setUp(self):
		cm = ContactManager()
		cm.addContact("Chris Harris")
		cm.addContact("Chris Cairns")
		cm.addContact("Harry Potter")
		cm.addContact("Chris")
		cm.addContact("Ellen")
		self.cm = cm

	def testPrefix(self):
		result = self.cm.searchContact("Ch", pretty=False)
		result.sort()
		expected = ["Chris", "Chris Harris", "Chris Cairns"]
		expected.sort()
		self.assertEqual(expected, result)

	def testCaseSensitive(self):
		result = self.cm.searchContact("ch", pretty=False)
		result.sort()
		expected = ["Chris", "Chris Harris", "Chris Cairns"]
		expected.sort()
		self.assertEqual(expected, result)

	def testOnlyName(self):
		result = self.cm.searchContact("El", pretty=False)
		result.sort()
		expected = ["Ellen"]
		expected.sort()
		self.assertEqual(expected, result)

	def testNoMatch(self):
		result = self.cm.searchContact("abc", pretty=False)
		result.sort()
		expected = []
		expected.sort()
		self.assertEqual(expected, result)

	def tearDown(self):
		self.cm = None

if __name__ == "__main__":
	unittest.main()
