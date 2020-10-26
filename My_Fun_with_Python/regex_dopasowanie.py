import re   >>> tworzenie obiektów wyrażeń regularnych. W tym module znajdują się wszystkie funkcje wyrażeń regularnych

re.compile(), search(), group(), groups(), znak | , findall()

grupowanie z użyciem nawiasów:

zmienna = re.compile(r'(\d\d)-(\d\d\d-\d\d-\d\d)')
message = zmienna.search("Mój numer telefonu: 71-722-75-25")
message.group(1)
>>>'71'
>>> message.group()
'71-722-75-25'

Znak | jest nazywany - potokiem, wykorzystujemy tam, gdzie trzeba dopasować jedno z wielu wyrażeń.

>>> findRegex = re.compile(r'numer|telefonu')
>>> wynik1 = findRegex.search("numer telefonu")
>>> wynik1.group()
'numer'

>>> wynik2 = findRegex.search("telefonu numer")
>>> wynik2.group()
'telefonu'
>>> 

>>> import re
>>> komRegex = re.compile(r'kom(nata|puter|órka|pas)')
>>> wynik = komRegex.search("Czy Bursztynowa komnata nareszcie odnaleziona?")
>>> wynik.group()
'komnata'
>>> wynik.group(1)
'nata'
>>> wynik2 = komRegex.search("komputer osobisty (Personal Computer) alias PC (pecet) jest obecnie najbardziej popularny na całym świecie i używany praktycznie wszędzie.")
>>> wynik2.group()
'komputer'
>>> wynik2.group(1)
'puter'
>>> 


>>> import re
>>> word = re.compile(r'anten(n)*a')
>>> w1 = word.search("Została podłączona antena")
>>> w1.group()
'antena'
>>> w2 = word.search("Została podłączona antenna")
>>> w2.group()
'antenna'
>>> w3 = word.search("Została podłączona antenna")
>>> w3.group()
'antenna'
>>> w4 = word.search("Została podłączona antennnnna")
>>> w4.group()
'antennnnna'
>>> 

>>> import re
>>> message = re.compile(r'ogród(ecz)?ku')
>>> message1 = message.search("Kotki bawią się w ogródku")
>>> message1.group()
'ogródku'
>>> message2 = message.search("Kotki bawią się w ogródeczku")
>>> message2.group()
'ogródeczku'
>>> 
