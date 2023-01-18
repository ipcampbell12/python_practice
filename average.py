scores = [
    {
        "score": 3,
        "student_id": 2
    },
    {
        "score": 1,
        "student_id": 2
    },
    {
        "score": 1,
        "student_id": 2
    },
    {
        "score": 1,
        "student_id": 2
    },
    {
        "score": 2,
        "student_id": 3
    },
    {
        "score": 0,
        "student_id": 3
    },
    {
        "score": 0,
        "student_id": 3
    },
    {
        "score": 0,
        "student_id": 3
    },
    {
        "score": 1,
        "student_id": 4
    },
    {
        "score": 0,
        "student_id": 4
    },
    {
        "score": 1,
        "student_id": 4
    },
    {
        "score": 0,
        "student_id": 4
    },
    {
        "score": 3,
        "student_id": 5
    },
    {
        "score": 3,
        "student_id": 5
    },
    {
        "score": 3,
        "student_id": 5
    },
    {
        "score": 3,
        "student_id": 5
    }
]


def totals_by_id(arr):

    uniqueIds = list(set([item["student_id"] for item in arr]))
    key_list = ["student_id", "score"]
    n = len(uniqueIds)

    new_list = []
    for index in range(0, n):
        new_list.append({key_list[0]: uniqueIds[index], key_list[1]: 0})

    for item in arr:
        for other_item in new_list:
            pass


# def totals_by_id(arr):


"""  const getCategoryTotals = (expenses) => {

        const totalsList = []

        expenses.forEach(element => {
            const itemAlreadyExists = totalsList.find(item => item.category === element.category)

            //if item is not present, add the item
            if (!itemAlreadyExists) {
                totalsList.push({ category: element.category, value: element.value })
            } else {
                //if is present, add the amt 
                itemAlreadyExists.value += element.value
            }
        });

        return totalsListß


    } """


print(totals_by_id(scores))
