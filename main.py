def quantity_same_elem(lists):
    same_elems = {}
    same_quan = []
    for list in lists:
        for elem in list:
            if elem not in same_elems:
                same_elems[elem] = 0
            else:
                same_elems[elem] += 1
    for elem in same_elems:
        if same_elems[elem] > 1:
            str_elem = str(elem)
            str_quan = str(same_elems[elem])
            same_quan.append((str_elem+' : '+str_quan+' times '))
    return same_quan

first_list = [8,8,90,1]
second_list = [90,11,8,43]
third_list = [124,77,8,90]

lists = []
lists.append(first_list)
lists.append(second_list)
lists.append(third_list)

print(quantity_same_elem(lists))