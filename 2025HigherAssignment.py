
from dataclasses import dataclass
@dataclass
class Customer:
    OrderNumber: str = ""
    Date: str = ""
    Email: str = ""
    Price: float = 0.0
    Rating: int = 0
    DeliveryType: str = ""  
    Month: str = ""



def ReadFromFileIntoArrayOfRecords():
    orders = []
    try:
        with open("orders.txt", "r") as file:
            for line in file:
                x = line.strip().split(",")
                print(x)
                if len(x) == 6:
                    order = Customer(
                        OrderNumber=x[0],
                        Date=x[1],
                        Email=x[2],
                        DeliveryType=x[3],
                        Price=float(x[4]),  # Fixed conversion
                        Rating=int(x[5])
                        
                    )

# Extract month from date format is YYYY/MM/DD                    
                    order.Month = x[1].split("-")[1]

                    orders.append(order)
# ensure the program doesn't show an error when run
    except FileNotFoundError:
        print("orders.txt file is not found.")
    return orders


# Function to find winning customer
def FindPositionOfCustomer(orders):
    position = -1
    index = 0
    month = input("Enter the month you would like to search for (MM): ")

    while position == -1 and index < len(orders):
        print(orders[index].Month)
        if (
            orders[index].Month == month
            and orders[index].Rating == 5
        ):
            position = index
        index += 1
    return position


# Function to write winner details
def WriteDetailsOfWinningCustomer(orders, position):
    with open("winningCustomer.txt", "w") as file:
        if position >= 0:
            winner = orders[position]
            file.write(f"Winning Order Number: {winner.OrderNumber}\n")
            file.write(f"Email: {winner.Email}\n")
            file.write(f"Cost: £{winner.Price:.2f}\n")
        else:
            file.write("No winner\n")


# Function to count delivery types
def CountOrders(orders):
    delivered = 0
    collected = 0

    for order in orders:
        if order.DeliveryType.lower() == "delivery":
            delivered += 1
        elif order.DeliveryType.lower() == "collection":
            collected += 1

    return delivered, collected


# Function to display totals
def DisplayTotalNumberOrdersDelivered(orders):
    delivered, collected = CountOrders(orders)

    print(f"Total number of orders delivered: {delivered}")
    print(f"Total number of orders collected: {collected}")


# MAIN PROGRAM - run the functions
orders = ReadFromFileIntoArrayOfRecords()
position = FindPositionOfCustomer(orders)
WriteDetailsOfWinningCustomer(orders, position)
DisplayTotalNumberOrdersDelivered(orders)