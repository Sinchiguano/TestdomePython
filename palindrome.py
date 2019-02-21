#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.



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


def main():


    #Palindrome
    #-----------
    print(is_palindrome('Deleveled'))



if __name__ == '__main__':
	main()

