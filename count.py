

def letter_count(name):
    char_list = [char for char in name]
    char_count = [name.count(char) for char in name]
    char_dict = dict(zip(char_list, char_count))
    tup = sorted(char_dict.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    for i in tup[:3]:
        print(str(i[0]+' '+str(i[1])))


letter_count('aabbbccde')
# should return
# b 3
# a 2
# c 2
# letter_count('google')
# should return G:2, O;2, E:1
