import csv
filePath ="C:/Users/SwastikaRath/Downloads/H_Computing_2023_Assignment_Files (1)/NH_Computing-Science_Assignment-Electronic-Files_2023/Software File/"


from dataclasses import dataclass
@dataclass
class order:
    attraction : str = ""
    category : str = ""
    visitors : int = 0
    daysOpen : float = 0.0
    height : float = 0.0






def read_from_file_into_parallel_arrays():
    attraction = []
    category = []
    visitors = []
    daysOpen = []
    height = []

    with open(filePath+'attractions.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            attraction.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(float(row[3]))
            height.append(float(row[4]))
            
            
    
    return attraction, category, visitors, daysOpen, height 


attraction, category, visitors, daysOpen, height = read_from_file_into_parallel_arrays()


#finding minimum visitors value
minimum = visitors[0]
for index in range(1,len(visitors)):
    if visitors[index] < minimum:
        minimum = visitors[index]


#finding minimum visitors index

minpos = 0
for index in range(1,len(visitors)):
    if visitors[index] < visitors[minpos]:
        minpos = index
print("The attraction with the lowest number of visitors is:", attraction[minpos], "which has", visitors[minpos], "visitors")


#finding the maximum visitors value

maximum = visitors[0]
for index in range(1,len(visitors)):
    if visitors[index] > maximum:
        maximum = visitors[index]



#finding minimum visitors index

maximumPosition = 0
for index in range(1,len(visitors)):
    if visitors[index] > visitors[maximumPosition]:
        maximumPosition = index
print("The attraction with the highest number of visitors is:", attraction[maximumPosition], "which has", visitors[maximumPosition], "visitors")



#write the names of all of the roller coasters that require a service within 7 days to a file

serviceNeeded = 0
attractionsNeedingService = []

for index in range(len(daysOpen)):
    days = (daysOpen[index] / 90)
    if days <= 7:
        print(attraction[index])
        attractionsNeedingService.append(attraction[index])
        serviceNeeded = serviceNeeded + 1
print("Total attractions needing service:", serviceNeeded)



with open("C:/Users/SwastikaRath/Downloads/H_Computing_2023_Assignment_Files (1)/NH_Computing-Science_Assignment-Electronic-Files_2023/Software File/service.csv", 'w') as writefile:
    for attractionName in attractionsNeedingService:
        writefile.write(attractionName + '\n')



#1cii - count and display the number of attractions with the height restriction

HeightRestrictedAttractionCount = 0
for index in range(len(height)):
    if height[index] >= 1.0:
        HeightRestrictedAttractionCount = HeightRestrictedAttractionCount + 1
print("There are", HeightRestrictedAttractionCount, "attractions with this height restriction.")