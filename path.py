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
        #print(new_path)
        #print(path)

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



def main():

    #Path
    #--------
    path = Path('/a/b/c/d')
    path.cd('../x')
    print(path.current_path)

  
if __name__ == '__main__':
	main()
