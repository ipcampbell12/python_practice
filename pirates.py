
# need to make sure that all the characters from first are in second and that they have the same length

def grabscrab(word, possible_words):

    actual_words = []

    w = sorted(word)

    for possible in possible_words:
        if sorted(possible) == w:
            actual_words.append(possible)

    return actual_words


#print(grabscrab("ortsp", "ports"))
print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))
# should return "sport" and "ports"
