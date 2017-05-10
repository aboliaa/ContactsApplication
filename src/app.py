import sys
import traceback

from log import logger
from contacts import ContactManager

def validateOption(option):
	""" Validate user option. It should not be non-integer.
	"""
	if not option.isdigit():
		print "Invalid option"
		return False
	else:
		return True

def addContact(app):
	""" Accept a contact from user and add it to the tree.
	"""
	contact = raw_input("Enter name: ")
	try:
		app.addContact(contact)
	except Exception as e:
		logger.debug(traceback.format_exc())
		print "Error in adding contact: " + str(e)

def searchContact(app):
	""" Accept a searchterm from user and search for it in the tree.
	"""
	contact = raw_input("Enter name: ")
	try:
		print app.searchContact(contact)
	except Exception as e:
		logger.debug(traceback.format_exc())
		print "Error in searching contact: " + str(e)

if __name__ == "__main__":
	app = ContactManager()

	while True:
		option = raw_input("1) Add contact 2) Search 3) Exit ")
		if not validateOption(option):
			sys.exit(1)
		option = int(option)
		if option == 1:
			addContact(app)
		elif option == 2:
			searchContact(app)
		elif option == 3:
			print "Happy searching"
			sys.exit(0)

