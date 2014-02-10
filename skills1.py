# Things you should be able to do. # Write a function that takes a list and returns a new list with only the odd numbers. def all_odd(some_list):    x = 0
def all_odd(some_list):
    x = 0
    oddlist = []
    for i in some_list:
        if some_list[x] % 2 != 0:
            oddlist.append(some_list[x])
        x = x + 1
    return oddlist    

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    x = 0
    oddlist = []
    for i in some_list:
        if some_list[x] % 2 == 0:
            oddlist.append(some_list[x])
        x = x + 1
    return oddlist    

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    x = 0
    fourletterwords = []
    word = " "
    for i in word_list:
        word = word_list[x]
        if len(word) >= 4:
            fourletterwords.append(word_list[x])
        x = x + 1
    return fourletterwords
    

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    x = 0
    smallest = some_list[x]
    for i in some_list:
        if some_list [x] < smallest:
            smallest = some_list[x]
        x = x + 1
    return smallest


# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    x = 0
    largest = some_list[x]
    for i in some_list:
        if some_list [x] > largest:
            largest = some_list[x]
        x = x + 1
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    x = 0
    new_list = []
    for i in some_list:
        element = float(some_list[x])
        new_list.append(element/2)
        x = x + 1
    return new_list 

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    x = 0
    word_l= []
    for i in word_list:
        word_l.append(len(word_list[x]))
        x = x + 1
    return word_l
    

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        i += 1
    return sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for i in numbers:
        product = product * i
        i += 1
    return product

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joinListString = ""
    x = 0
    for i in string_list:
        joinListString = joinListString + string_list[x] + " "
        x += 1
    return joinListString

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    sumNumbers = 0
    sumNumbers = sum_numbers(numbers)
    avg = sumNumbers / len(numbers)
    return avg


# Get only odd numbers from the given list
mixedlist = [12, 566, 987, 1,0, 21,99,2]
print "------------------------"
print "Original list is %s " % mixedlist
a = all_odd(mixedlist)
print "odd numbers are %s " % a
print "------------------------"

# Get only odd numbers from the given list
mixedlist = [12, 566, 987, 1,0, 21,99,2]
print "Original list is %s " % mixedlist
a = all_even(mixedlist)
print "Even numbers are %s " % a
print "------------------------"

# Get strings that are 4 letter or longer from the given list # mixedwordslist = ["This" , "list" ,"contains" ,"few" ,"words" ,"that" ,"are" ,"longer" ,"than", "4", "words"] # print "Original list is %s " % mixedwordslist 
mixedwordslist = ["This" , "list" ,"contains" ,"few" ,"words" ,"that" ,"are" ,"longer" ,"than", "4", "words"]
print "THe original list is %s " % mixedwordslist
a = long_words(mixedwordslist)
print "four or longer letter words are %s" % a
print "------------------------"

# Find the smallest integer from the given list
integerslist = [3,6,1,-2,7]
print "Original list is %s " % integerslist
a = smallest(integerslist)
print "Smallest number from the list is %d" % a
print "------------------------"

# Find the largest integer from the given list
integerslist = [3,6,1,-2,7]
print "Original list is %s " % integerslist
a = largest(integerslist)
print "Largest number from the list is %d" % a
print "------------------------"

# Find numbers that are divisible by 2 from the list
integerslist = [3,6,1,-2,7]
print "Original list is %s " % integerslist
a = halvesies(integerslist)
print "Halvies numbers from the list are %s" % a
print "------------------------"

# Find length of each string from the list
mixedwordslist = ["This" , "list" ,"contains" ,"few" ,"words" ,"that" ,"are" ,"longer" ,"than", "4", "words"]
print "Original list is %s " % mixedwordslist
y = 0
a = word_lengths(mixedwordslist)
for i in mixedwordslist:
    # print ("Length of word number %d is %s " % ((x+1),a[y])
    print "Length of word '%s'  is %d " % (i , a[y])
    y = y + 1 
print "------------------------"

#Find sum of all numbers in the given list
numbers = range(10)
a = sum_numbers(numbers)
print "Original list is %s " % numbers
print "sum of all numbers is %d " % a
print "------------------------"

#Find product of all numbers in the given list
numbers = [1,2,3,4,5]
a = mult_numbers(numbers)
print "Original list is %s " % numbers
print "Product of all numbers is %d " % a
print "------------------------"


# Join all the words from the given list
stringsList = ["All", "the",  "strings", "in", "a", "list", "together"]
a = join_strings(stringsList)
print "Original list is %s " % stringsList
print "The single string is '%s' " % a
print "------------------------"

# Find Average of all numbers in the given list without using AVG method
numbers = range(5)
a = average(numbers)
print "Original list is %s " % numbers
print "Average of all numbers is %d " % a
print "------------------------"
