
li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
def RemoveDuplicate(li):
    new_list=[]
    seen=set()

    for item in li:
        if item not in seen:
            seen.add(item)
            new_list.append(item)
    return new_list

print(RemoveDuplicate(li))