# Create a program that asks the user to input 5 test scores and calculates the running total after each input.
total = 0
for index in range(5):
    test = int(input("enter your score as a number out of 100: "))
    total = test + total
    print(total)

total * 0.2
print("your average mark was: ", total * 0.2)
