from random import randint

def return_birthday():
    # Returns a number between 1-365
    n = randint(1, 365)
    return n

def main():
    iterations = []
    for x in range(100000):
        it = 1
        arr = []
        for n in range(23):
            b = return_birthday()
            arr.append(b)

        if len(arr) == len(set(arr)):
            iterations.append(it)
        else:
            it += 1
    
    print(f"Chance of the same birthday in a group of 23 people was {(sum(iterations)/100000)*100}%. The group of 23 people was ran 100000 iterations")
    
    return

while True:
    main()