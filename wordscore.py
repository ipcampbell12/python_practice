""" Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
 """


def high(x):

    # 1. find value for each letter in alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = dict(zip(alphabet, list(range(1, len(alphabet)+1))))

    # 2. find score for each word
    words = x.split(' ')
    word_scores = []
    count = 0

    while len(word_scores) < len(words):
        word_score = 0
        for char in words[count]:
            word_score += alpha_dict[char]
        word_scores.append(word_score)
        count += 1

    # 3. find highest scoring word
    words_dict = dict(zip(words, word_scores))
    for key, value in words_dict.items():
        if value == max(word_scores):
            return key


#print(high('aa b'))
print(high('bb d'))
print(high('d bb'))
#print(high('what time are we climbing up the volcano'))
# volcano


# Alternative solution
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
