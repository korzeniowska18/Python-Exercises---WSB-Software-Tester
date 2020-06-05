listaUczestnikow = []

while True:
    print("Podaj imię " + str(len(listaUczestnikow) + 1) + " uczestnika zebrania: (Nic nie wpisując zakończysz listę.):")
    name = input()
    if name == "":
        break
    listaUczestnikow = listaUczestnikow + [name.capitalize()]
    
print("Liczba uczestników zebrania: " + str(len(listaUczestnikow)))
print("Jako pierwszy(a) przybył(a) na zebranie: " + (listaUczestnikow)[0])
print("Jako ostatni(ia) przybył(a) na zebranie: " + (listaUczestnikow)[-1])
print("Lista uczestników zebrania: ")
listaUczestnikow.sort()
for name in listaUczestnikow:
    print(" " + name)
