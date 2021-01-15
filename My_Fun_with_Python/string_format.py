helloMessage = "Hej, %s!"
     
print(helloMessage % ("Lena"))
print(helloMessage % ("Alex"))
     
helloMessage = "Hej, {0:s}!"
     
print(helloMessage.format("Lena"))
print(helloMessage.format("Alex"))
     
helloMessage = "%s ma %d %s"
     
print(helloMessage % ("Lena",1,"kotka"))
print(helloMessage % ("Alex",100000,"$"))
     
helloMessage = "{0:s} ma {1:d} {2:s}"
     
print(helloMessage.format("Lena",1,"kotka"))
print(helloMessage.format("Alex",100000,"$"))

# 0 - elementów, 20 znaków zarezerowanego miejsca, s - string
     
line = "{0:20s} kosztują(je) {1:6d} €"
     
print(line.format('Lody',3))
print(line.format('Wycieczka',119))
print(line.format('PIZZA Margarita',6))

# 0 - liczba elementów, s - string, 1 - liczba elementów, d - cyfra(digital)
     
line = '{0:s} {1:d}'         
     
print(line.format('Lody', 3))
print(line.format('Wycieczka', 119))
print(line.format('PIZZA Margarita', 6))
