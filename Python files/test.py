# define filename
DATA_FILE = "C:/Users/SwastikaRath/Downloads/H_Computing_2024_Assignment_Files/Python files/companies.csv" #file path

# --- 1. REUSABLE FUNCTION TO FIND MAX POSITION ---
def findMaxPos(target_array):
    maxPos = 0
    for index in range(1, len(target_array)):
        if target_array[index] > target_array[maxPos]:
            maxPos = index
    return maxPos


# --- 2. PROCEDURES ---
def read_data_from_file():
    # create empty lists
    company = []
    numEmployees = []
    ceoSalary = []

    # open file for reading
    with open(DATA_FILE, 'r') as f:
        # go through every line of data
        for line in f.readlines():
            # decode the line
            line = line.strip('\n')
            line = line.split(',')

            # add data to lists
            company.append(line[0])
            numEmployees.append(int(line[1]))
            ceoSalary.append(int(line[2]))

    return company, numEmployees, ceoSalary


def compare_salary(company, ceoSalary):
    chosenCompany = input("Enter the name of the company you would like to check:\n")
    found = False
    
    # Call the reusable function
    maxPos = findMaxPos(ceoSalary)
    
    # Loop for company array
    for index in range(len(company)):
        if company[index] == chosenCompany:
            found = True
            position = index
            
    if found == True:
        difference = ceoSalary[maxPos] - ceoSalary[position]
        print(f"\n{company[maxPos]} company has the highest paid CEO.")
        print(f"The {chosenCompany} CEO earns £{difference} less than the highest paid CEO.")
    else:
        print("\nCompany not found")


def employee_stats(numEmployees):
    # Call the reusable function again for a different array
    maxPos = findMaxPos(numEmployees)
    maxEmployees = numEmployees[maxPos]
    
    count = 0
    
    for index in range(len(numEmployees)):
        # Check if current employee count is >= 90% of the maximum
        if numEmployees[index] >= (maxEmployees * 0.9):
            count = count + 1
            
    print(f"\nThe highest number of employees employed by a single company is {maxEmployees}.")
    print(f"{count} companies employ within 10% of {maxEmployees}.")


# ==========================================
# MAIN PROGRAM
# ==========================================
company, numEmployees, ceoSalary = read_data_from_file()

compare_salary(company, ceoSalary)
employee_stats(numEmployees)