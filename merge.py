#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.


'''
Merge Names

Implement the unique_names method. When passed two arrays of names, it will return an array containing the names that appear in either or both arrays. The returned array should have no duplicates.

For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return an array containing Ava, Emma, Olivia, and Sophia in any order.

'''

def unique_names(names1, names2):
    tmp=list()
    for n1,n2 in zip(names1,names2):
        if not n1 in tmp:
            tmp.append(n1)
        if not n2 in tmp:
            tmp.append(n2)
    return tmp


def main():
    #Merge Names
    #---------------

    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia////['Ava', 'Olivia', 'Emma', 'Sophia']

if __name__ == '__main__':
	main()
