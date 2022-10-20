from time import sleep
import sys

### slow spelling function, where:
### n = a word;
### t = the interval between the letters;

def spell(n,t): 
    for char in n:
        sleep(t)
        sys.stdout.write(char)


def pickNumbers(): #Pick how many number you'll use, and numbers.
    while True: #used to always insert a valid unit
        try:
            qtd = input("How many numbers will you sum? ")
            qtd = int(qtd)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        else:
            break

    for n in range(qtd):
        while True: #used to always insert a valid unit
            try: 
                print("Pick {}° number: ".format(len(numbersList)))
                n = int(input())
            except ValueError:
                print("Please enter a valid integer.")
                continue
            else:
                break

        numbersList.append(n) #add the number you picked to a list


def sumNumbers(): #Determine the sum of the numbers you picked
    sumNumbers = sum(numbersList)
    print("The sum of the chosen numbers is {}".format(sumNumbers))
    del(numbersList[0]) 
    print("Chosen numbers:" , numbersList)
