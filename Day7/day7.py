def evaluate(expr) -> int:
    target, nums = expr.split(":")
    target = int(target)
    print(nums)
    nums = [int(num) for num in nums.split()]
    

with open("example.txt") as f:
    data = f.read().split("\n")
    result = 0
    for expr in data:
        result += evaluate(expr)
    print(result)