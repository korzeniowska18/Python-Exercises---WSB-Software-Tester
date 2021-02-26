#Zasada: tworząc nową linijkę, dodajemy jedynki jako piewrszy i ostatni element, każdy ze środkowych elemntów jako suma dwóch srodkowych elementów

>>>>

width = 60
height = 7

numbers = [1]

line = " "

for n in numbers:
    line+= "%3d " % (n)
print(line.center(width))

for i in range(height-1):
    newNumbers = [1]
    
    position = 0

    while position < len(numbers) - 1:
        newNumbers.append(numbers[position] + numbers[position] + 1)
        position +=1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    line = ' '
    for n in numbers:
        line+= "%3d " % (n)
        

    print(line.center(width))
    
    >>>>
    
                              1                             
                            1   1                           
                          1   3   1                         
                        1   3   7   1                       
                      1   3   7  15   1                     
                    1   3   7  15  31   1                   
                  1   3   7  15  31  63   1                 
>>> 

width = 60
height = 12     #zmieniona wysokość na 12

numbers = [1]

line = " "

for n in numbers:
    line+= "%3d " % (n)
print(line.center(width))

for i in range(height-1):
    newNumbers = [1]
    
    position = 0

    while position < len(numbers) - 1:
        newNumbers.append(numbers[position] + numbers[position] + 1)
        position +=1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    line = ' '
    for n in numbers:
        line+= "%3d " % (n)
        

    print(line.center(width))
    
>>>

                              1                             
                            1   1                           
                          1   3   1                         
                        1   3   7   1                       
                      1   3   7  15   1                     
                    1   3   7  15  31   1                   
                  1   3   7  15  31  63   1                 
                1   3   7  15  31  63 127   1               
              1   3   7  15  31  63 127 255   1             
            1   3   7  15  31  63 127 255 511   1           
          1   3   7  15  31  63 127 255 511 1023   1        
       1   3   7  15  31  63 127 255 511 1023 2047   1      
>>> 

numbers = [1]

print(numbers)

for i in range(5):
    newNumbers = [1]
    
    position = 0

    while position < len(numbers) - 1:
        newNumbers.append(numbers[position] + numbers[position] + 1)
        position +=1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    print(numbers)
        
      
>>>>

[1]
[1, 1]
[1, 3, 1]
[1, 3, 7, 1]
[1, 3, 7, 15, 1]
[1, 3, 7, 15, 31, 1]
>>> 
