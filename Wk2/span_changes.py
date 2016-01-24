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
span = parsed_file.find_objects_wo_child(parentspec=r'.*rstp.*',childspec=r'.*[0-9]d.*')

print '\n'
print 'VLANS WITH STP CHANGES'
print '-' * 30

for vlan in span:
	print vlan.text
	for child in vlan.all_children:
		print child.text

print '\n'

