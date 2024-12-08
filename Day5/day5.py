# Part 1

def check_update(update:str, rules) -> int:
    # Return the value at the middle index of the update
    pages = update.split(",")
    for x, X in enumerate(pages):
        for Y in pages[x+1:]:
            if rules.find(f"{Y}|{X}") != -1: return 0
    return int(pages[len(pages)//2])
    
def compare(X, Y, rules):
    if rules.find(f"{X}|{Y}") != -1:
        return -1
    if rules.find(f"{Y}|{X}") != -1:
        return 1
    return 0

def sort_incorrect(update:str, rules) -> int:
    if check_update(update, rules): return 0
    pages = update.split(",")

    # Compare each X with each Y, n * n complexity
    sorted_pages = sorted(pages, key=lambda X: [compare(X, Y, rules) for Y in pages])
    return int(sorted_pages[len(sorted_pages)//2])


with open("input.txt", "r") as f:
    raw_data = f.read()
    raw_rules, raw_updates = raw_data.split("\n\n")
    rules = raw_rules.split()
    updates = raw_updates.split()
    result = 0
    result2 = 0
    for update in updates:
        result += check_update(update, raw_rules)
    print(result)
    for update in updates:
        result2 += sort_incorrect(update, raw_rules)
    print(result2)
    