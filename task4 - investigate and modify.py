# Program 4 - Investigate and Modify
name = ['alice adams','ben brown','carol codd']
newname = []
for x in range(len(name)):
  initial = name[x][0]
  surname = name[x].split(' ')[1]
  print(initial,surname)
  newname.append(initial.upper() + surname[0].upper() + surname[1:])
print(newname)
