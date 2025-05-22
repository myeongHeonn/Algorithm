from itertools import product

def solution(word):
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        permutation = list(product(vowels, repeat = i))
        for p in permutation:
            dictionary.append("".join(p))

    dictionary.sort()

    for idx, w in enumerate(dictionary):
        if w == word:
            return idx + 1