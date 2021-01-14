# w zbiorach nie ma znaczenia kolejność, tylko czy jest ta wartość w zbiorze czy nie

>>> fruits = {'apple', 'orange', 'watermelon', 'pear'}
>>> fruits
{'pear', 'watermelon', 'apple', 'orange'}

>>> print(type(fruits))
<class 'set'>                  => set (zbiór)
>>> 

>>> print(len(fruits))
4                              => zbiór składa się z 4 elementów
>>> 

>>> set('Travel')
{'e', 'v', 'r', 'T', 'l', 'a'}

>>> set('Koooooteek')
{'t', 'e', 'K', 'o', 'k'}
>>> 

>>> 'apple' in fruits
True
>>> 

>>> print(dir(set))
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', 
'__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
'__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__',
'__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear',
'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 

>>> fruits.add('pomegranate')
>>> fruits
{'pomegranate', 'pear', 'orange', 'watermelon', 'apple'}
>>> 

>>> fruits.remove('pear')
>>> fruits
{'pomegranate', 'orange', 'watermelon', 'apple'}
>>> 

>>> fruits.pop()          => metoda pop usuwa dowolny element ze zbioru i zwraca ten element
'pomegranate'
>>> fruits.pop()
'orange'
>>> fruits.pop()
'watermelon'
>>> fruits.pop()
'apple'
>>> fruits.pop()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    fruits.pop()
KeyError: 'pop from an empty set'
>>> 

>>> fruits = {'apple', 'orange', 'watermelon', 'pear'}
>>> fruits.clear()
>>> fruits
set()
>>> 

>>> A = {5, 7, 8, 9, 10}
>>> B = {8, 9, 10, 11}
>>> C = {8, 9}
>>> 
>>> C.issubset(A)
True
>>> C.issubset({8, 10})    
False
>>> A.issuperset(C)    => czy zbiór A jest nadrzędnym zbiorem w stosunku do C (czyli zawiera te same elementy)
True
>>> A.union(B)                 => łączenie zbiorów, te same wartości zapisane są pojedyńczo
{5, 7, 8, 9, 10, 11}
>>> 

>>> A.intersection(B)   => wypisuje wartości które występują w jednym i drigim zbiorze
{8, 9, 10}
>>> 

>>> A.symmetric_difference(B)   => wypisuje pozostałe elementy, które są w zbiorach, pomijając elementy, które występują w jednym i drugim
{5, 7, 11}
>>> 

>>> D = A.copy()
>>> D
{5, 7, 8, 9, 10}
>>> 
