p = open("requirements.txt", "r")
licznik = 0
for line in p:
    print(str(licznik) + " " + line)
    licznik = licznik + 1
    
p.close()

p = open("requirements.txt", "r")
for line in p:
    line_split = line.split()
    if line_split[1] == "P":
        print(line)
    
p.close()

p = open("requirements.txt", "r")
inny_plik = open("InnyPlik.txt", "w")
for line in p:
    line_split = line.split()
    if line_split[1] == "P":
        inny_plik.write(line)
        print(line)
    
p.close()
inny_plik.close()




"""
>>>

0 robotframework

1 robotframework-seleniumlibrary

2 webdrivermanager

>>>

robotframework  P

robotframework-seleniumlibrary  P

webdrivermanager  P

>>> # InnyPlik.txt został w ten sposób stworzony i zawiera:

robotframework  P

robotframework-seleniumlibrary  P

webdrivermanager  P


"""
