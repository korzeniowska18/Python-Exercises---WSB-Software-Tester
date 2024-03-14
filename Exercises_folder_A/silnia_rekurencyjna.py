#!usr/bin/python
#! -*- coding: utf-8 -*-

#Napisz program liczący silnię rekurencujnie. (5 * 4 * 3 *2 * 1)

def silnia(x):
    if x < 1:
        return 1
    else:
        return x * silnia (x - 1)
print(silnia(5))
