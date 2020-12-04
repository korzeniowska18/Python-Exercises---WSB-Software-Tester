#permutations - te same dane w innej kolejności
#combinations - nie używamy jeśli mamy takie same elementy jak inne, podczas dopasowania nie używa takich samych elementów

import itertools 

lista_gosci = {1: "Kleo", 2: "Leo", 3: "Marco", 4: "Nata"}
for g in itertools.permutations(lista_gosci):
    print(g)
    
for g1 in itertools.permutations(lista_gosci.values()):
    print(g1)
    
kwiaty = ["stokrotka", "lawenda", "azalja", "tulipan", "lilia"]

for k in itertools.combinations(kwiaty, 2):  #liczba oznacza ile elementów będzie w każdej dopasowanej grupie
    print(k)
    

    
"""
>>>
(1, 2, 3, 4)
(1, 2, 4, 3)
(1, 3, 2, 4)
(1, 3, 4, 2)
(1, 4, 2, 3)
(1, 4, 3, 2)
(2, 1, 3, 4)
(2, 1, 4, 3)
(2, 3, 1, 4)
(2, 3, 4, 1)
(2, 4, 1, 3)
(2, 4, 3, 1)
(3, 1, 2, 4)
(3, 1, 4, 2)
(3, 2, 1, 4)
(3, 2, 4, 1)
(3, 4, 1, 2)
(3, 4, 2, 1)
(4, 1, 2, 3)
(4, 1, 3, 2)
(4, 2, 1, 3)
(4, 2, 3, 1)
(4, 3, 1, 2)
(4, 3, 2, 1)

>>>

('Kleo', 'Leo', 'Marco', 'Nata')
('Kleo', 'Leo', 'Nata', 'Marco')
('Kleo', 'Marco', 'Leo', 'Nata')
('Kleo', 'Marco', 'Nata', 'Leo')
('Kleo', 'Nata', 'Leo', 'Marco')
('Kleo', 'Nata', 'Marco', 'Leo')
('Leo', 'Kleo', 'Marco', 'Nata')
('Leo', 'Kleo', 'Nata', 'Marco')
('Leo', 'Marco', 'Kleo', 'Nata')
('Leo', 'Marco', 'Nata', 'Kleo')
('Leo', 'Nata', 'Kleo', 'Marco')
('Leo', 'Nata', 'Marco', 'Kleo')
('Marco', 'Kleo', 'Leo', 'Nata')
('Marco', 'Kleo', 'Nata', 'Leo')
('Marco', 'Leo', 'Kleo', 'Nata')
('Marco', 'Leo', 'Nata', 'Kleo')
('Marco', 'Nata', 'Kleo', 'Leo')
('Marco', 'Nata', 'Leo', 'Kleo')
('Nata', 'Kleo', 'Leo', 'Marco')
('Nata', 'Kleo', 'Marco', 'Leo')
('Nata', 'Leo', 'Kleo', 'Marco')
('Nata', 'Leo', 'Marco', 'Kleo')
('Nata', 'Marco', 'Kleo', 'Leo')

>>>

('stokrotka', 'lawenda')
('stokrotka', 'azalja')
('stokrotka', 'tulipan')
('stokrotka', 'lilia')
('lawenda', 'azalja')
('lawenda', 'tulipan')
('lawenda', 'lilia')
('azalja', 'tulipan')
('azalja', 'lilia')
('tulipan', 'lilia')


"""
