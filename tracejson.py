#!/usr/bin/env python

import sys, os
import subprocess

filename = sys.argv[1]
output = 'output_'+filename
# filename = './' + filename

f = open(filename, 'r')
outputFile = open(output, 'w')
outputFile.write('traceroute:[')
outputFile.close()

lastID = 0
for line in f:
	line = line.strip()
	f = line.find('(')
	l = line.find(')')
	ip = line[f+1:l]
	ipinfo = subprocess.Popen(['curl', 'ipinfo.io/%s' %(ip)], stdout=subprocess.PIPE)
	(out, err) = ipinfo.communicate()
	with open(output, "a") as outputFile:
		if out:
			outputFile.write(out)
			outputFile.write(',')
		else:
			pass

with open(output, 'rb+') as outputFile:
	outputFile.seek(-1, os.SEEK_END)
	outputFile.truncate()
outputFile.close()
outputFile = open(output, 'a')
outputFile.write(']')
outputFile.close()
