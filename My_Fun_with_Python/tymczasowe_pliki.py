import tempfile

tempPlik = tempfile.TemporaryFile()

tempPlik.write(b"Zachowaj tymczasowo password: 373201010")

tempPlik.seek(0)

print(tempPlik.read())

tempPlik.close()

"""
>>>
b'Zachowaj tymczasowo password: 373201010'
>>>
"""
