# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    
    x = 0
    for i in some_list:
        if some_list[x] % 2 == 0:
            del some_list[x]
        x =x + 1
    return some_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    x = 0
    print some_list
    for i in some_list:
        if some_list[x] % 2 != 0:
           del some_list[x]
        x =x + 1
    return some_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return []

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return None

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return []

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return []

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None

# Get only odd numbers from the list
mixedlist = [1,2,4,6,7,8,0]
result = all_odd(mixedlist)
print mixedlist
print "The odd numbers are : %s" % result


# # Get only even numbers from the list
# mixedlist = [1,3,5,7]
# result = all_even(mixedlist)
# print "The even numbers are : %s" % result
