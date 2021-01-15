>>> a = ['kotek', 'lisek', 'piesek']
>>> a[0] = 'kotek biały'
>>> print(a)
['kotek biały', 'lisek', 'piesek']   => nadpisanie zmiennej
>>> 

>>> liczby = [1, 3, 5, 6]
>>> print(liczby)
[1, 3, 5, 6]
>>> print(type(liczby))
<class 'list'>
>>> 

>>> difference = ['kotek', 'lisek', 'piesek', 1, 3, 5, 6]
>>> print(difference)
['kotek', 'lisek', 'piesek', 1, 3, 5, 6]
>>> 

>>> listy = [[1, 3, 5, 6], ['kotek biały', 'lisek', 'piesek'], 8]    => listy zagniezdżone
>>> print(listy)
[[1, 3, 5, 6], ['kotek biały', 'lisek', 'piesek'], 8]
>>> print(len(listy))
3
>>> 

>>> a = [1, 3, 5, 7]
>>> b = [7, 3, 2, 'apple']
>>> c = [a, b]
>>> print(c)
[[1, 3, 5, 7], [7, 3, 2, 'apple']]
>>> d = a + b
>>> print(d)
[1, 3, 5, 7, 7, 3, 2, 'apple']
>>> 

>>> print(len(c))
2
>>> print(len(d))
8
>>> 

>>> d += ['orange']
>>> print(d)
[1, 3, 5, 7, 7, 3, 2, 'apple', 'orange']
>>> 

>>> print(dir(list))
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__','__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 

>>> a = [1, 3, 5, 7, 7, 3, 2, 'apple', 'orange']
>>> a[1] = 10
>>> a
[1, 10, 5, 7, 7, 3, 2, 'apple', 'orange']
>>> a.append('fruits')
>>> a
[1, 10, 5, 7, 7, 3, 2, 'apple', 'orange', 'fruits']
>>> a.insert(6, 22)
>>> a
[1, 10, 5, 7, 7, 3, 22, 2, 'apple', 'orange', 'fruits']
>>> a.remove([3])
>>> a.remove(7)
>>> a
[1, 10, 5, 7, 3, 22, 2, 'apple', 'orange', 'fruits']

>>> a
[1, 2, 3, 5, 7, 10, 22, 'apple', 'orange', 'fruits']
>>> a
[1, 2, 3, 5, 7, 10, 22, 'apple', 'orange', 'fruits']
>>> a
[1, 2, 3, 5, 7, 10, 22, 'apple', 'orange', 'fruits']
>>> a
[1, 2, 3, 5, 7, 10, 22, 'apple', 'orange', 'fruits']
a
>>> 
>>> a
[1, 2, 3, 5, 7, 10, 22, 'apple', 'orange', 'fruits']
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a = 'apple', 'orange', 'fruits']
SyntaxError: unmatched ']'
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a = ['apple', 'orange', 'fruits']
>>> a.sort()
>>> a
['apple', 'fruits', 'orange']
>>> b = [1, 2, 3, 5, 7, 10, 22]
>>> b.sort()
>>> b
[1, 2, 3, 5, 7, 10, 22]
>>> sorted(b)
[1, 2, 3, 5, 7, 10, 22]
>>> b
[1, 2, 3, 5, 7, 10, 22]
>>> b.reverse()
>>> b
[22, 10, 7, 5, 3, 2, 1]
>>> b
[22, 10, 7, 5, 3, 2, 1]
>>> sorted(b)
[1, 2, 3, 5, 7, 10, 22]
>>> b
[22, 10, 7, 5, 3, 2, 1]
>>> a.index('apple')
0
>>> a.append(10)
>>> a
['apple', 'fruits', 'orange', 10]
>>> b.append(10)
>>> b
[22, 10, 7, 5, 3, 2, 1, 10]
>>> b.count(10)
2
>>> a.extend(b)
>>> a
['apple', 'fruits', 'orange', 10, 22, 10, 7, 5, 3, 2, 1, 10]
>>> a = b
>>> a
[22, 10, 7, 5, 3, 2, 1, 10]
>>> b
[22, 10, 7, 5, 3, 2, 1, 10]
>>> a.extend(b)
>>> a
[22, 10, 7, 5, 3, 2, 1, 10, 22, 10, 7, 5, 3, 2, 1, 10]
>>> b = a
>>> a
[22, 10, 7, 5, 3, 2, 1, 10, 22, 10, 7, 5, 3, 2, 1, 10]
>>> b
[22, 10, 7, 5, 3, 2, 1, 10, 22, 10, 7, 5, 3, 2, 1, 10]
>>> b.clear()
>>> b
[]
>>> a
[]
>>> a = [22, 10, 7, 5, 3, 2, 1, 10, 22, 10, 7, 5, 3, 2, 1, 10]
>>> b = a.copy()
>>> b
[22, 10, 7, 5, 3, 2, 1, 10, 22, 10, 7, 5, 3, 2, 1, 10]
>>> b.clear()
>>> b
[]
>>> a
[22, 10, 7, 5, 3, 2, 1, 10, 22, 10, 7, 5, 3, 2, 1, 10]

