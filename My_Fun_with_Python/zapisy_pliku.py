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

"""
