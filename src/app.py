import sys
from contacts import ContactManager

def validateOption(option):
	if not option.isdigit():
		print "Invalid option"
		return False
	else:
		return True

def addContact(app):
	contact = raw_input("Enter name: ")
	return app.addContact(contact)

def searchContact(app):
	contact = raw_input("Enter name: ")
	return app.searchContact(contact)


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
			print searchContact(app)
		elif option == 3:
			print "Happy searching"
			sys.exit(0)

