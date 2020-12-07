import os
from pathlib import Path

ALL = {
    "DOKUMENTY": ['.txt', '.doc', '.pdf'],
    "MUZYKA": ['.m4a', '.m4b', '.mp3'],
    "FILMY": ['.mov', '.avi', '.mp4'],
    "OBRAZY": ['.jpg', '.png', '.jpeg']
}

def pobrac_dyrektorie(value):
    for category, suffixes in ALL.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MIX'
                
print(pobrac_dyrektorie('.jpg'))
                
info_o_dyrektorii =(input("Wpisz format, aby otrzymać informacje o dyrektorii: "))

print("Jest to dyrektoria: ", pobrac_dyrektorie(info_o_dyrektorii))

def uporzadkowanie_dyrektorii():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        dyrektoria = pobrac_dyrektorie(filetype)
        dyrektoriaPath = Path(dyrektoria)
        if dyrektoriaPath.is_dir() != True:
            dyrektoriaPath.mkdir()
        filePath.rename(dyrektoriaPath.joinpath(filePath))
        
uporzadkowanie_dyrektorii()

"""
>>>

OBRAZY
Wpisz format, aby otrzymać informacje o dyrektorii: .mp4
Jest to dyrektoria:  FILMY

>>> # w ten sposób wszystkie pliki są posegregowane, a pliki poza zakresem podanych są w folderze "MIX"
$ ls
DOKUMENTY/  MIX/


"""
