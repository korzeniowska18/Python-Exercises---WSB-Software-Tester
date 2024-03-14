#!usr/bin/python
#! -*- coding: utf-8 -*-

#Sito Eratostenesa - liczby pierwsze nie większe od n
# liczby pierwsze <= n
#p*p, p*(p+1), p*(p+2),...

def sito(n):                  

    
    L = [0] + n * [1]
    for p in range(2, n):     
        q = p * p
        if q > n:
            break
        if L[p] == 1:         
                               
            for i in range(q, n+1, p):
                L[i] = 0
    return [i for i in range(1, n+1) if L[i]==1]
