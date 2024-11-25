# make empty list
my_list = []
print("empty array : ")
print(my_list)

print("--------------------------------------------------------------")

# append stuff
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("appended array : ")
print(my_list)

print("--------------------------------------------------------------")

# insert 15 at second index
my_list.insert(1,15);
print("after inserting 15 : ")
print(my_list)

print("--------------------------------------------------------------")

# extend with another list
addme = [50, 60, 70]
my_list.extend(addme)
print("after extending it : ")
print(my_list)

print("--------------------------------------------------------------")

# remove the last element
del my_list[-1]
print("after deleting the last item : ")
print(my_list)

print("--------------------------------------------------------------")

# sort in ascending order
my_list.sort()
print("sorted array : ")
print(my_list)

print("--------------------------------------------------------------")

# print the index of 30
the_id = my_list.index(30)
print("the index of 30 ~> : " + str(the_id))

print("--------------------------------------------------------------")