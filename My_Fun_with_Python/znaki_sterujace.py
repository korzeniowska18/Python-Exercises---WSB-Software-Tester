"""
\' = Apostrof
\" = Cudzysłów
\t = Tabulator
\n = Nowy wiersz(Enter)
\\ = Ukośnik
''' = potrójny apostrof

"r" przed ciągiem tekstowym "raw string" oznacza niezmodyfikowany ciąg tekstowy i wypisuje wszystkie znaki sterujące
"""

print('Jest to cytat:\n \n \"Jedynym sposobem na prawdziwą satysfakcję z pracy jest robienie tego,\
 w czego wielkość się wierzy. \n A jedynym sposobem na robienie rzeczy wielkich jest miłość do tego, co się robi.\"\n \n \t \t \\Steve Jobs\\')

"""
wynik:

>>>
Jest to cytat:
 
 "Jedynym sposobem na prawdziwą satysfakcję z pracy jest robienie tego,w czego wielkość się wierzy. 
 A jedynym sposobem na robienie rzeczy wielkich jest miłość do tego, co się robi."
 
 	 	 \Steve Jobs\
>>> 
"""

print(r'Jest to cytat:\n \n \"Jedynym sposobem na prawdziwą satysfakcję z pracy jest robienie tego,\
 w czego wielkość się wierzy. \n A jedynym sposobem na robienie rzeczy wielkich jest miłość do tego, co się robi.\"\n \n \t \t \\Steve Jobs\\')
 
 """
 wynik:

>>>
Jest to cytat:\n \n \"Jedynym sposobem na prawdziwą satysfakcję z pracy jest robienie tego,\
 w czego wielkość się wierzy. \n A jedynym sposobem na robienie rzeczy wielkich jest miłość do tego, co się robi.\"\n \n \t \t \\Steve Jobs\\

>>>
"""
 print('''Jest to cytat:

"Jedynym sposobem na prawdziwą satysfakcję z pracy jest robienie tego, w czego wielkość się wierzy.
A jedynym sposobem na robienie rzeczy wielkich jest miłość do tego, co się robi."

          \Steve Jobs\ ''')
 
 """
 wynik:
 
 >>>
 
 Jest to cytat:

"Jedynym sposobem na prawdziwą satysfakcję z pracy jest robienie tego, w czego wielkość się wierzy.
A jedynym sposobem na robienie rzeczy wielkich jest miłość do tego, co się robi."

          \Steve Jobs\ 
>>> 
"""
