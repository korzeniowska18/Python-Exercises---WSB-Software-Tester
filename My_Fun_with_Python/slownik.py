#słownik i metody słownikowe: keys(), values(), items()

slownik = {'Ojczyzna': 'das Heimatland', 'zawód': 'der Beruf',
           'dyspozycja': 'das Verfügung', 'gospodarka': 'der Wirtschaft'}

print('Jakie słowa są w twoim słowniku z języka niemieckiego:')
print('\n')

for k in slownik.keys():
    print('' + k)

print('\n')


print('Jakich słów nauczyłeś się w języku niemieckim:')
print('\n')

for v in slownik.values():
    print('' + v)
    
print('\n')
print('Podaj zawartoś twojego słownika z języka niemieckiego z tłumaczeniem:')
print('\n')

for i in slownik.items():
    print(*list(i),sep=' : ')
    
print('\n')
print('Zawartość słownika:')

for k, v in slownik.items():
    print(f'słowo w języku polskim: {k}, tłumaczenie na język niemiecki: {str(v)}')
    
#Wynik:

Jakie słowa są w twoim słowniku z języka niemieckiego:


Ojczyzna
zawód
dyspozycja
gospodarka


Jakich słów nauczyłeś się w języku niemieckim:


das Heimatland
der Beruf
das Verfügung
der Wirtschaft


Podaj zawartoś twojego słownika z języka niemieckiego z tłumaczeniem:


Ojczyzna : das Heimatland
zawód : der Beruf
dyspozycja : das Verfügung
gospodarka : der Wirtschaft


Zawartość słownika:
słowo w języku polskim: Ojczyzna, tłumaczenie na język niemiecki: das Heimatland
słowo w języku polskim: zawód, tłumaczenie na język niemiecki: der Beruf
słowo w języku polskim: dyspozycja, tłumaczenie na język niemiecki: das Verfügung
słowo w języku polskim: gospodarka, tłumaczenie na język niemiecki: der Wirtschaft

>>> autos = {'Ford': 2017, 'Audi': 2015, 'BMW': 2016}
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2016}
>>> autos['Opel'] = 2018
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2016, 'Opel': 2018}
>>> autos.keys()
dict_keys(['Ford', 'Audi', 'BMW', 'Opel'])
>>> autos.values()
dict_values([2017, 2015, 2016, 2018])
>>> autos.items()
dict_items([('Ford', 2017), ('Audi', 2015), ('BMW', 2016), ('Opel', 2018)])
>>> autos('Ford')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    autos('Ford')
TypeError: 'dict' object is not callable
>>> autos['Ford']
2017
>>> autos.popitem()
('Opel', 2018)
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2016}
>>> autos.setdefault('BMW', 2020)
2016
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2016}

>>> autos.setdefault('Mitsubishi', 2010)    => setdefault tylko dla items które nie znajdują się jeszcze w dictionary
2010
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2016, 'Mitsubishi': 2010}
>>> autos.get('Dacia')
>>> print(autos.get('Dacia'))
None
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2016, 'Mitsubishi': 2010}
>>> NewAutos = {'BMW': 2021, 'Fiat': 2021}
>>> autos.update(NewAutos)
>>> autos
{'Ford': 2017, 'Audi': 2015, 'BMW': 2021, 'Mitsubishi': 2010, 'Fiat': 2021}
>>> 
