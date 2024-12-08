
#Part 1
# Check according to reading direction : N, NE, E (XMAS), SE, SW, W (SAMX), NW

def check_E(rows) -> int:
    result = 0
    for row in rows:
        index = 0
        while index != -1:
            index = row.find("XMAS", index)
            if index != -1:
                result += 1
                index += 1
    return result

def check_W(rows) -> int:
    result = 0
    for row in rows:
        index = 0
        while index != -1:
            index = row.find("SAMX", index)
            if index != -1:
                result += 1
                index += 1
    return result

def check_N(rows) -> int:
    result = 0
    # Rotate the rows 90 degrees counterclockwise to check vertically
    rotated_rows = [''.join(row) for row in zip(*rows)]
    for row in rotated_rows:
        index = 0
        while index != -1:
            index = row.find("XMAS", index)
            if index != -1:
                result += 1
                index += 1
    return result

def check_S(rows) -> int:
    result = 0
    # Rotate the rows 90 degrees counterclockwise to check vertically
    rotated_rows = [''.join(row) for row in zip(*rows)]
    for row in rotated_rows:
        index = 0
        while index != -1:
            index = row.find("SAMX", index)
            if index != -1:
                result += 1
                index += 1
    return result

#Idk how to do it cleaner
def check_SE(rows) -> int:
    result = 0
    for i in range(len(rows) - 3):
        for j in range(len(rows[i]) - 3):
            if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M' and rows[i+3][j+3] == 'X':
                result += 1
    return result

def check_NW(rows) -> int:
    result = 0
    for i in range(3, len(rows)):
        for j in range(3, len(rows[i])):
            if rows[i][j] == 'S' and rows[i-1][j-1] == 'A' and rows[i-2][j-2] == 'M' and rows[i-3][j-3] == 'X':
                result += 1
    return result

def check_NE(rows) -> int:
    result = 0
    for i in range(3, len(rows)):
        for j in range(len(rows[i]) - 3):
            if rows[i][j] == 'S' and rows[i-1][j+1] == 'A' and rows[i-2][j+2] == 'M' and rows[i-3][j+3] == 'X':
                result += 1
    return result

def check_SW(rows) -> int:
    result = 0
    for i in range(len(rows) - 3):
        for j in range(3, len(rows[i])):
            if rows[i][j] == 'S' and rows[i+1][j-1] == 'A' and rows[i+2][j-2] == 'M' and rows[i+3][j-3] == 'X':
                result += 1
    return result

def check_all(rows) -> int:
    result = 0
    result += check_N(rows)
    result += check_NE(rows)
    result += check_E(rows)
    result += check_SE(rows)
    result += check_S(rows)
    result += check_SW(rows)
    result += check_W(rows)
    result += check_NW(rows)
    return result

def check_mas_square(rows):
    result = 0
    for i in range(1,len(rows) - 1):
        for j in range(1,len(rows[i]) - 1):
            if rows[i-1][j-1] == 'M' and rows[i-1][j+1] == 'S'\
            and rows[i][j] == 'A'\
            and rows[i+1][j-1] == 'M' and rows[i+1][j+1] == 'S':
                result += 1
            
            if rows[i-1][j-1] == 'S' and rows[i-1][j+1] == 'S'\
            and rows[i][j] == 'A'\
            and rows[i+1][j-1] == 'M' and rows[i+1][j+1] == 'M':
                result += 1
            
            if rows[i-1][j-1] == 'S' and rows[i-1][j+1] == 'M'\
            and rows[i][j] == 'A'\
            and rows[i+1][j-1] == 'S' and rows[i+1][j+1] == 'M':
                result += 1
            
            if rows[i-1][j-1] == 'M' and rows[i-1][j+1] == 'M'\
            and rows[i][j] == 'A'\
            and rows[i+1][j-1] == 'S' and rows[i+1][j+1] == 'S':
                result += 1
    return result

        


with open("input.txt", 'r') as f:
    data:str = f.read()
    rows = data.split()
    result = check_all(rows)

    print(result) #2401
    result2 = check_mas_square(rows)
    print(result2) #1822
