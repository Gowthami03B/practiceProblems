from collections import defaultdict

def func(i):
    return i % 3

def mapToClasses(arr):
    classesToItems = defaultdict(list) # 1: [1,3,7,10], 2: [2,5,8]

    for i in arr:
        res = func(i)
        classesToItems[res].append(i)

    return list(classesToItems.values())

print(mapToClasses([1,2,3,4,5,6,7,8,9,10]))
