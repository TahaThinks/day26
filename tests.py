# Number List Comprehension 1
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

# Number List Comprehension 2
doubled_numbers = [num*2 for num in range(1, 5)]
print(doubled_numbers)

# Number List Comprehension 3
numbers_2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number**2 for number in numbers_2]
print(squared_numbers)

# String List Comprehension 1
name = "Angela"
new_name = [letter for letter in name]
print(new_name)

# Conditional List Comprehension 1
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Conditional List Comprehension 2
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

# Conditional List Comprehension 3
numbers_3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [number for number in numbers_2 if number % 2 == 0]
print(even_numbers)

