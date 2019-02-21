#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

'''
File Owners

Implement a group_by_owners function that:

    Accepts a dictionary containing the file owner name for each file name.
    Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
'''

def group_by_owners(files):
	my_dict = {}
	for key,value in files.items():
        #if i already have value as key in my new dictionary i will skip, otherwise i will create a new one, key is value in a new dict
		if value in my_dict:
			my_dict[value].append(key)
		else:
			my_dict[value] = [key]
	return my_dict


def main():


    #File Owners
    #---------------------
    files = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'}   
    print(group_by_owners(files))

if __name__ == '__main__':
	main()

