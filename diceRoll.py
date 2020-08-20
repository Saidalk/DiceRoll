import random
def Main():
    Input = int(input("how many rolls would you like?\n"))
    print("Your rolls:")
    Roll(Input)

def Roll(Input):
    n = 0
    while n < Input:
        print(random.randint(1,6))
        n += 1


Main()