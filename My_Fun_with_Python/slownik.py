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
