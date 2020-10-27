# * - gwiazdka oznacz "Dopasuj zero lub więcej wystąpień"
# + - plus oznacza "Dopasuj jedno wystąpienie lub więcej wystąpień", ta grupa ze stringiem w nawiasach, np. (ecz), 
#     musi wystąpić przynajmniej jeden raz, jeżeli chcemy dopasować znak plus, musimy to zrobić w ten sposób: \+
# re.search("(cud){2}",text) - wyszykiwanie odpowiedniej ilości powtórzeń, dopasuje podwójne powtórzenie "cudcud"
#     (cud){2, 4} - podwójne lub czterokrotne, (cud){2,} - od dwóch i wiecej, (cud){,4} - od zera do czterech
#     (cud){2, 4} - dopasowanie zachłanne - dopasuje największą liczbę
#     (cud){2, 4}? - dopasowanie niezachłanne - dopasuje najkrótszy ciąg tekstowy

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

>>> import re
>>> message = re.compile(r'ogród(ecz)+ku')
>>> message1 = message.search("Kotki bawią się w ogródeczku")
>>> message1.group()
'ogródeczku'
>>> message2 = message.search("Kotki bawią się w ogródeczeczeczku")
>>> message2.group()
'ogródeczeczeczku'
>>> message3 = message.search("Kotki bawią się w ogródku")
>>> message3 == None
True
>>> 


>>> import re
>>> text = "Jaki Świat jest cudowny, jest to cudcud"
>>> proba1 = re.search("^Jaki.*cud$",text)
>>> print(proba1)
<re.Match object; span=(0, 39), match='Jaki Świat jest cudowny, jest to cudcud'>
>>> proba2 = re.search("(cud){2}",text)
>>> print(proba2)
<re.Match object; span=(33, 39), match='cudcud'>
>>> proba3 = re.search("(cud){3}",text)
>>> print(proba3)
None
>>> proba5 = re.search("(cud){1}",text)
>>> print(proba5)
<re.Match object; span=(16, 19), match='cud'>
>>> 

>>> proba8 = re.compile(r'(cud){2}')
>>> text = proba8.search("Jaki Świat jest cudowny, jest to cudcud")
>>> text.group()
'cudcud'

>>> proba9 = re.compile(r'(cud){2,}')
>>> text = proba9.search("Jaki Świat jest cudowny, jest to cudcudcud")
>>> text.group()
'cudcudcud'
>>> 

Zachłanne 

>>> import re
>>> cudRe = re.compile(r'(Cud){2,4}')
>>> szukamy = cudRe.search('CudCudCudCud')
>>> szukamy.group()
'CudCudCudCud'
>>> 
niezachłanne

>>> cudRe = re.compile(r'(Cud){2,4}?')
>>> szukamy2 = cudRe.search('CudCudCudCud')
>>> szukamy2.group()
'CudCud'
>>> 

