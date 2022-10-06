""" returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
 """

# FIRST ATTEMPT - TOO INEFFICIENT
# def scramble(s1, s2):
#     s1list = [char for char in s1]
#     s2list = [char for char in s2]
#     newlist = []

#     for char in s2list:
#         if char in s1list:
#             newlist.append(char)
#             s1list.remove(char)

#     return ''.join(newlist) == s2


# if any character in s1 has a character in s2 that has a lower count, then it will fail


print(scramble("fxnhzpbxkuamlzg", "mgllpnau"))
# l shows up in s1 but not for same number of time as in s2
# so double letters are a problem


print(scramble('rkqodlw', 'world'))
# returns True
print(scramble('cedewaraaossoqqyt', 'codewars'))
# returns True
print(scramble('katas', 'steak'))
# returns False
