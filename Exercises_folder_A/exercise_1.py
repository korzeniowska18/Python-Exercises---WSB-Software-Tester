#!usr/bin/python
#! -*- coding: utf-8 -*-

#Napisz program suma.py, który wyświetli sumę dwóch liczb podanych przez użytkownika

a = int(input("Podaj pierwszą liczbę: "))

b = int(input("Podaj drugą liczbę: "))

wynik = a + b

print("Wynik dodawania dwóch liczb to: ", wynik)

--------------------------------------------------------

def suma_liczb(a, b):
    return a + b
a = int(input("Podaj pierwszą liczbę: "))

b = int(input("Podaj drugą liczbę: "))
print("Wynik dodawania dwóch liczb to: ", suma_liczb(a, b))
