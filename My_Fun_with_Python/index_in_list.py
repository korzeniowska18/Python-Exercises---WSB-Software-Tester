print("Jak określić index każdego elementu z listy. \n")

womensWardrobe = ['sukienka', 'spódnica', 'bluzka', 'pasek', 'szalik', 'spodnie', 'płaszcz']
mensWardrobe = ['spodnie', 'koszula', 'dżinsy', 'krawat', 'podkoszulka', 'pasek', 'sweter', 'dres', 'garnitur']

print(" \n  Lista rzeczy z damskiej garderoby: \n")
 
for i in range(len(womensWardrobe)):
	print('Index ' + str(i) + ' na liście rzeczy z damskiej garderoby to: ' + womensWardrobe[i])

print(" \n  Damska garderoba zawiera: " + (str(len(womensWardrobe))) + " rzeczy \n")

print(" \n  Lista rzeczy z męskiej garderoby: \n")

for i in range(len(mensWardrobe)):
	print('Index ' + str(i) + ' na liście rzeczy z damskiej garderoby to: ' + mensWardrobe[i])


print(" \n  Męska garderoba zawiera: " + (str(len(mensWardrobe))) + " rzeczy \n")
