#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""
Task 3
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string in the following manner:
● All sorted lowercase letters are ahead of uppercase letters.
● All sorted uppercase letters are ahead of digits.
● All sorted odd digits are ahead of sorted even digits.
Input Format
A single line of input contains the string.
Constraints
0 < len(S) < 1000
Output Format
Output the sorted string.
"""

def preprocessing_string(word):
    'This function select uppercase, lowercase and numbers from the input string.'
    strUP = ""
    strLOW = ""
    num=list()
    for c in word:
        if c.isupper():
            strUP= c+strUP
        elif c.islower():
            strLOW =c+strLOW 
        else:
            if c.isdigit():
                num.append(int(c))
    up=sorted(strUP)
    low=sorted(strLOW)
    return up,low,num

def even_odd_number(num):
    'This function check if a number is even or odd, then proceeds to cluster each of them to even or odd group.'
    tmp=list()
    aux=list()
    for i in range(len(num)):
        if num[i]%2==0:#even number
            tmp.append(num[i])
        else:#odd number
            aux.append(num[i])
    tmp_=sorted(tmp, reverse=False)
    aux_=sorted(aux, reverse=False)
    return tmp_,aux_

def final(up,low,odd,even):
    'Final append the uppercase, lowercase and number according the to pattern given'
    one_word=low+up+odd+even
    tmp=" "
    for i in one_word:
        tmp = tmp + str(i)
        #print(i)
    return tmp

 
# Sample Input--> Sorting1234
# Sample Output--> ginortS1324
def main():

    print ("\n============ Enter alphanumeric characters only:")
    word=input()
    print('Sample Input: {}'.format(word))

    up,low,num=preprocessing_string(word)
    #print(preprocessing_string(word))
    even,odd=even_odd_number(num)
    #print(even_odd_number(num))
    #print(final(up,low,odd,even))
    casch=final(up,low,odd,even)
    #print(final(up,low,odd,even))
    print('Sample Ouput: {}'.format(casch))


if __name__=='__main__':
    main()