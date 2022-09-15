python_students = [['Harry', 37.21], ['Berry', 37.21],
                   ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

other_students = [
    ['Prashant', 32],
    ['Pallavi', 36],
    ['Dheeraj', 39],
    ['Shivam', 40]
]

# my code isn't working because the number of students who shared the lowest grade will vary for each input

# This code doesn't work


""" def second_lowest(students):
    sorted(students, key=lambda x: x[1]).pop(0)
    print(students)
    arr = sorted(students[0:2])
    print(arr)
    for student in arr:
        print(student[0]) """


def second_lowest(students):
    arr = sorted(students, key=lambda x: x[1])
    lowest = min(arr, key=lambda x: x[1])
    arr.pop(arr.index(lowest))

    print(arr)


# shoud return Harry and Berry
second_lowest(python_students)
# should return Pallavi
# second_lowest(other_students)
