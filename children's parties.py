adult_no = int(input("Enter the number of adults: "))
child_no = int(input("Enter the number of children: "))
total_people = adult_no + child_no
total_cost = 0
if total_people > 20:
    total_cost = total_cost + 50 

for x in range(total_people):
    y = input("Any diatry requirements?")

child_price = 2 * child_no
cake = input("Is cake needed?: ")
if cake == "yes":
    total_cost = total_cost + 10

total_cost = total_cost + child_price
print("Your total cost comes to: £", total_cost)
    

