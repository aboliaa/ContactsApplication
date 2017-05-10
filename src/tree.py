
"""
Implementation of Ternary Search Tree.

http://www.geeksforgeeks.org/ternary-search-tree/
https://www.cs.usfca.edu/~galles/visualization/TST.html
http://hacktalks.blogspot.in/2012/03/implementing-auto-complete-with-ternary.html

"""

from log import logger

__all__ = ["TernarySearchTree"]

class Node(object):
	def __init__(self, val, isEndOfWord=False):
		self.val = val
		self.isEndOfWord = isEndOfWord
		self.left = None
		self.right = None
		self.equal = None

	def __repr__(self):
		leftval = self.left.val if self.left else None
		equalval = self.equal.val if self.equal else None
		rightval = self.right.val if self.right else None
		msg = "\nChar = %s, End-of-word = %s \nLeft = %s, Equal = %s, Right = %s"
		args = (self.val, self.isEndOfWord, leftval, equalval, rightval)
		return msg %args

class TernarySearchTree(object):
	def __init__(self, caseSensitive=False):
		self.root = None
		self.caseSensitive = caseSensitive

	def nodeVal(self, node):
		if not node:
			return None
		if node.val is None:
			return None
		return node.val

	def compareVal(self, v1, v2):
		if type(v1) == Node:
			v1 = self.nodeVal(v1)
		if type(v2) == Node:
			v2 = self.nodeVal(v2)
		if v1 is None:
			v1 = ""
		if v2 is None:
			v2 = ""

		if self.caseSensitive:
			return v1 == v2
		else:
			return v1.lower() == v2.lower()

	def _insert(self, word, node=None):
		if not word:
			return

		ch = word[0]
		if not node:
			node = Node(ch)
		if not self.root:
			self.root = node

		logger.debug("Adding char " + ch)

		if ch < node.val:
			node.left = self._insert(word, node.left)
		elif ch > node.val:
			node.right = self._insert(word, node.right)
		else:
			if len(word) == 1:
				node.isEndOfWord = True
				logger.debug("End of string " + ch)
			else:
				node.equal = self._insert(word[1:], node.equal)
		return node
	
	def insert(self, word):
		return self._insert(word, self.root)

	def _DFS(self, node, word, results=[]):
		if node.isEndOfWord:
			logger.debug("Word found " + word)
			results.append(word)

		if not node.left and not node.equal and not node.right:
			return results

		if node.left:
			self._DFS(node.left, word[:-1]+node.left.val, results)
		if node.equal:
			self._DFS(node.equal, word+node.equal.val, results)
		if node.right:
			self._DFS(node.right, word[:-1]+node.right.val, results)

		return results

	def DFS(self):
		if not self.root:
			return
		word = self.root.val
		return self._DFS(self.root, word)

	def _search(self, word, node):
		if not node:
			return False

		if not word:
			return False

		ch = word[0]
		logger.debug("Char %s %s" %(ch, word))
		logger.debug(node)

		if ch < node.val:
			return self._search(word, node.left)
		elif ch > node.val:
			return self._search(word, node.right)
		else:
			if len(word) == 1:
				return node.isEndOfWord
			else:
				return self._search(word[1:], node.equal)

	def search(self, word):
		if not self.root:
			return False
		return self._search(word, self.root)

	def _prefixSearch(self, string, word, node, results=[]):
		if not string:
			return results
		if not node:
			return results

		ch = string[0]
		logger.debug("Char %s %s %s" %(ch, string, word))
		logger.debug(node)

		if ch < node.val:
			return self._prefixSearch(string, word, node.left)
		elif ch > node.val:
			return self._prefixSearch(string, word, node.right)
		else:
			if len(string) == 1:
				if node.isEndOfWord:
					logger.debug("End of word " + string)
					results.append(word+ch)
				if node.equal:
					DFSResults = self._DFS(node.equal, word+node.val+node.equal.val)
					results.extend(DFSResults)
			else:
				return self._prefixSearch(string[1:], word+ch, node.equal)
		return results

	def prefixSearch(self, string):
		if not self.root:
			return []

		if not string:
			return []
	
		return self._prefixSearch(string, "", self.root)

if __name__ == "__main__":
	t = TernarySearchTree()
	t.insert("cat")
	t.insert("cab")
	t.insert("hut")
	t.insert("bug")
	t.insert("cats")
	t.insert("up")
	t.insert("utter")

	print "\nSimple search:", t.search("bug")
	print "\nPrefix search:"
	print t.prefixSearch("cat")
	
	print "\nDFS:"
	t.DFS()
