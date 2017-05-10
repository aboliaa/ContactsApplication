
"""
Implementation of Ternary Search Tree.

[Wikipedia]
A ternary search tree is a type of trie where nodes are arranged in a manner 
similar to a binary search tree, but with up to three children rather than the 
binary tree's limit of two. Like other prefix trees, a ternary search tree can 
be used as an associative map structure with the ability for incremental string search.

Ternary search trees are more space-efficient than tries, because each node can
have atmost 3 children (there can be upto 26 children in tries).

Tries can be more time-efficeint than ternary search trees, there can space/time
tradeoff.

References:
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
		""" Print a node in readable format.
		"""
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

	def _nodeVal(self, node):
		""" Return the value of node.
		"""
		if not node:
			return None
		if node.val is None:
			return None
		return node.val

	def getVal(self, v):
		""" Return the value of node/char depending on case-sensitivity.
		"""
		if type(v) == Node:
			v = self._nodeVal(v)
		if v is None:
			v = ""

		if self.caseSensitive:
			return v
		else:
			return v.lower()

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
		""" Insert a word in tree.
		"""
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
		""" Preorder depth first traversal of a tree.
		"""
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

		if self.getVal(ch) < self.getVal(node.val):
			return self._search(word, node.left)
		elif self.getVal(ch) > self.getVal(node.val):
			return self._search(word, node.right)
		else:
			if len(word) == 1:
				return node.isEndOfWord
			else:
				return self._search(word[1:], node.equal)

	def search(self, word):
		""" Search for exact word.
		"""
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

		if self.getVal(ch) < self.getVal(node.val):
			return self._prefixSearch(string, word, node.left, results)
		elif self.getVal(ch) > self.getVal(node.val):
			return self._prefixSearch(string, word, node.right, results)
		else:
			if len(string) == 1:
				if node.isEndOfWord:
					logger.debug("End of word " + string)
					results.append(word+node.val)
				if node.equal:
					DFSResults = self._DFS(node.equal, word+node.val+node.equal.val, results)
					results.extend(DFSResults)
				results = list(set(results))
			else:
				return self._prefixSearch(string[1:], word+node.val, node.equal, results)
		return results

	def prefixSearch(self, string):
		""" Prefix search
		"""
		if not self.root:
			return []

		if not string:
			return []

		results = []
		return self._prefixSearch(string, "", self.root, results)

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
	print t.prefixSearch("CA")
	print "================"
	print t.prefixSearch("up")
	
	print "\nDFS:"
	# t.DFS()

