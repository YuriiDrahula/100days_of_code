# List Comprehension
numbers = [1, 2, 3]
new_list = [item + 1 for item in numbers]
print(new_list)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)


doubled_list = [item * 2 for item in range(1, 5)]
print(doubled_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)