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
