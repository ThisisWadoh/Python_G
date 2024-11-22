#Creating empty list:
my_list = []

#appending list:
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print("After Append:", my_list)

#inserting elements to list:
my_list.insert(1, 15)
# print("After insert:", my_list)

#Extending lists:
list_2 = [50, 60, 70]
my_list.extend(list_2)
# print("Extended List:", my_list)

#Removing the last element:
del my_list[-1]
# print("After delete:", my_list)

#Sorting list in ascending order:
my_list.sort()
print("Sorted List:", my_list)

#Finding index of elements in list:
index_of_30 = my_list.index(30)
print("Index of no.30:", index_of_30)