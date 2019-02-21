#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.


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


def main():

    #Pipeline
    #------------------
    fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
    print(fun(3)) #should print 5.0


if __name__ == '__main__':
	main()

