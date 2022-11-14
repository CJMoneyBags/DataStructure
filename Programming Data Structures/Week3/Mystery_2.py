def is_float(text):
    try:
        float(text)
        return True
    except:
        return False

def mystery_2(text):
    stack = []
    for item in text.split(' '):
        if item == "+" or item == "-" or item == "*" or item == "/":
            if len(stack) < 2:
                print("Invalid Case 1!")
                return None
            op2 = stack.pop()
            op1 = stack.pop()
            if item == "+":
                res = op1 + op2
            elif item == "-":
                res = op1 - op2
            elif item == "*":
                res = op1 * op2
            else: 
                if op2 == 0:
                    print("Invalid Case 2!")
                    return None
                res = op1 /op2
            stack.append(res)
        elif is_float(item):
            stack.append(float(item))
        elif item == "":
            pass
        else:
            print("Invalid Case 3!")
            return None
    if len(stack) != 1:
        print("Invalid Case4!")
        return None
    return stack[0]
print(mystery_2("5 3 7 + * ")) ## return 50
print(mystery_2("6 2 + 5 3 - /")) # return 4
mystery_2("-") ## Inavlid Case 1
mystery_2("a")
mystery_2("4 2 2 - /") ## Inavlid Case 2
mystery_2('537+*') ## Invalid Case 3
mystery_2('') ## Invalid Case 4
mystery_2('              ') ## Invalid Case 4




