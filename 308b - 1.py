saving_year = 0
for index in range (12):
    saving_month = float(input("Enter savings this month £"))
    saving_year = saving_year + saving_month

print(round(saving_year,2))
