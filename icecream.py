#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.


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


def main():


    #Ice Cream Machine
    #--------------------

    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    #machine = IceCreamMachine([], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]



if __name__ == '__main__':
	main()

