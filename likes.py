def likes(names):

    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


print(likes(["Peter"]))
# returns "Peter likes this"

print(likes(["Alex", "Jacob", "Mark", "Max"]))
# returns "Alex, Jacob and 2 others like this"

print(likes(['Jacob', 'Alex']))
# returns "Jacon and Alex like this"

print(likes(['Max', 'John', 'Mark']))
# returns "Max, John, and Mark like this"
