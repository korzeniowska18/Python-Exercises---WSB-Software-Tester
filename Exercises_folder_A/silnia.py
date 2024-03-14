#!usr/bin/python
#! -*- coding: utf-8 -*-

#Napisz program zawierający funkcję zwracająca silnię liczby podanej jako argument.

#Wskazówka: Policz silnię iteracyjnie. (1 * 2 * 3 *4 *5)

def silnia(liczba):
    wynik = 1
    for licznik in range(2, liczba + 1):
        wynik *= licznik
    return wynik
print(silnia(5))
