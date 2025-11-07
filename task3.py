items = []
names = []
marks = []
with open("C:/Users/a.sharma\Desktop/1101 task 3/idk.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')
for i in range(len(names)):
    print(names[i] + " - " + marks[i])
print(names)
print(marks)