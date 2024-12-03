# Part 1

with open("input.txt", 'r') as f:
    # i = Reading head
    data:str = f.read()
    i = 0
    result = 0
    while i < len(data):
        i = data.find('mul(', i)
        # No more mul( from i onwards
        if i == -1:
            break
        i = i + 4
        num_length = 0
        arg1:str = ""
        arg2:str = ""
        while data[i].isnumeric() and num_length <= 3:
            arg1 += data[i]
            i += 1
            num_length += 1
        if data[i] == ",":
            i += 1
            num_length = 0
            while data[i].isnumeric() and num_length <= 3:
                arg2 += data[i]
                i += 1
                num_length += 1
        if data[i] == ")":
            result += int(arg1) * int(arg2)
        i += 1
    print(result) # 174960292

# Part 2

