#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.


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


def main():

    #Playlist
    #----------
    first = Song("Hello")
    second = Song("Eye of the tiger")

    first.next_song(second)
    second.next_song(first)
    print(first.is_repeating_playlist())


if __name__ == '__main__':
	main()
