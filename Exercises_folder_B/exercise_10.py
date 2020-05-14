#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Napisz program fitness obliczający BMI

#BMI = waga / (wzrost)2

height = float(input("Podaj wzrost w centymetrach: "))
weight = float(input("Podaj wagę w kilogramach: "))
bmi = round((weight / (height **2) * 10000))

wynik = 0

if (bmi <= 18.5)  :
    wynik += bmi
    print("Masz niedowagę. Zmień dietę, dobrze się odżywiaj.")

elif (bmi >= 18.5 and bmi <= 25)  :
    wynik += bmi
    print("Masz idealną wagę. Tak trzymaj!")

elif (bmi >= 25 and bmi <= 26)  :
    wynik += bmi
    print("Masz lekką nadwagę. Zmień dietę i zacznij ćwiczyć")
elif (bmi >= 26.1 and bmi <= 29.9)  :
    wynik += bmi
    print("Masz nadwagę. Pilnie zmień dietę i zacznij ćwiczyć. Dasz radę!")
elif (bmi >= 30)  :
    wynik += bmi
    print("Cierpisz na otyłość. Pilnie zmień dietę i zacznij ćwiczyć, ale najpierw skonsultuj się z lekarzem. Nigdy nie jest za póżno. ")

print("Twoje BMI to: ", bmi)
