Errors:
```
NameError

t[5]

This is because the name ‘t’ is not defined.
```
```
IndexError

lst = [1, 2, 3]
lst[3]

This is because the index of the list given in the code, that is, 3 is out of range.
```
```
TypeError

4 + '3'

This is because the operand ‘+’ is not supported when we combine the data types ‘int’ and ‘str’.
```
```
ValueError

int('65.43')

This is because there is an invalid literal for int() with base 10: ’65.43’.
```
```
ValueError, NameError   (entered value = -6)

CODE 1
import math
num=int(input("Enter a number of whose factorial you want to find"))
print(math.factorial(num))

ValueError: factorial() not defined for negative values
 
CODE 2
num=int(input("Enter a number of whose factorial you want to find"))
print(math.factorial(num))

NameError: name 'math' is not defined
```
```
SemanticError

Print(“Good Morning”)

SyntaxError - Syntax errors are also known as parsing errors

print(“Good night)
```
```
IOError - exceptions are raised as a result of an error in opening a particular file.

multiple exception - except TypeError, SyntaxError [,…] 
```
