def explore(target, nums):
    if target == 0:
        return True
    if len(nums) == 0:
        return False
    # Try division only if remainder is zero
    return (target % nums[0] == 0 and explore(target // nums[0], nums[1:]))\
            or explore(target - nums[0], nums[1:])


def evaluate(expr) -> int:
    target, nums = expr.split(":")
    target = int(target)
    nums = [int(num) for num in nums.split()]
    # Do the operations in reverse order
    if explore(target, nums[::-1]):
        return target
    return 0

with open("input.txt") as f:
    data = f.read().split("\n")
    result = 0
    for expr in data:
        result += evaluate(expr)
    print(f"\nFinal result = {result}")