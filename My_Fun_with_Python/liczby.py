>>> liczba = 4.16273788888
>>> print(liczba)
4.16273788888
>>> print(int(liczba))
4
>>> print(abs(-liczba))
4.16273788888
>>> liczba_wieksza = 5.1627281
>>> print(max(liczba_wieksza, liczba))
5.1627281
>>> print(min(liczba_wieksza, liczba))
4.16273788888
>>> print(round(liczba_wieksza))
5
>>> print(round(liczba_wieksza, 2))
5.16
>>> print(round(liczba_wieksza, 3))
5.163
>>> print(round(liczba_wieksza, 4))
5.1627
>>> print(round(liczba_wieksza, 5))
5.16273
>>> print(round(liczba_wieksza, 6))
5.162728
>>> lista = [1, 56, 23]
>>> print(sum(lista))
80
>>> print(len(lista))
3
>>> >>> percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
>>> print(sum(percent))
100.00000000399999
>>> >>> print(min(percent))
0.781876504
>>> print(max(percent))
10.60545309

countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']

sumOfPoints = 4988

for i in range(len(countries)):
 
    print(percent[i], int(percent[i]), round(percent[i],2), int(round(percent[i]*sumOfPoints/100,0)), countries[i])
  
>>>
2.606255012 2 2.61 130 Ukraine
1.222935044 1 1.22 61 Spain
1.283079391 1 1.28 64 Slovenia
3.628708901 3 3.63 181 Lithuania
6.856455493 6 6.86 342 Austria
4.911788292 4 4.91 245 Estonia
2.886928629 2 2.89 144 Norway
0.781876504 0 0.78 39 Portugal
0.962309543 0 0.96 48 United Kingdom
2.265437049 2 2.27 113 Serbia
6.816359262 6 6.82 340 Germany
3.688853248 3 3.69 184 Albania
3.468323978 3 3.47 173 France
5.633520449 5 5.63 281 Czech Republic
4.530874098 4 4.53 226 Denmark
1.984763432 1 1.98 99 Australia
0.922213312 0 0.92 46 Finland
3.327987169 3 3.33 166 Bulgaria
4.190056135 4 4.19 209 Moldova
5.493183641 5 5.49 274 Sweden
1.864474739 1 1.86 93 Hungary
10.60545309 10 10.61 529 Israel
2.425821973 2 2.43 121 Netherlands
2.726543705 2 2.73 136 Ireland
8.740978348 8 8.74 436 Cyprus
6.174819567 6 6.17 308 Italy
>>> 
