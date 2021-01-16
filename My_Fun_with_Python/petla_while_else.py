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
