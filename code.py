def findMaxPos(array):
    maxPos = 0
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] > maxValue:
            maxValue = array[i]
            maxPos = i
    return maxPos

def readData(filename):
    companies, employees, salaries = [], [], []
    with open(filename, "r") as file:
        for line in file:
            name, numEmp, ceoSal = line.strip().split(",")
            companies.append(name.strip())
            employees.append(int(numEmp))
            salaries.append(int(ceoSal))
    return companies, employees, salaries

def salaryDifference(companies, salaries):
    chosen = input("Enter the name of the company you would like to check: ")
    maxPos = findMaxPos(salaries)
    found = False
    for i in range(len(companies)):
        if companies[i].lower() == chosen.lower():
            found = True
            diff = salaries[maxPos] - salaries[i]
            print(f"{companies[maxPos]} company has the highest paid CEO.")
            print(f"The {companies[i]} CEO earns £{diff} less than the highest paid CEO.")
    if not found:
        print("Company not found")

def employeeStats(companies, employees):
    maxPos = findMaxPos(employees)
    maxEmp = employees[maxPos]
    count = 0
    for emp in employees:
        if emp >= maxEmp * 0.9:
            count += 1
    print(f"The highest number of employees employed by a single company is {maxEmp}.")
    print(f"{count} companies employ within 10% of {maxEmp}.")

companies, employees, salaries = readData("C:/Users/SwastikaRath/Desktop/SQA comp sci ASSIGNMENTS/2024/companies.csv")
salaryDifference(companies, salaries)
employeeStats(companies, employees)
