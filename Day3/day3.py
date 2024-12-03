# Part 1

# Evaluates the data from a given start and end index
# Returns the result between the start and end index
def eval(data:str, start:int, end:int) -> int:
    assert start < end
    assert end <len(data)
    i = start
    result = 0
    while i < len(data) and i < end: 
        i = data.find('mul(', i)
        # No more mul( from i onwards
        if i == -1 or i >= end:
            break
        i = i + 4
        num_length = 0
        arg1:str = ""
        arg2:str = ""
        while i < end and data[i].isnumeric() and num_length <= 3:
            arg1 += data[i]
            i += 1
            num_length += 1
        if i < end and data[i] == ",":
            i += 1
            num_length = 0
            while i < end and data[i].isnumeric() and num_length <= 3:
                arg2 += data[i]
                i += 1
                num_length += 1
        if i < end and data[i] == ")":
            result += int(arg1) * int(arg2)
        i += 1
    return result 

with open("input.txt", 'r') as f:
    data:str = f.read()
    # index = Reading head
    result1 = eval(data, 0, len(data)-1) 
    print(result1) # 174960292

    enabled = True
    index = 0
    result2 = 0
    end = len(data) - 1
    while index < len(data) - 1:
        if enabled:
            end = data.find("don't()", index) 
        else:
            end = data.find("do()", index) 
        if end != -1:
            # found an instruction
            if enabled:
                result2 += eval(data, index, end)
            enabled = not enabled
        else: # No instrcution found
            end = len(data) - 1
            if enabled:
                result2 += eval(data, index, end)
        # Update index
        index = end + 1
    print(result2) #56275602
