#!/usr/bin/env python

'''
Modules to import
'''

import re
from ciscoconfparse import CiscoConfParse
from sys import argv

'''
End of Modules
'''

script, file = argv


input_file = file
parsed_file = CiscoConfParse(file)
traffic = parsed_file.find_objects_wo_child(parentspec=r'.*connected.*', childspec='.*1/255.*1/255.*')

print '\n'
print 'INTERFACES WITH TRAFFIC'
print '-' * 30

for int in traffic:
	print int.text
	for child in int.children:
		print child.text

