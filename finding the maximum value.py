# 1001Task6.py
# Standard Algorithms - Finding Min + Max

from random import *

numbers = []

def random20numbers():
    for x in range(20):
        numbers.append(randrange(1, 51))
    return numbers

def displayNumbers(numbers):
    for x in range(20):
        print(numbers[x], " ", end="")
    print()  # Move to a new line after displaying all numbers

def findingMax(numbers):
    # Find the maximum manually (without using max() built-in)
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("The highest number (maximum) in the list is", maximum, ".")

numbers = random20numbers()
displayNumbers(numbers)
findingMax(numbers)
