def find_pairs(words):
    pairs = set()
    pair = set()
    for word in words:
        rev = word[::-1]
        if rev < word: # Make sure that the pairs are in order or else the pairs set will have duplicate pairs.
            pair = (rev, word)
        else:
            pair = (word, rev)

        if rev in words:
            pairs.add(pair)

    return pairs

print(find_pairs(["am", "at", "ma", "if", "fi"]))
