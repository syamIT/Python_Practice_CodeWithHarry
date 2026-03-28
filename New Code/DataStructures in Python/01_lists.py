marks = [100,95,49,68,55];
mixed = [True,False, 100,"Syam","mixedList"]
print(marks[0])
print(mixed[1:5])
# print(marks[5])   #IndexError: list index out of range


# Some Methods in List
# print(marks)
# marks.append(62); 
# print(marks)
# marks.pop()
# print(marks)
# marks.sort()
# print(marks)



# list comprehensions
table = [];
a = 5;
# for i in range(1,11):
#     table.append(a*i)
# print(table)

table = [a*i for i in range(1,11)]
print(table)
print("Hello")