'''
my_list = [15, 23, 32, 46]

print(my_list[0]) #Outputs the first item in the list
print(my_list[-1]) #Outputs the last item in the list
print(my_list[:2]) #Outputs the first two items in the list

result = my_list[0] + my_list[-1] #Creating a new item by adding together the first and last item in the list
my_list.append(result) #Adding this new item to the end of the list

print(my_list) #Outputs the entire list, including the new item

tuples_list = [200, 15, "Programming", 1+2, "Lab 3"] #A tuple with items of multiple data types

print("The number of items in the list is ", len(tuples_list)) #Outputs the length of the list
tuples_list.append(5.25) #Appends a new item with a different data type

print(tuples_list) #Outpus entire list, including the new item

tuples_list.insert(0, "Something") #Inseting a new item into the list at postion 0
tuples_list.remove(tuples_list[-1]) #Removes the item in the last position

print(len(tuples_list)) #Outputs the length of the list
print(tuples_list[0]) #Outputs the item in the first position of the list

tuples_list[1] += 1 #Changes the item in the second position

print(type(tuples_list)) #Outputs the type of the list

tuple_list = tuple(tuples_list) #Converts the type of the list to a tuple
print(type(tuple_list)) #Re-outputs the type of the list

print(tuple_list[0]) #Outputs the first item in the tuple
print(len(tuple_list)) #Outputs the length of the tuple

#tuple_list[0] = "New item" #Attempts to add a new item to the tuple (cannot happen as tuples are immutable)

tuples_list_two = [5, 13, 24, "Text", 3.1415926, "Some more text"] #New tuple
tuple_list_two = tuple(tuples_list_two)

joined_tuple = tuple_list + tuple_list_two #Joins the two tuples together by creating a new list and moving all the items into it

print(joined_tuple) #Outputs the new tuple
'''

my_dict = {"name" : "John",
           "age" : 20,
           "email" : "Something@gmail.com",
           "is_student" : True,
           "sleep_late" : False,
           "descriptive_message" : "John is a student who likes programming"}

print(my_dict)
print(my_dict["age"])
