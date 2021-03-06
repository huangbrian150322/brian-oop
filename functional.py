from functools import reduce

# A function that returns another function. These are also called 'closures'
def create_adder(x):
    # Note how this fn is declared WITHIN the block
    def adder(y):
        return x + y
    # NO PARENTHESES. 
    # If we instead returned adder(), that would first call `adder`, then return ITS return value!
    return adder

# add_15 is set to a FUNCTION (adder), and x is set to 15
add_15 = create_adder(15)

# What is the result?
add_15(75)
add_15(2)
add_15(3)

# Closures are also useful because they can keep track of state (like objects)
def create_counter():
    count = 0
    def counter():
        # python doesn't like us accessing a variable accessed outside this block
        nonlocal count 
        count += 1
        return count
    return counter

c = create_counter()
c()
c()
c()
c()


# Create a closure that takes in an index, and returns a function that takes an
# array & removes the element at that index.
def create_remover(index):
    def removed(array):
        array.pop(index)
        return array
    return removed

remover = create_remover(2)
remover(['hi', 'hello', 'foo', 'bar']) # ['hi', 'hello', 'bar']

remover = create_remover(7)
remover([1,2,3,4,5,6,7,8,9]) # [1,2,3,4,5,6,7,9]

# Make a generator. It will take no arguments, but returns the next value in the fibonacci sequence on each call.
# Python generators: https://www.tutorialspoint.com/generators-in-python
# Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number
# Starting with 1 instead of zero is fine.
def next_fib():
    i = 1
    j = 1
    while True:
        k = i + j
        yield k
        i = j
        j = k

fib_gen = next_fib()
next(fib_gen)


# Next, some familiarity with "map", "filter" and "reduce".
# Here is a function that iterates through and array and only keeps elements < 10
array = [84, 2, -9, 42, 10, -10, 17, 54, 3]
def keep_lower_than_ten(array):
    new_array = []
    for elem in array:
        if elem < 10:
            new_array.append(elem)
    return new_array

# Instead, write a function, and use `filter`
# https://www.w3schools.com/python/ref_func_filter.asp
# Note that `filter` returns an iterable, not an array. Convert it to an array with `list()`
array = [84, 2, -9, 42, 10, -10, 17, 54, 3]
def filter_func(value):
    if value < 10:
        return True
    else:
        return False

new_array = []
for val in filter(filter_func, array):
    new_array.append(val)
print(new_array)


# Finally, try to write it in one line - use a "lambda" (a undeclared function)
# https://www.tutorialspoint.com/lambda-and-filter-in-python-examples
array = [84, 2, -9, 42, 10, -10, 17, 54, 3]
new_array = list(filter(lambda x: x < 10, array))
print(new_array)


# Map - take an array and multiply all of the elements by -1
array = [84, 2, -9, 42, 10, -10, 17, 54, 3]
new_array = list(map(lambda x: x / -1, array))


# Reduce - this is the hardest one. Reduce is difficult because you need to keep track of a value.
# I will let you do the research for this.
# Note that you will need `from itertools import reduce`
# Start easy - make a reducer that takes in an array of numbers & returns the sum of the array (there are a lot of guides for this)
find_sum([3, 5, -1, 6, 12]) # returns 25

#1
def array_sum(array):
    return reduce(lambda a, b: a + b, array)

#2
array = ([3, 5, -1, 6, 12])
print(reduce(lambda a, b: a + b, array, 0))


# Finally, do something much more difficult - take an array of strings & return the most common character (break a tie how you want)
find_most_common(["hello", "how are you", "not bad", "foo", "bar", "summary"]) # returns 'o'


def find_most_common(array):
    initial = [0] * 26
    final_array = reduce(reducer, array, initial)
    
    maximum = 0
    max_index = 0
    for index, val in enumerate(final_array):
        if val > maximum:
            maximum = val
            max_index = index
    return chr(max_index + 97)

def reducer(array_count, next_value):
    for letter in next_value:
        letter = letter.lower()
        index = ord(letter) - 97
        if index >=0 and index < 26:
            array_count[index] += 1
    return array_count