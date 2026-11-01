# filter() : retrieve only those items from an iterable that satisfy a certain condition and returns a filter object(lazy iterator)
# syntax:
    # filter(function,iterable)

# PS: Retrive value which are even from a list of numbers using filter() function.

numbers = [1,2,3,4,5,6,7,8,9,10]
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(list(filter(even, numbers)))

# can be also be done using lambda function
print(list(filter(lambda x: x % 2 == 0, numbers)))

# can also be used to filter data from list of dictionaries.
characters = [
    {'name' : 'Luffy', 'age' : 19, 'status': 'Yonko'},
    {'name' : 'Zoro', 'age' : 21, 'status': 'Swordsman'},
    {'name' : 'Nami', 'age' : 20, 'status': 'Navigator'},
    {'name' : 'Usopp', 'age' : 19, 'status': 'Sniper'},
    {'name' : 'Sanji', 'age' : 21, 'status':  'Cook'}
]

print(list(filter(lambda x: x['age'] > 20, characters)))