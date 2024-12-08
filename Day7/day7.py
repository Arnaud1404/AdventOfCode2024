def explore(target, nums) -> bool:
    # Explore both * and + branches
    if len(nums) == 1:
        return nums[0] == target
    
    mult = nums[0]*nums[1]
    add = nums[0]+nums[1]

    # Replace nums[0]
    return explore(target, [mult]+nums[2:]) or \
           explore(target, [add]+nums[2:])

def explore2(target, nums) -> bool:
    # Explore *, + and concatenation branches
    if len(nums) == 1:
        return nums[0] == target
    
    mult = nums[0]*nums[1]
    add = nums[0]+nums[1]
    concat = int( str(nums[0]) + str(nums[1]))
    # Replace nums[0]
    return explore2(target, [mult]+nums[2:]) or \
           explore2(target, [add]+nums[2:]) or \
           explore2(target, [concat]+nums[2:])

def evaluate(expr, concat = False) -> int:
    target, nums = expr.split(":")
    target = int(target)
    nums = [int(num) for num in nums.split()]
    if concat:
        if explore2(target, nums):
            return target
        return 0
    if explore(target, nums):
        return target
    return 0

with open("input.txt") as f:
    data = f.read().split("\n")
    result = 0
    result2 = 0
    for expr in data:
        result += evaluate(expr)
    for expr in data:
        result2 += evaluate(expr, True)
    print(f"Result1 = {result}")
    print(f"Result2 = {result2}")
