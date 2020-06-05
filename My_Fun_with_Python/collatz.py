print("This is Collatz program")

inputNumber = int(input("Podaj liczbę całkowitą: "))

def collatz(number):
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)

        else:
            number = number *3 + 1
            print(number)


collatz(inputNumber)
