#  Data Structures: Used to store, organize and manipulate data. CRUD operations can be performed as well.
'''
Python programming language provides the following built-in data structures, which can be used to store collections of data:
1. List
2. Tuple
3. Set
4. Dictionary
'''

# List: A list is a collection of ordered and mutable elements. It allows duplicate values, index based access (0 -  length-1).
# Internal working: Lists in Python are implemented as dynamic arrays, which allow for efficient insertion and deletion of elements at any position in the list. It resizes the underlying array when the number of elements exceeds its capacity, which can lead to occasional performance overhead. However, for most use cases, lists provide good performance and are a versatile data structure in Python.

# creating list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# iterating over list
for i in my_list:
    print(i)

# List methods
# append(object): add item in the end of the list
my_list.append(6)
print(my_list)

# insert(index, value): insert element at specified index
my_list.insert(0, 0)
print(my_list)

# pop(): remove/delete last element of the list
my_list.pop()
print(my_list)

# remove(object): remove specified object from the list
# for duplicates, remove first occurence

# my_list.remove(6)
# my_list.remove(6) # and return error if element is not present
print(my_list)

# sort(): sort list alphabetically
unsorted_list = ['b', 'd', 'c', 'a']
print(unsorted_list)   

sorted_list = unsorted_list.sort() #do not work on characters
print(sorted_list) #returns None

# list_name.sort(reverse=True) : sort list in descending order
unsorted_list.sort(reverse=True)
print(unsorted_list)

# count(object): return count of the specified object
print(my_list.count(1))

# reverse(): reverse the list
my_list.reverse()
print(my_list)

# index(object) : return index of specified index in the list
print(my_list.index(0))


# clear(): remove all elements from the list
my_list.clear()
print(my_list)