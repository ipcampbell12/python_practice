

import math
#
#
#
#
""" for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print(num, "fizzbuzz")
    elif num % 3 == 0:
        print(num, "fizz")
    elif num % 5 == 0:
        print(num, "buzz")
    else:
        print(num)
 """
# can also use continue statement


# FIND LEAP YEAR
""" while True:
    year = input("Enter a year:")
    year_num = int(year)

    def leap_year(year):
        if year % 4 == 0:
            return f'{year} IS a leap year! Awesome!'
        else:
            return f'{year} IS NOT a leap year! Bummer!'

    print(leap_year(year_num))
    keep = input("Would you like to keep going y/n?")

    if keep == 'y':
        continue
    else:
        break
 """

# FIND WORD LENGTH ON INPUT STRING
# split string into a list with space as delimiter
# find length of list


# using split method
""" while True:
    profile = input("Enter your profile summmary:")

    def word_count(text):
        text_list = text.split()
        return len(text_list)

    if word_count(profile) > 50:
        print("Cannot exceed 50 words")
        continue
    else:
        print(f'You have written {word_count(profile)} words')
        break
 """

# SAME TASK BUT USING FOR LOOP INSTEAD
""" profile = input("Enter your profile summary:")


def word_count(text):
    count = 0

    for char in text:
        if char == " ":
            count += 1

    return count + 1


print(word_count(profile)) """


# COUNT NUMBER OF VOWELS IN SENTENCE


""" sentence = "I have too many sponges"


def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return f"Your sentence has {count} vowels in it. "


print(count_vowels(sentence)) """
# should return 8

# REMOVE DUPLICATE ENTRIES

""" lottery_entries = ['Joe Bob', 'Ashley Sanchez', 'Bob Anderson', 'Joe Bob']


def remove_dupes(names):
    unique = []

    for name in names:
        if name not in unique:
            unique.append(name)

    return unique


print(remove_dupes(lottery_entries)) """


# FIBONACCI SEQUENCE

""" def fib_seq(n):
    fib_list = [0, 1]
    index = 1

    while len(fib_list) <= n+2:
        fib_list.append(fib_list[index]+fib_list[index-1])
        index += 1

    return fib_list


print(fib_seq(12)) """


# NARCISSTIC NUMBERS


""" def narcissistic(value):
    num_list = [int(num) for num in str(value)]
    raised_nums = list(map(lambda x: x**len(num_list), num_list))
    num_sum = 0

    for num in raised_nums:
        num_sum += num

    return num_sum == value


# print(narcissistic(371))
# should return True

# print(narcissistic(122))
# should return False

print(narcissistic(4887))
# should return False
 """


""" def delete_nth(order, max_e):
    num_count = {}

    for num in order:
        if num not in num_count:
            num_count[num] = 0
        num_count[num] += 1

    for key, value in num_count.items():
        while value > max_e:
            order.reverse()
            order.remove(key)
            order.reverse()
            break

    return order


print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
# print(delete_nth([20, 37, 20, 21], 1))
# print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))

# not just remove next value but remove ALL the next values after n """


source1 = 'https://www.geeksforgeeks.org/python-sort-list-of-lists-by-lexicographic-value-and-then-length/'
source2 = 'https://stackoverflow.com/questions/20145842/python-sorting-by-multiple-criteria'
source3 = 'https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/'
ssourc4 = 'https://docs.python.org/3/howto/sorting.html'
source5 = 'https://www.geeksforgeeks.org/python-merge-two-lists-into-list-of-tuples/'


my_dict = {'a': 2, 'd': 1, 'c': 5, 'b': 3, 'f': 2}


# set to reverse so it sorts alphabetically, but negate the value to make it sort right
# allows you to sort integers in reverse and the letters not in reverse (alphabetically)
def print_vals(n):
    my_vals = sorted(n.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    for val in my_vals:
        print(str(val[0])+' '+str(val[1]))


# print_vals(my_dict)
"""
intended output:
c 5
b 3
a 2
f 2
d 1 """


def letter_count(name):
    char_list = [char for char in name]
    char_count = [name.count(char) for char in name]
    char_dict = dict(zip(char_list, char_count))
    tup = sorted(char_dict.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    for i in tup[:3]:
        print(str(i[0]+' '+str(i[1])))

# letter_count('aabbbccde')
# should return
# b 3
# a 2
# c 2

# letter_count('google')
# letter_count("Google")
# should return
# G 2
# O 2
# E 1


""" def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']

    kevin = [''.join(x) for l in range(1, len(string))
             for x in combinations(string, l) if x[0] in vowels]

    kevin_subs = []

    for word in kevin:
        index = 0
        while kevin.count(word) < string.count(word):
            kevin_subs.append(word)
            index += 1

    return kevin_subs


 """


# someone else's solution
""" def minion_game(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    S = []
    K = []
    for i in range(len(string)):
        if string[i] in vowel:
            K.append(string[i:])  # grab
        else:
            S.append(string[i:])

    return K


print(minion_game('BANANA')) """


def get_digits(number):
    digits = len(str(number))
    return f"{number} has {digits} digits"


print(get_digits(255))


def get_square_root(number):
    sqrt = math.sqrt(number)
    return f"The square root of {number} is {sqrt}"


print(get_square_root(255))


def squared(number):
    sqrd = number**2
    return f"{number} squared is {sqrd}"


print(squared(255))


def even_odd(number):
    status = ''
    if number % 2 == 0:
        status = 'even'
    if number % 2 != 0:
        status = 'odd'
    return f"{number} is an {status} number"


print(even_odd(10))


def prime_composite(number):
    flag = False
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break
    if flag == True:
        return f"{number} is a composite number"
    else:
        return f"{number} is a prime number"


print(prime_composite(11))
