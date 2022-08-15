

answer = input("Do you want to go the store?")

if answer == "Yes":
    print("Well get going!")
else:
    print("You are so lazy!")

""" my_list = [3, 6, 8, 15, 19, 35]

plus1list = []

for num in my_list:
    if num % 2 == 0:
        print(f'The number {num} is even')
    else:
        print(f'The number {num} is odd')

 """
""" my_list = ['Bob', 'Rolf', 'Anne']
my_tuple = ('Bob', 'Rolf', 'Anne')
my_set = {'Bob', 'Rolf', 'Anne'}


# print(my_list[2])

my_list[0] = 'Smith'
my_list.append("Yo Momma")
my_list.remove("Rolf")

print(my_list)

# can't modify tuples after they are created

# can add elements to list, but will be in any order
# can't have duplicate elements inside a set
my_set.add("Bruno")
print(my_set)
 """


# ADVANCED SET OPERATIONS
friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}
other_friends = {"Madea", "Velma"}

# figure out which friends are not abroad
# difference takes set as argument, removes from first set
# inverse would return empty set, set()
local_friends = friends.difference(abroad)
# print(local_friends)

# adds two sets together to make new set
all_friends = friends.union(other_friends)
# print(all_friends)


art = {"David", "Ian", "Selma", "Veronica"}
science = {"David", "Ian", "Jose", "Mirabel"}

# find the elements that both sets have in common
both = art.intersection(science)
# print(both)
