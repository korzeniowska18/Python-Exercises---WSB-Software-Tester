>>> from math import *
>>> floor(pi)
3
>>> 
>>> 
================================ RESTART: Shell ================================
>>> import math
>>> math.floor(math.pi)
3
>>> 
================================ RESTART: Shell ================================
>>> from math import floor
>>> floor(pi)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    floor(pi)
NameError: name 'pi' is not defined
>>> from math import pi
>>> pi
3.141592653589793
>>> from math import floor
>>> floor(pi)
3
>>> 

import statistics


percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
percent.sort()

print(percent)
print('\n')
 
print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))

>>>
[0.781876504, 0.922213312, 0.962309543, 1.222935044, 1.283079391, 1.864474739, 1.984763432, 2.265437049, 
 2.425821973, 2.606255012, 2.726543705, 2.886928629, 3.327987169, 3.468323978, 3.628708901, 3.688853248,
 4.190056135, 4.530874098, 4.911788292, 5.493183641, 5.633520449, 6.174819567, 6.816359262, 6.856455493,
 8.740978348, 10.60545309]


3.3981555735
3.327987169
3.468323978
>>> 

import math
 
degree = 360
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
 
degree = 45
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
print('')
 
print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')
      
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
 
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00
 
small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2
 
print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)      
print('')
print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)
print('')
      
math_ls = dir(math) 
print(math_ls)

>>>
360 degree is 6.283185 radians
45 degree is 0.785398 radians

360 degree is 6.283185 radians
45 degree is 0.785398 radians

small 0.22 11.5 0.152053084433746
big 0.27 15.6 0.22902210444669593
family 0.38 22.0 0.45364597917836613

small 75.63148122135523
big 68.115695808877
family 48.49596603908168

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin',
 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf',
 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 
 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 
 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt',
 'tan', 'tanh', 'tau', 'trunc']

>>> 
