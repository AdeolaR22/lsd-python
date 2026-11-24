 # uestion 1  : 
# Write a Python program that multiplies all the items in a list.
# Sample list= [2, 3, 6]
# Result = 36
# Question 2
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# Hint: You can use the sort function.
# Question 3 
# Write a Python program that combines two dictionaries by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
# Question 4
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) so that is an integral number between 1 and n (both included). Then the program should print the dictionary. Suppose the following input is supplied to the program: 8. Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Question 5
# Write a program to sort a tuple by its float element.
# For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
# Question 6
# Write a Python program to create a set.
# Examples : {0, 1, 2, 3, 4}
# Write a Python program to iteration over sets.
# Write a Python program to add members in a set and to remove items from a given set.



numbers = [2, 3, 6]

result = 1

for number in numbers:
    result = result * number

print(result)



my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

my_list.sort(key=lambda x: x[-1])

print(my_list)



d1 = {'a': 100, 'b': 200, 'c': 300}

d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()

for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print(result)



n = int(input("Enter a number: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print(squares)




my_list = [
    ('item1', '12.20'),
    ('item2', '15.10'),
    ('item3', '24.5')
]
my_list.sort(key=lambda x: float(x[1]), reverse=True)
print(my_list)


# Create a set
numbers = {0, 1, 2, 3, 4}
print(numbers)
# Iterate over a set
numbers = {0, 1, 2, 3, 4}
for number in numbers:
    print(number)
# Add and remove members from a set
numbers = {0, 1, 2, 3, 4}

# Add an item
numbers.add(5)

print("After adding:", numbers)

# Remove an item
numbers.remove(2)

print("After removing:", numbers)

