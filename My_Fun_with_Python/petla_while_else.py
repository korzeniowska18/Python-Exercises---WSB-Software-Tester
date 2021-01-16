a = 1
amax = 10

while a <= amax:
    print("This is Ok")
    a +=1                   => jeśli zapomnimy zaimplementować to, wtedy pętla wykonuje się w nieskończonność
    
>>>
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
>>>

a = 1
amax = 10

while a <= amax:
    print("This is Ok")
    a +=1
else:
    print("Now a = ", a)
    
>>>
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
Now a =  11
>>>

a = 1
amax = 10

while a <= amax:
    print(a, "This is Ok")
    a +=1
else:
    print("Now a = ", a)
   
   
>>>
1 This is Ok
2 This is Ok
3 This is Ok
4 This is Ok
5 This is Ok
6 This is Ok
7 This is Ok
8 This is Ok
9 This is Ok
10 This is Ok
Now a =  11
>>>

a = 1
amax = 10

while a <= amax:
    print(a, "This is Ok")
    a +=2
else:
    print("Now a = ", a)
    
>>>
1 This is Ok
3 This is Ok
5 This is Ok
7 This is Ok
9 This is Ok
Now a =  11
>>>

a = 10
amin = 0

while a >= amin:
    print(a, "This is Ok")
    a -=2
else:
    print("Now a = ", a)
>>>
10 This is Ok
8 This is Ok
6 This is Ok
4 This is Ok
2 This is Ok
0 This is Ok
Now a =  -2
>>>

line = 1

lastLinie = 10

number = line

while number <= lastLinie:
    print(number*'x')
    number +=1
    
>>>
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx
xxxxxxxxxx
>>>

a = 0
b = 16

while a <= b:
    print("Dwa do potęgi ", a, "wynosi ", 2 ** a)
    a +=1

>>>
Dwa do potęgi  0 wynosi  1
Dwa do potęgi  1 wynosi  2
Dwa do potęgi  2 wynosi  4
Dwa do potęgi  3 wynosi  8
Dwa do potęgi  4 wynosi  16
Dwa do potęgi  5 wynosi  32
Dwa do potęgi  6 wynosi  64
Dwa do potęgi  7 wynosi  128
Dwa do potęgi  8 wynosi  256
Dwa do potęgi  9 wynosi  512
Dwa do potęgi  10 wynosi  1024
Dwa do potęgi  11 wynosi  2048
Dwa do potęgi  12 wynosi  4096
Dwa do potęgi  13 wynosi  8192
Dwa do potęgi  14 wynosi  16384
Dwa do potęgi  15 wynosi  32768
Dwa do potęgi  16 wynosi  65536

>>>
