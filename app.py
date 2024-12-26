# ﬂowerpot = int(input('How many flowerpots?: '))
# ﬂower_seeds = int(input('How many packs of ﬂower seeds?: '))
# soil = int(input('How many bags of soil?: '))

# ﬂowerpot_price = 4.00
# ﬂower_seeds_price = 1.00
# soil_price = 5.00

# salex_tax = 0.06

# items_price = (flowerpot * flowerpot_price) + (flower_seeds * flower_seeds_price) + (soil * soil_price)

# final_price = (items_price * salex_tax) + items_price

# print(final_price)


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

#CONTINUE STATEMENT
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
total = 0
for count in range (x + 3, y+1, 3):
    print('Count: ', count)
    total += count
print(total)