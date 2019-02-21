#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.



'''
Binary Search Tree

Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.

Write a function that, efficiently with respect to time used, checks if a given binary search tree contains a given value.

For example, for the following tree:

    n1 (Value: 1, Left: null, Right: null)
    n2 (Value: 2, Left: n1, Right: n3)
    n3 (Value: 3, Left: null, Right: null)

Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
'''

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    #print(root,value)
    if root==None:
        return False
    if root.value==value:
        return True
    elif (root.value > value) :
        return contains(root.left, value)#from the screen
    else:
        return contains(root.right, value)#from the screen
    pass


def main():

    #Binary Search Tree
    #---------------------

    import collections

    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
            
    print(contains(n2, 3))
        

    # for p in [ n1, n3,n2 ]:
    #     #print(p)
    #     print ('%s  %s %d' % p )  

    #print('Contain value: {}'.format(contains(n2, 3)))

if __name__ == '__main__':
	main()

