#!usr/bin/python
#! -*- coding: utf-8 -*-

#Napisz program sprawdzający, czy podane słowo jest palindromem.

def  is_palindrome(s):
               return s[::-1] == s
               


>>> s = 'tenet'
>>> is_palindrome(s)
True
>>> s = 'tenet', 'Kobyła ma mały bok', 'mam', 'dama'
>>> is_palindrome(s)
False
>>> s = 'tenet', 'Kobyła ma mały bok', 'mam'
>>> is_palindrome(s)
False
>>> s = 'Kobyła ma mały bok'
>>> is_palindrome(s)
False
>>> s = 'mam'
>>> is_palindrome(s)
True
