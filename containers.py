# Exercise 1

    #Create a list named students containing some student names (strings).
    #Print out the second student's name.
    #Print out the last student's name.

students = ['kydae','bill','joe']
print(students[1])
print(students[-1])

# Exercise 2

#     Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
#     Use a for loop to print out the string "[food goes here] is a good food".
foods = ('berry', 'coffee','truffle')
for key in foods:
    print(f"{key} is a good food")

    # Exercise 3

    # Using a for loop, print just the last two food strings from foods.

    #     Hint: Use the slice operator to select the last two foods

sliced_foods = foods[-2:]
print(sliced_foods)

# Exercise 4

#     Create a dictionary named home_town containing the keys of city, state and population.
#     Print a string with this format:
#     "I was born in city, state - population of population"

home_town = {
    'city': 'Grants Pass',
    'state': ' Oregon',
    'population': '37,000'
}
print(f" I was born in {home_town['city']},{home_town['state']} - population of {home_town['population']}")


print(dir(home_town))
# Exercise 5

#     Iterate over the key: value pairs in home_town and print a string for each item, for example:
#     "city = Arcadia"
#     "state = California"
#     "population = 58000"

for key, value in home_town.items():
    print(f"{key} = {value}")

    # Exercise 6

    # Create an empty list named cohort.

    # Using a for loop to iterate over the students list.

    #     Hint: Use the enumerate function to provide both the index & student

    # Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:

    #  {
    #    'student': 'Tina',
    #    'fav_food': 'Cheeseburger'
    #  }

    # Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).

cohort = []
