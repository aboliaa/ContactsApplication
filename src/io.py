from log import logger
from const import MAX_CONTACT_LEN

__all__ = ["InputProcessor", "OutputProcessor"]

class InputProcessor(object):
	def __init__(self):
		pass

	def validateContact(self, contact):
		# Remove extra leading and trailing whitespaces
		contact = contact.strip()

		# Check whether a contact contains any character other than an alphabet or whitespace
		if all(x.isalpha() or x.isspace() for x in contact):
			logger.debug("Only alphabets and spaces are present in contact %s" %contact)
		else:
			raise Exception("Invalid contact: Non-alpha characters present %s" %contact)

		subparts = contact.split()
		if len(subparts) == 1:
			# Contact contains only firstName
			pass
		elif len(subparts) == 2:
			# Contact contains firstName LastName
			contact = subparts[0].strip() + " " + subparts[1].strip()
		else:
			# More than one space separators. Invalid contact
			raise Exception("Invalid contact: Too many subparts %s" %contact)

		if len(contact) > MAX_CONTACT_LEN:
			raise Exception("Invalid contact: Max length exceeded %s" %contact)

		return contact

class OutputProcessor(object):
	def __init__(self):
		pass

	def format(self, output):
		if not output:
			return ""
		if not isinstance(output, list):
			raise Exception("Output is not in valid format")

		result = ""
		for o in output:
			result += o + "\n"
		return result
