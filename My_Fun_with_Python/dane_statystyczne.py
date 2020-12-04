#mean-average - średnia
#median - midpoint - punkt średni
#mode - najczęściej występująca  
#variance - lista [3, 3, 4] =  variance = ((3 - 3,33)2 + (3 - 3,33)2 + (4 - 3,33)2 / (3 - 1) = 1/3
#1/3 = .57735
#statistic deviation - stdev



import statistics
import math

punkty = [5, 7, 3, 9, 7, 7, 8, 4, 10]

print(statistics.mean(punkty))
print(statistics.median(punkty))
print(statistics.mode(punkty))
print(sorted(punkty))
print(sorted(punkty, reverse=True))
a = [3, 3, 4]
print(statistics.variance(a))
print(statistics.stdev(a))
print(math.sqrt(statistics.variance(a)))
"""
>>>
6.666666666666667
7
7

>>>

[3, 4, 5, 7, 7, 7, 8, 9, 10]
[10, 9, 8, 7, 7, 7, 5, 4, 3]

>>>

0.3333333333333333

>>>
0.5773502691896257

>>>
0.5773502691896257


"""
