#!/usr/bin/env python

'''
Program to create a list containing different values. This list will
then be written to a file using both YAML and JSON.
'''

##Modules needed to run program##
import yaml
import json
from sys import argv
##End of import##

def convert():

	script, file = argv

	yml_file = file +'.yml'
	json_file = file + '.json'

	new_dict = {'hostname': 'router', 'ip_addr': '1.1.1.1', 'vendor': 'cisco'}

	new_list = ['my name','my pet', 150, 22, new_dict, 'new school', 'old school']

	with open(yml_file, "w") as f:
		f.write(yaml.dump(new_list, default_flow_style=False))

	with open(json_file, "w") as f:
		json.dump(new_list, f)


if __name__ == "__main__":
	convert()





