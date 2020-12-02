# %y %Y - rok, %a %A - dzień tygodnia, %b %B - miesiąc, %d - dzień miesiąca

from datetime import datetime
from datetime import date
from datetime import time

def main():
    obecny_czas = datetime.now()
    print(obecny_czas.strftime("Obecnie jest %Y rok"))

if __name__ == "__main__":
    main()

>>> Obecnie jest 2020 rok

