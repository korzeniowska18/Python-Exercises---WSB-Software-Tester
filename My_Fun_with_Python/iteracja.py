import itertools        

for x in itertools.count(50):
    print(x)
    if x == 60:
        break
        
for x in itertools.count(50, 5):
    print(x)
    if x == 60:
        break
        
x=0

for a in itertools.cycle("AUTOS"):
        print(a)
        x = x + 1
        if x > 50:
            break
            
x=0

for a in itertools.cycle([1, 2, 3, 4, 5]):
        print(a)
        x = x + 1
        if x > 50:
            break
            
for t in itertools.repeat(True):
    print(t)
    x = x+1
    if x > 60:
        break
"""
>>>
50
51
52
53
54
55
56
57
58
59
60

>>>
50
55
60
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A
U
T
O
S
A

>>>
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
>>>

True
True
True
True
True
True
True
True
True
True


"""
