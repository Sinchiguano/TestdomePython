#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.


"""
Path

Write a function that provides change directory (cd) function for an abstract file system.

Notes:

    Root path is '/'.
    Path separator is '/'.
    Parent directory is addressable as '..'.
    Directory names consist only of English alphabet letters (A-Z and a-z).
    The function should support both relative and absolute paths.
    The function will not be passed any invalid paths.
    Do not use built-in path-related functions.
"""


class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        #loading paths
        new_path=new_path.split('/')
        path=self.current_path.split('/')
        print(new_path)
        print(path)

        space=0
        #if this is empty it means that we have the absolute path
        if new_path[0]=='':
            del path[:]
            path.append('/'+new_path[1])
            space+=2

        #here we deal with relative path
        while(space<len(new_path)):

            index=len(path)-1
            if new_path[space]=='..':
                path.pop(index)
            else:
                path.append(new_path[space])
            space+=1
        self.current_path='/'.join(path)
        pass

'''
Palindrome

A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

'''


def is_palindrome(word):
  str = "" 
  word=word.lower()
  for i in word: 
    str = i + str
  print(word,'/',str)
  return word==str

'''
Playlist

A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.

Implement a function is_repeating_playlist that, efficiently with respect to time used, returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.
'''
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
                
    def is_repeating_playlist(self): 
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        my_set = set()
        current_object =self
        while(current_object):
            if current_object.name in my_set: # if we already saw this song
                return True
            my_set.add(current_object.name)
            current_object = current_object.next#we pass object not song at all
            #print(my_set)
        return False # no repeats found



#A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).



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


'''

Ice Cream Machine

Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. 
If there are no ingredients or toppings, the method should return an empty list.

'''
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        tmp=list()
        if self.ingredients==None or self.toppings==None:
            return tmp 
        else:
            for ing in self.ingredients:
                for top in self.toppings:
                    tmp.append([ing,top])
            return tmp
        pass




'''

Pipeline

As part of a data processing pipeline, complete the implementation of the pipeline method:

    The method should accept a variable number of functions, and it should return a new function that accepts one parameter arg.
    The returned function should call the first function in the pipeline with the parameter arg, and call the second function with the result of the first function.
    The returned function should continue calling each function in the pipeline in order, following the same pattern, and return the value from the last function.

For example, pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2) then calling the returned function with 3 should return 5.0.

'''

def pipeline(*funcs):

    def helper(arg):
       
        for f in funcs :
            arg = f(arg)
            #print(arg)
        return arg
        
        #pass#do not care if there is nothing, it will still run it!!!
    return helper


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
   
'''
League Table

The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 

The player's rank in the league is calculated using the following logic:

    The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
    If two players are tied on score, then the player who has played the fewest games is ranked higher.
    If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.

Implement the player_rank function that returns the player at the given rank.
'''






def main():

    #Path
    #--------
    path = Path('/a/b/c/d')
    #path.cd('/a/b/c/x')
    #path.cd('../x')
    #path.cd('../../x')
    #print(path.current_path)

    #Palindrome
    #-----------
    #print(is_palindrome('Deleveled'))


    #Playlist
    #----------
    # first = Song("Hello")
    # second = Song("Eye of the tiger")
    # #third = Song("We Will Rock You")

    # first.next_song(second)
    # second.next_song(first)

    # print(first.is_repeating_playlist())
    first = Song("Hello")
    second = Song("Eye of the tiger")
    third = Song("We Will Rock You")

    first.next_song(second)
    #second.next_song(first)
    second.next_song(third)

    #print(first.is_repeating_playlist()) 


    #Binary Search Tree
    #---------------------

    import collections

    Node = collections.namedtuple('Node', ['left', 'right', 'value'])       
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
    

    # for p in [ n1, n3,n2 ]:
    #     #print(p)
    #     print ('%s  %s %d' % p )  

    print('Contain value: {}'.format(contains(n2, 3)))
    #Merge Names
    #---------------

    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia////['Ava', 'Olivia', 'Emma', 'Sophia']

    #Ice Cream Machine
    #--------------------

    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    #machine = IceCreamMachine([], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]



    #Pipeline
    #------------------
    fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
    print(fun(3)) #should print 5.0


    #File Owners
    #---------------------
    files = {'Input.txt': 'Randy','Code.py': 'Stan','Output.txt': 'Randy'}   
    print(group_by_owners(files))

if __name__ == '__main__':
	main()


# import collections

# Person = collections.namedtuple('Person', 'name age gender')
# print ('Type of Person:', type(Person))

# bob = Person(name='Bob', age=30, gender='male')
# print ('\nRepresentation:', bob)

# jane = Person(name='Jane', age=29, gender='female')
# print ('\nField by name:', jane.name)

# print( '\nFields by index:')
# for p in [ bob, jane ]:
#     print(p)
#     print ('%s is a %d year old %s' % p)


# ##########################
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
# print('squared: ',squared)


# ########################
# def multiply(x):
#     return (x*x)
# def add(x):
#     return (x+x)

# funcs = [multiply, add]
# for i in range(5):
#     value = list(map(lambda x: x(i), funcs))
#     print(value)
# #################
# print('reduce')
# product = 1
# list_ = [1, 2, 3, 4]
# for num in list_:
#     product = product * num
# print('product normal',product)


# import functools
# from functools import reduce
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# print('product reduce',product)

# ##################################################
# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print('filter',less_than_zero)
# ##################################

# people = [{'name': 'Mary', 'height': 160},
#           {'name': 'Isla', 'height': 80},
#           {'name': 'Sam'}]

# heights = map(lambda x: x['height'],filter(lambda x: 'height' in x, people))

# print('heights',heights)
# for height in heights: