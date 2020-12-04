#jak wywołąć parametru scryptu podane w Configuration w programie

import sys

print("Liczba podanych argumentow: ", len(sys.argv), " argument.")
print("Argumenty ", sys.argv)

sys.argv.remove(sys.argv[0])

print("Argumenty", sys.argv)

argumenty = sys.argv
razem = 0

for a in argumenty:
    try:
        liczba = int(a)
        razem = razem + liczba
    except Exception:
        print("Niewłaściwy input")
        
print(razem)       

"""
>>>
Liczba podanych argumentow:  1  argument.
Argumenty  ['parametry_skryptu.py']
Argumenty []
0

>>>
#argumenty można podać wywołując skrypt

python parametry_skryptu.py 4 2 3
Liczba podanych argumentow:  4  argument.
Argumenty  ['parametry_skryptu.py', '4', '2', '3']
Argumenty ['4', '2', '3']
9

"""

