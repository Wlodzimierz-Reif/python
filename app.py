# IF ELIF ELSE
# x = int(input('first value:'))
# y = int(input('second value:'))
# if((x + y) % 2 == 0):
#     print('sum is even')
# else:
#     print('sum is odd')

# print('sum is', 'even' if ((x + y) % 2 == 0) else 'odd' )

# x = int(input('Enter a whole number:'))
# y = 6
# print('Your number is:', 'smaller' if (x < y) else f'greater than {y}')

# x = input('Enter a day:')
# y = int(input('Enter an hour'))

# if (x == 'Saturday' or x == 'Sunday'):
# # if (x == 'Saturday') or (x == 'Sunday'):
#     print('Closed, sorry...')
# elif(y < 9 or y > 17):
#     print('Closed, sorry...')
# else:
#     print('Open, come on in!')


# FACTORIAL
# x = int(input("Enter a number to calculate its factorial: "))
# count = x
# total: int = 0
# while count > 1:
#     print('count', count)
#     if total == 0:
#         total = count * (count - 1)
#         count -= 1
#     else:
#         total *= count - 1
#         count -= 1
# print(total)

# LOOP
# n = int(input('Enter n: '))
# m = int(input('Emter m: '))
# total = 0

# while m <= n:
#     total += m
#     m += 1
# print(total)

# WHILE ELSE LOOP
# countdown = 10
# while countdown > 0:
#     print(countdown)
#     countdown -= 1
#     if input('Is it windy? ') == 'yes':
#         print('Mission Aborted')
#     break
# else:
#     print('We Have Liftoff!')

# WHILE EXERCISE
# import random
# available_players = ['Anastasia', 'Eli', 'Jamal', 'Jada', 'Theo', 'Michelle', 'Adam', 'Rhea', 'Charlie', 'Jasmine', 'Marley', 'Kenji', 'Sydney', 'Cooper']
# # List of each captain’s teams
# jaleesas_team = ['Jaleesa']
# rahims_team = ['Rahim']
# while len(jaleesas_team) < 8:
#     player_selected = random.choice(available_players)
#     jaleesas_team.append(player_selected)
#     available_players.remove(player_selected)
# rahims_team.extend(available_players)
# # Prints the players on each team
# print("Jaleesa's Team")
# print (*jaleesas_team, sep = ", ")
# print("Rahim's Team")
# print (*rahims_team, sep = ", ")


# FOR LOOP
# x = int(input("Enter a number: "))
# for i in range(1, x + 1):2
#     if i > 5:
#         break
#     print(i)

# CONTINUE STATEMENT
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# total = 0
# for count in range (x + 3, y+1, 3):
#     print('Count: ', count)
#     total += count
# print(total)

# NESTED LOOPS
# Sum of all numbers between 1 and x
# x = int(input('Enter a number: '))
# y = 1
# while y <= x:
#     total = 0
#     i = 1
#     while i <= y:
#         total += i
#         i += 1
#     y += 1
#     print('Total:', total)

# RANDOM
# continue break the current loop iteration execution, not only if statement

# for i in range(10):
#     if i % 2 == 0:
#         print(i + 10)
#     elif i % 3 == 0:
#         continue
#     elif i % 5 == 0:
#         break
#     print("Hello")
# print("Hello again")

# LIST
# list_name[-1]
# list index -1 access the last element of the list
# negative index access the list from the end i.e. -1 is the last element, -2 is the second last element and so on
# x = [1, 2, 3, 4, 5]
# print(x[-1])

# LIST CONCATINATION
# x = [1, 2, 3]
# y = [4, 5, 6]
# z = x + y
# print(z)

# LIST SLICING
# Slice from index to index not including the end index
# x = [1, 2, 3, 4, 5]
# print(x[1:3])
# print(x[:3])
# print(x[1:])
# print(x[-4:-1])

# LIST REPLICATION
# Multiply list by a number
# x = [1, 2, 3]
# y = x * 3
# print(y)

# IN OPERATOR
# Is current value present in the list. Like .some in JS
# x = [1, 2, 3, 4, 5]
# print(0 in x)

# NOT IN OPERATOR
# Reverse of in operator
# x = [1, 2, 3, 4, 5]
# print(0 not in x)

# LIST FUNCTIONS
# x = [1, 2, 3, 4, 5, 100, 10, 9, 12]
# print(min(x))
# print(max(x))
# print(sum(x))
# print(len(x))
# x.append(6)
# x.insert(2,'x')
# .pop removes index
# x.pop()
# x.pop(3)
# .remove removes certain value
# y=['a', 'b', 'c', 'd', 'e']
# y.remove(2)
# x.sort()
# x.reverse()
# z = x.index(100)
# x.clear()
# print(x)

# PROCESSING LISTS
# Adding index to the list
# birds = ['crow', 'parrot', 'eagle', 'pigeon', 'sparrow']
# for i in range(len(birds)):
#     print('Bird', birds[i], 'is at index', i)
# for i, bird in enumerate(birds):
#     print('Bird', bird, 'is at index', i)

# filtering using while loop
# word = ['a', 'd', 'a', 'm', 'a', 'n', 't']
# while 'a' in word:
#     word.remove('a')
# print(word)

# Extend
# x = [1, 2, 3]
# y = [4, 5, 6]
# x.extend(y)

# LIST COMPREHENSION
# It's like filter in JS
# x = [1, 2, 3, 4, 5]
# y = [i for i in x if i % 2 == 0]
# z = [i*2 for i in x if i % 2 == 0]
# print(y)
# print(z)

#
#####################
# STRINGS
# Strings can have their elements accessed using the same indexing and slicing as lists
# Min and max values are based on ASCII values
# x = 'Hello, World!'
# print(x[0])
# print(x[-1])
# print(x[1:5])
# print(x[:5])
# print(x[7:])
# print(x.find('W'))
# print(min(x))
# print(max(x))
# print(len(x))
# print(x.replace('World', 'Universe'))
# x.replace('World', 'Universe') # Strings are immutable!!!
# print(x)

# MULTILINE STRINGS
# x = '''Hello,
# World!'''
# x = """Hello,
# World!"""
# x = 'Hello, \nWorld!'
# print(x)

# REPEATING STRINGS
# x = 'Hello, World! '
# y = x * 3
# print(y)

# CONCATENATING STRINGS
# x = 'Hello, '
# y = 'World!'
# z = x + y
# print(z)

# STRING FUNCTIONS
# x = 'Hello World! test  test'
# print(x.isalpha())
# print(x.isnumeric())
# print(x.islower())
# print(x.isupper())
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.split(' ')) # Splits the string into a list

# SUBSTRING
# x = 'Hello, World!'
# print(x[1:12:2]) # Start, end, step
# print(x[::-1]) # Reverse string

# PLACEHOLDER
# x = 'Hello, {}!'
# y = 'World'
# z = 'Hello, {test}!' #named indexes
# ff = 'Hello, {0}! {1}' #numbered indexes
# fff = 'Hello, {0}! {0}' #numbered indexes
# print(x.format(y))
# print(z.format(test = 'World')) #named indexes
# print(ff.format('World', 'Test')) #numbered indexes
# print(fff.format('World', 'Test')) #numbered indexes

# STRING ALIGMENT
# x = 'Hello,{:3} World!'
# print(x.format('')) #add extra space in the index
# str1 = 'a{:>4}c'.format('b') #extra space before the index
# str2 = 'a{:^4}c'.format('b') #extra space evenly
# str3 = 'a{:<4}c'.format('b') #extra space after the index
# print(str1)
# print(str2)
# print(str3)


# ####################
# ####################
# TUPLES
# Tuples are immutable

# FUNCTIONS
# min and max
# len and sum
# count(value) - how many times a value appears in a tuple
# index(value) - index of a value in a tuple
# tuple(variable) - convert a list/string to a tuple


# ####################
# ####################
# SETS
# Sets are unordered and do not allow duplicates
# Sets are immutable
# Sets can be converted to lists/tuples and vice versa
# We can initiate a set with repeating values though(x = {1,1,2,3,4,4})
# x = {1, 2, 3, 4, 5}
# y = list(x)
# z = tuple(x)
# ff = set(z)

# Similar to JS when converting to a set, duplicates are removed
# x = [1, 2, 3, 4, 5, 5, 5, 5]
# y = set(x)

# You can't access elements in a set using indexing
# x = {1, 2, 3, 4, 5}
# # print(x[0]) # Error
# print(list(x)[2])
# print(2 in x)

# Set seems to sort the elements

# Set functions
# x = {1, 2, 3, 4, 5}
# y = {1, 3, 7, 9}
# print(min(x))
# print(max(x))
# print(len(x))
# x.add(6)
# x.remove(2) # the argument is a value, not index
# x.pop() # removes the last element
# x.clear() # removes all elements

# UNION
# print(x.union(y)) # combines two sets. Union function
# print(x | y) # Union operator

# # INTERSECTION
# print(x.intersection(y)) # returns the common elements between two sets
# print(x & y) # Intersection operator

# # DIFFERENCE
# print(x.difference(y)) # returns the elements that are in x but not in y
# print(x - y) # Difference operator

# # SIMMETRIC DIFFERENCE
# print(x.symmetric_difference(y)) # returns the elements that are not common between two sets
# print(x ^ y) # Symmetric difference operator


# ######################
# ######################
# DICTIONARIES
# Like objects in JS
# key can a string, int or float or tuples(?)
# x = {'name': 'Adam', 'age': 25, 'city': 'London', 1: 'One', 0.2: 'Zero point two'}
# can be initiated with dict() function
# x = {}
# x = dict([('name', 'Adam'), ('age', 25), ('city', 'London')])
# print(x)
# x = dict((('name', 'Adam'), ('age', 25), ('city', 'London')))
# print(x)
# x = dict([[1, 'One'], [2, 'Two'], [3, 'Three']])
# print('lastName' in x) # Check if a key is in the dictionary keys
# print('One' in x.values()) # Check if a value is in the dictionary values
# print(x['age'])
# print(x[0.2])
# print(x.get('name'))
# print(x.get(0.3, 'Not Found')) # returns a default value if the key is not found
# x['city'] = 'Manchester' # update a value

# REMOVING VALUES
# del x['age']
# print(x.pop('name'))
# print(x)
# pop removes the key:value pair and returns the value


# BUILD-IN FUNCTIONS
# x = {1: 'One', 2: 'Two', 3: 'Three'}
# print(min(x)) # Finds the minimum key
# print(max(x)) # Finds the maximum key
# print(len(x))
# print(list(x.keys()))
# print(list(x.values()))
# print(list(x.items())) # returns a list of tuples
# for key, value in x.items():
#     print(key, value)
# keys, values and items have to be conveted to list to use the build-in list functions
# x.clear() # removes all elements
# for key in x:
#     print(key, x[key])


# ###################
# USING FILE SYSTEM
# file = open('test.txt', 'r') # w - write, r - read, a - append, x - create
# file.write('Hello, World!')
# file.close()
# file = open('test.txt', 'r')
# s = file.readlines()
# for line in file:
#     print(line)
# file.close()
# print(s)
# we can write only strings to a file


###################
# FUNCTIONS
# def my_function(raz, dwa):  # function header
#     """This is a function that prints 'Hello, World!'"""  # docstring
#     print("Hello, World!")


# my_function()
