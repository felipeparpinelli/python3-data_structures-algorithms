list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]

# Concat lists.
list3 = list1 + list2
print (list3)


# Pop -> remove an element for the specified index
list = [1, 2, 3, 4]
list.pop(1) # remove index 1
list.pop(len(list) - 1) # Removes the element from the last index
print (list)

# Remove -> Instead of removing by index, remove by element
list = [1, 2, 3, 4]
num = 3
if num in list:
	list.remove(3)
else:
	print ("element not found")
print (list)

# len() -> Get list size
print (len(list))
for i in list:
	print (i)

# convert list to tuple
t_list = tuple(list)
print (t_list)
print (type(t_list))

# append() -> add element in list
list.append(10)
print (list)

# insert(index, element) -> insert an element in the specified index
list.insert(0, 500)
list.insert(len(list), 400)
print (list)

# sort()
list.sort()
print (list)

# slice notation
list = [1, 2, 3, 4]
print(list[1:3]) # items start through end-1
print(list[1:]) # items start through the rest of the list
print(list[:3]) # items from the beginning through end-1
print(list[:]) # a copy of the whole array
print(list[0]) # return first element
print(list[-1]) # return last element
print(list[::-1]) # reverse list



