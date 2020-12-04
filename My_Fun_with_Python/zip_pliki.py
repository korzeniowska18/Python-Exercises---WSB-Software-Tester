import zipfile

zip = zipfile.ZipFile("przykladowy1.zip", "r")

print(zip.namelist())

for data in zip.infolist():
    print(data)
    
informacja = zip.getinfo("przykladowy1.txt")
print(informacja)

print(zip.read("przykladowy2.txt"))
with zip.open("przykladowy2.txt") as p:
    print(p.read())                       #wypisuje zawartość pliku, czyta

#wypakowanie pliku zip, extract

#zip.extract("przykladowy2.txt")
zip.extractall()    #konwertuje wszystkie pliki zip w tej dyrektorji
zip.close()
 
 
"""
>>>
['przykladowy1.txt', 'przykladowy2.txt']
<ZipInfo filename='przykladowy1.txt' filemode='-rw-rw-r--' external_attr=0x8020 file_size=22>
<ZipInfo filename='przykladowy2.txt' compress_type=deflate filemode='-rw-rw-r--' external_attr=0x8020 file_size=9 compress_size=8>

>>>

<ZipInfo filename='przykladowy1.txt' filemode='-rw-rw-r--' external_attr=0x8020 file_size=22>

>>>

<ZipInfo filename='przykladowy1.txt' filemode='-rw-rw-r--' external_attr=0x8020 file_size=22>
b'tra la la'

>>>
b'tra la la'

"""
