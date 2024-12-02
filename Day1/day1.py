from typing import Dict, List

# Part 1 

list1: List[int] = []
list2: List[int] = []
with open("input.txt") as f:
    for line in f:
        try:
            a, b = line.strip().split("   ")
            list1.append(a)
            list2.append(b)
        except ValueError:
            continue

list1 = sorted(list1)
list2 = sorted(list2)
result = 0
for i in range(len(list1)):
    result += abs(int(list1[i]) - int(list2[i]))
print(result)

# Part 2 

list1: List[int] = []
list2: List[int] = []
count: Dict[int, int] = {}

with open("input.txt") as f:
    for line in f:
        try:
            a, b = line.strip().split("   ")
            a = int(a)
            b = int(b)
            list1.append(a)
            list2.append(b)
            count[b] = count.get(b, 0) + 1
        except ValueError:
            continue
        
result = 0
for val in list1:
    if val in count:
        result += val * count[val]
print(result)