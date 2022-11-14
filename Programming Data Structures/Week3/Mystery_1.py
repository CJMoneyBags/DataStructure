def mystery_1(text):
    stack = []
    for letter in text:
        stack.append(letter)

    result = " "
    while len(stack) > 0:
        result += stack.pop()

    return result


print(mystery_1("racecar"))
print(mystery_1("stressed"))
print(mystery_1("a nut for a jar of tuna"))
