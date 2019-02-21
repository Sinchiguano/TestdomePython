#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""

"""

#first exercise

def is_palindrome(word):
  str = "" 
  word=word.lower()
  for i in word: 
    str = i + str
  print(word)
  print(str)
  return word==str

print(is_palindrome('Deleveled'))


print('#####')

#second exercise
def group_by_owners(files):
	my_dict = {}
	for key,value in files.items():
		if value in my_dict:
			my_dict[value].append(key)
		else:
			my_dict[value] = [key]
	return my_dict
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))


# if None:
#     print(“Hello”)

for char in 'PYTHON STRING':
  if char == ' ':
      break

  print(char)
  
  if char == 'O':
      continue


class MyClass(object):
    def meth_a(self):
        pass

    def meth_b(self):
        print "I'm meth_b"


def greetPerson(*name):
  print('Hello', name)

greetPerson('Frodo', 'Sauron')


result = lambda x: x * x
print(result(5))


from math import pi
print(pi)



numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)


def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)	

# import os, sys
# os.listdir()


number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")


try:
  # code that can raise error
   pass
  
except (TypeError, ZeroDivisionError):
  print("Two")