>>> auta = ('Ford', 'Opel', 'Audi', 'BMW')
>>> rocznik = (2015, 2017, 2018, 2010)

>>> info = (auta, rocznik)

>>> info
(('Ford', 'Opel', 'Audi', 'BMW'), (2015, 2017, 2018, 2010))
>>> sale_auto = auta[0], rocznik[0]
>>> print(sale_auto)
('Ford', 2015)
>>> 

>>> imie, nazwisko, ID = ('Lena', 'Nowak', '888')
>>> imie, nazwisko, ID
('Lena', 'Nowak', '888')
>>> imie
'Lena'
>>> ID
'888'
>>> 

>>> auto = ('Ford', '2015', 'red', '1 owner')   =. rozpakowanie krotki "auto"
>>> model, rocznik, kolor, wlasciciel = auto
>>> print(model, rocznik, kolor, wlasciciel)
Ford 2015 red 1 owner
>>> print(auto)
('Ford', '2015', 'red', '1 owner')
>>> 
>>> model
'Ford'
>>> kolor
'red'
>>> 

>>> autos = 'Ford', 'Opel', 'Audi', 'BMW'
>>> print(type(autos))
<class 'tuple'>
>>> 

>>> transport = ('Samolot', 'Auto', ('BMW', 'Ford'))
>>> print(transport)
('Samolot', 'Auto', ('BMW', 'Ford'))                  => zagniezdżona krotka
>>> 

>>> a, b = 14, 18    => zamiana wartości zmiennych
>>> a, b = b, a
>>> print(a, b)
18 14
>>> 
>>> x = (55, 3, 6, 1, 9, 11)
>>> x[-1]
11
>>> x.index(55)
0
>>> x.count(11)
1
>>> max(x)
55
>>> x
(55, 3, 6, 1, 9, 11)
>>> list(x)
[55, 3, 6, 1, 9, 11]
>>> x
(55, 3, 6, 1, 9, 11)
>>> x.append(50)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x.append(50)
AttributeError: 'tuple' object has no attribute 'append'
>>> y = list(x)
>>> y
[55, 3, 6, 1, 9, 11]
>>> y.append(50)
>>> y
[55, 3, 6, 1, 9, 11, 50]
>>> x = tuple(y)
>>> x
(55, 3, 6, 1, 9, 11, 50)
>>> (g1, g2, g3, g4) = x
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    (g1, g2, g3, g4) = x
ValueError: too many values to unpack (expected 4)
>>> d = 1
>>> c =10
>>> print("d =",d,"\tc",c)
d = 1 	c 10
>>> print("d =",d,"\tc =",c)
d = 1 	c = 10
>>> (d,c) = (c,d)
>>> print("d =",d,"\tc =",c)
d = 10 	c = 1
