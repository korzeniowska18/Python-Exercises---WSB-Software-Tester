#można użyć różne permissions: w, r+(read and write), a(append)

MojPlik = open("przykladowy.txt", "w")

print("Nazwa pliku " + MojPlik.name)
print("Permissions " + MojPlik.mode)

MojPlik.write("Lista na zakupy:\nChlebek: 1\nMleko: 2\nSzynka: 1 kg")

MojPlik.close()

MojPlik = open("przykladowy.txt", "r")
print("Czytam moj plik: " + MojPlik.read(15))   #podano liczbe znakow do odczytania
print("Odczytam plik znowu: " + MojPlik.read(15))

MojPlik.close()

#Jeżeli chcemy odczytać plik od nowa od pierwszego wiersza, to musimy użyć "seek(0)" i zresetować

MojPlik = open("przykladowy.txt", "r")
print("Czytam moj plik: " + MojPlik.read(15))   #podano liczbe znakow do odczytania
MojPlik.seek(0)
print("Odczytam plik znowu: " + MojPlik.read(15))

MojPlik.close()

#można to zrobić w inny sposób przez ponowne otwarcie i zamknięcie pliku

MojPlik = open("przykladowy.txt", "r")
print("Czytam moj plik: " + MojPlik.read(15))   #podano liczbe znakow do odczytania
MojPlik.close()
MojPlik = open("przykladowy.txt", "r")
print("Odczytam plik znowu: " + MojPlik.read(15))

MojPlik.close()

MojPlik = open("przykladowy.txt", "r")
print("Pierwsza linia pliku: ", MojPlik.readline())
print("Druga linia pliku: ", MojPlik.readline())
MojPlik.seek(0)
print("Otwieramy plik znowu i czytamy od pocza,tku.\nPierwsza linia pliku: ", MojPlik.readline())

MojPlik = open("przykladowy.txt", "r")
for line in MojPlik:
    ZamieniamyWpis = line.replace("Chlebek", "Bagietka")
    print(ZamieniamyWpis)
    
MojPlik.close()

"""
>>>
Nazwa pliku przykladowy.txt
Permissions w

#do pliku dodaje:
Lista na zakupy:
Chlebek: 1
Mleko: 2
Szynka: 1 kg

>>>

Nazwa pliku przykladowy.txt
Permissions w
Czytam moj plik: Lista na zakupy
Odczytam plik znowu: :
Chlebek: 1
Ml

>>>

Czytam moj plik: Lista na zakupy
Odczytam plik znowu: :
Chlebek: 1
Ml
Czytam moj plik: Lista na zakupy
Odczytam plik znowu: Lista na zakupy
>>>

Czytam moj plik: Lista na zakupy
Odczytam plik znowu: Lista na zakupy
Czytam moj plik: Lista na zakupy
Odczytam plik znowu: Lista na zakupy

>>>

Pierwsza linia pliku:  Lista na zakupy:

Druga linia pliku:  Chlebek: 1

Otwieramy plik znowu i czytamy od pocza,tku.
Pierwsza linia pliku:  Lista na zakupy:

>>>

Lista na zakupy:

Bagietka: 1

Mleko: 2

Szynka: 1 kg

"""
