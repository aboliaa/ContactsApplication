from const import DEBUG

class Node(object):
	def __init__(self, val, isEndOfString=False):
		self.val = val
		self.isEndOfString = isEndOfString
		self.left = None
		self.right = None
		self.equal = None

	def __repr__(self):
		leftval = self.left.val if self.left else None
		equalval = self.equal.val if self.equal else None
		rightval = self.right.val if self.right else None
		msg = "\nChar = %s, End-of-word = %s \nLeft = %s, Equal = %s, Right = %s"
		args = (self.val, self.isEndOfString, leftval, equalval, rightval)
		return msg %args

class TernarySearchTree(object):
	def __init__(self):
		self.root = None

	def _insert(self, word, node=None):
		if not word:
			return

		ch = word[0]
		if not node:
			node = Node(ch)
		if not self.root:
			self.root = node

		if DEBUG:
			print "Adding char", ch


		if ch < node.val:
			node.left = self._insert(word, node.left)
		elif ch > node.val:
			node.right = self._insert(word, node.right)
		else:
			if len(word) == 1:
				node.isEndOfString = True
				if DEBUG:
					print "End of string", ch
			else:
				node.equal = self._insert(word[1:], node.equal)
		return node
	
	def insert(self, word):
		return self._insert(word, self.root)

	def _DFS(self, node, word):
		if node.isEndOfString:
			print "Word found", word

		if not node.left and not node.equal and not node.right:
			return

		if node.left:
			self._DFS(node.left, word[:-1]+node.left.val)
		if node.equal:
			self._DFS(node.equal, word+node.equal.val)
		if node.right:
			self._DFS(node.right, word[:-1]+node.right.val)

	def DFS(self):
		if not self.root:
			return
		word = self.root.val
		return self._DFS(self.root, word)


	def _search(self, word, node=None):
		if not node:
			return False

		ch = word[0]
		if DEBUG:
			print "Char", ch, word 
			print node

		if ch < node.val:
			return self._search(word, node.left)
		elif ch > node.val:
			return self._search(word, node.right)
		else:
			if len(word) == 1:
				return node.isEndOfString
			else:
				return self._search(word[1:], node.equal)

	def search(self, word):
		return self._search(word, self.root)

	def prefixSearch(self, string):
		pass

if __name__ == "__main__":
	t = TernarySearchTree()
	t.insert("cat")
	t.insert("cab")
	t.insert("hut")
	t.insert("bug")
	t.insert("cats")
	t.insert("up")
	t.insert("utter")

	# print t.search("ca")
	t.DFS()
