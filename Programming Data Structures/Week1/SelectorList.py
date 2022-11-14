list1 = [1,2,3,4,5]
list2 = [2, 4, 6, 8, 10]
selector_list = [1,1,1,2,2,1,2,2,2,1]


def list_selector(list1, list2, selector):
    list1_pos = 0
    list2_pos = 0
    result = []

    for item in selector:
        if item == 1:
        
            result.append(list1[list1_pos])
            list1_pos += 1
        
        elif(item == 2):
        
            result.append(list2[list2_pos])
            list2_pos += 1

    return result

print(list_selector(list1, list2, selector_list))
    
