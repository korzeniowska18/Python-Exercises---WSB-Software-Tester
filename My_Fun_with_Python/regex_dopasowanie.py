# * - gwiazdka oznacz "Dopasuj zero lub więcej wystąpień"
# + - plus oznacza "Dopasuj jedno wystąpienie lub więcej wystąpień", ta grupa ze stringiem w nawiasach, np. (ecz), 
#     musi wystąpić przynajmniej jeden raz, jeżeli chcemy dopasować znak plus, musimy to zrobić w ten sposób: \+
# re.search("(cud){2}",text) - wyszykiwanie odpowiedniej ilości powtórzeń, dopasuje podwójne powtórzenie "cudcud"
#     (cud){2, 4} - podwójne lub czterokrotne, (cud){2,} - od dwóch i wiecej, (cud){,4} - od zera do czterech
#     (cud){2, 4} - dopasowanie zachłanne - dopasuje największą liczbę
#     (cud){2, 4}? - dopasowanie niezachłanne - dopasuje najkrótszy ciąg tekstowy
#     .search() - zwraca pierwsze dopasowanie i objekt Match
#     .findall() - zwraca wszystkie
#     \d - dowolna cyfra od 0 do 9
#     \0 - dowolny znak z wyłączeniem cyfr od 0 do 9
#     \w - Dowolna litera, cyfra lub znak podkreślenia(znaki 'słowa'(litery, cyfry, lub znaki podkreślenia))
#     \W - dowolny znak, który nie jest literą, cyfrą lub znakiem podkreślenia
#     \s - dowolna spacja, tabulator lub znak nowego wiersza(dopasowuje białe znaki)
#     \S - dowolny znak, który nie jest spacją, tabulatorem lub znakiem nowego wiersza.
#     (r'\d+\s\w+') - dopasowuje tekst zawierający jedna cyfrę lub więcej, spację, a dalej jeden znak lub więcej znaków 'słowa'
#     (r'[dsaeATK]') - w kwadratowych nawiasach możemy podać własną klasę znaków do wyszukiwania
#     (r'[KÓ0-3.]') - nie musimy oddzielać cyfry przez /, wyszukuje od 0 do 3 oraz kropki
#     (r'[^KÓ2-5.]') - znak daszku na poczatku wykona dopasowanie odwrotne, czy li wszystko oprócz tego co jest w nawiasach
#     (r'^Zakopane') - znak daszku, oznacza tu wyszukiwanie dopasowań zaczynających się z tych znaków
#     (r'Zakopane$') - zank dolara oznacza tu wyszukiwanie dopasowań kończących się tymi znakami
#     (r'.to') - znak wieloznaczny - czyli kropka - dopasowuje dowolny znak, ale tylko jeden 
 
poza znakiem nowego wiersza

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

>>> import re
>>> roomNumber = re.compile(r'\d\d\d-\d')
>>> roomNumber.findall('W pokojach num. 123-4 i 125-1 można złożyć wnioski')
['123-4', '125-1']
>>> text = 'W pokojach num. 123-4 i 125-1 można złożyć wnioski'
>>> roomNumber.findall(text)
['123-4', '125-1']
>>> roomNumber.search(text)
<re.Match object; span=(16, 21), match='123-4'>
>>> roomNumber = re.compile(r'(\d\d\d)-(\d)')   # zdefiniowane grupy
>>> text = 'W pokojach num. 123-4 i 125-1 można złożyć wnioski'
>>> roomNumber.findall(text)
[('123', '4'), ('125', '1')] # zwraca listę krotek ciągów tekstowych
>>> 

>>> roomNumber = re.compile(r'\d\d\d\s\w')  #dopasowanie za użyciem innych znaków
>>> text = 'W pokojach num. 123 A i 125 B można złożyć wnioski'
>>> roomNumber.findall(text)
['123 A', '125 B']
>>>

>>> roomNumber = re.compile(r'\d+\s\w+')
>>> text = 'W pokojach num. 123 w budynku-A i 125 w budynku-B można złożyć wnioski'
>>> roomNumber.findall(text)
['123 w', '125 w']
>>> text = 'W pokojach num. 123 budynek-A i 125 budynek-B można złożyć wnioski'
>>> roomNumber.findall(text)
['123 budynek', '125 budynek']
>>> text = 'W pokojach num. 123 budynek_A i 125 budynek_B można złożyć wnioski'
>>> roomNumber.findall(text)
['123 budynek_A', '125 budynek_B']
>>> 
>>> import re
>>> allZnaki = re.compile(r'[dsaeATK]')
>>> allZnaki.findall('KRUPÓWKI. Główną arterią komunikacyjną miasta są drewniane zakopiańskie restauracje, kawiarnie, galerie sztuki i sklepy z pamiątkami.')
['K', 'K', 'a', 'e', 'a', 'a', 's', 'a', 's', 'd', 'e', 'a', 'e', 'a', 'a', 's', 'e', 'e', 's', 'a', 'a', 'e', 'a', 'a', 'e', 'a', 'e', 'e', 's', 's', 'e', 'a', 'a']
>>> 

>>> allZnaki = re.compile(r'[KÓ0-3.]')
>>> allZnaki.findall('1.KRUPÓWKI. Główną arterią komunikacyjną miasta są drewniane zakopiańskie restauracje, kawiarnie, galerie sztuki i sklepy z pamiątkami.')
['1', '.', 'K', 'Ó', 'K', '.', '.']


>>> allZnaki = re.compile(r'[^KÓ2-5.]')
>>> allZnaki.findall('1.KRUPÓWKI. Główną arterią komunikacyjną miasta są drewniane zakopiańskie restauracje, kawiarnie, galerie sztuki i sklepy z pamiątkami.')
['1', 'R', 'U', 'P', 'W', 'I', ' ', 'G', 'ł', 'ó', 'w', 'n', 'ą', ' ', 
 'a', 'r', 't', 'e', 'r', 'i', 'ą', ' ', 'k', 'o', 'm', 'u', 'n', 'i', 
 'k', 'a', 'c', 'y', 'j', 'n', 'ą', ' ', 'm', 'i', 'a', 's', 't', 'a',
 ' ', 's', 'ą', ' ', 'd', 'r', 'e', 'w', 'n', 'i', 'a', 'n', 'e', ' ', 
 'z', 'a', 'k', 'o', 'p', 'i', 'a', 'ń', 's', 'k', 'i', 'e', ' ', 'r', 
 'e', 's', 't', 'a', 'u', 'r', 'a', 'c', 'j', 'e', ',', ' ', 'k', 'a',
 'w', 'i', 'a', 'r', 'n', 'i', 'e', ',', ' ', 'g', 'a', 'l', 'e', 'r',
 'i', 'e', ' ', 's', 'z', 't', 'u', 'k', 'i', ' ', 'i', ' ', 's', 'k', 
 'l', 'e', 'p', 'y', ' ', 'z', ' ', 'p', 'a', 'm', 'i', 'ą', 't', 'k', 'a', 'm', 'i']
>>> 

>>> beginWord = re.compile(r'^Zakopane')
>>> beginWord.search('Zakopane. Sprawdź, które atrakcje turyści wybierali najczęściej!')
<re.Match object; span=(0, 8), match='Zakopane'>

>>> endWord = re.compile(r'Zakopane$')
>>> endWord.search('Jakie są najlepsze aktywności na świeżym powietrzu w lokalizacji Zakopane')
<re.Match object; span=(65, 73), match='Zakopane'>
>>> endWord.search('Jakie są najlepsze aktywności na świeżym powietrzu w lokalizacji Zakopane?') == None
True
>>> 

>>> endPoint = re.compile(r'\d$')
>>> endPoint.search('12345667')
<re.Match object; span=(7, 8), match='7'>

>>> endPoint = re.compile(r'^\d+$')
>>> endPoint.search('12345667')
<re.Match object; span=(0, 8), match='12345667'>
>>> 

>>> import re
>>> ReWordy = re.compile(r'.to')
>>> ReWordy.findall('Co to? Kto to? Prosto.')
[' to', 'Kto', ' to', 'sto']
>>> ReWordy.findall('Co to? Kto to? Prosto tosty.')
[' to', 'Kto', ' to', 'sto', ' to']
>>> 
