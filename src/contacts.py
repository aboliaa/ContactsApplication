from tree import TernarySearchTree
from io import InputProcessor, OutputProcessor

def validateInput(func):
	def func_wrapper(self, contact):
		contact = self.input.validateContact(contact)
		func(self, contact)
	return func_wrapper

class ContactManager(object):
	def __init__(self):
		self.input = InputProcessor()
		self.output = OutputProcessor()
		self.contacts = TernarySearchTree()

	@validateInput
	def addContact(self, contact):
		""" Add a contact to ternary search tree
		"""
		self.contacts.insert(contact)

	def searchContact(self, contact, pretty=True):
		""" Search for a contact in ternary search tree
		"""
		result = self.contacts.prefixSearch(contact)
		if pretty:
			return self.output.pretty(result)
		else:
			return result

