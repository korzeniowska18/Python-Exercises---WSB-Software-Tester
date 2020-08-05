```
>>> suma = lambda x, y: x + y
>>> suma(5, 4)
9
>>> (lambda x: x * x)(3)
9
>>> (lambda x:(x % 2 and 'yes' or 'no'))(3)
'yes'

>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
6
```
```
suma = lambda x, y: x + y

x = int(input("Podaj pierwszą liczbę:"))
y = int(input("Podaj drugą liczbę:"))

print(suma(x, y))

Podaj liczbę:56
Podaj drugą liczbę:56
112
>>> 
```
