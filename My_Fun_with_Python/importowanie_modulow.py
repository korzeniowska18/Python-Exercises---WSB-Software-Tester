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
