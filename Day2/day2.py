# Part 1

def check_report(levels : str, tolerance = 0) -> bool:
    
    unsafe = 0
    increasing = 0
    # 0 = Not set, 1 = incr, -1 = decr
    for i in range(len(levels) - 1):
        cur = int(levels[i])
        next = int(levels[i + 1])
        delta = abs(cur - next)
        if delta > 3 or delta < 1: unsafe += 1
        if increasing == 0:
            if next > cur:
                increasing = 1
            else:
                increasing = -1
        else:
            if increasing == 1 and next < cur: unsafe += 1
            elif increasing == -1 and next > cur: unsafe += 1
    return unsafe <= tolerance  

result = 0

with open("input.txt", 'r') as f:
    reports = f.readlines()
    for report in reports:
        levels = report.split(" ")
        if check_report(levels): result += 1

print(result)

# Part 2
result2 = 0

def check_report_with_dampener(levels:str) -> bool:
    for i in range(len(levels)):
        # Remove level at index i
        new_levels = levels[:i] + levels[i+1:]
        if check_report(new_levels): return True
    return False

with open("input.txt", 'r') as f:
    reports = f.readlines()
    for report in reports:
        levels = report.split(" ")
        if check_report_with_dampener(levels): result2 += 1
print(result2)  