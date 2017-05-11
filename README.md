# ContactsApplication
A phonebook-like application to add and search the contacts

What it does:
1. It handles user-input errors.
2. Search is case-sensitive.
3. Exact-matches are ranked higher than prefix-matches.

What it doesn't do:
1. Search by lastName is not implemented.
2. Unicode names are not handled.

How to run:
1. Using makefile:
	- To run the program, 'make run'
	- To run testcases, 'make test'
2. Without make:
	- Go to <codebase>/src
	- Run as 'python app.py'
