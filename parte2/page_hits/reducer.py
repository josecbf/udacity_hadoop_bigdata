#!/usr/bin/python

import sys

currentPage = None
countPage = 0

for line in sys.stdin:
	newPage = line.strip().split()
	
	if len(newPage) != 1:
		continue

	if currentPage and currentPage != newPage:
		print "{0}\t{1}".format(currentPage, countPage)
		countPage = 0
	
	currentPage = newPage
	countPage += 1

if currentPage != None:
	print "{0}\t{1}".format(currentPage, countPage)
