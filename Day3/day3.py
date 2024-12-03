# Part 1

# Evaluates the data from a given start and end index
# Returns the result between the start and end index
def eval(data:str, start:int, end:int) -> int:
    assert start < end
    assert end <= len(data)
    i = start
    result = 0
    while i < len(data) and i < end:
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
    return result 

with open("example.txt", 'r') as f:
    data:str = f.read()
    # i = Reading head
    result1 = eval(data, 0, len(data)) 
    print(result1) # 174960292

    enabled = True
    index = 0
    result2 = 0
    end = len(data) - 1
    while index < len(data):
        if enabled:
            end = data.find("don't()", index) + len("don't()")
        else:
            end = data.find("do()", index)+ len("do()")
        if end != -1:
            # found an instruction
            if enabled:
                result2 += eval(data, index, end)
            enabled = not enabled
            
        else: #EOF
            if enabled:
                result2 += eval(data, index, len(data))
            end = len(data) - 1
        # Update index
        if enabled:
            index = end 
        else:
            i = end 
    print(result2)

    

# Part 2

