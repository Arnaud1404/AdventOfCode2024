import copy


def get_next_position(direction, data, r, c, width, height):
    nextPosition = None
    newr = r
    newc = c
    match direction:
        case "^":
            newr -= 1
            if newr >= 0 and newr < height:
                nextPosition = data[newr][c]
        case "<": 
            newc -= 1
            if newc >= 0 and newc < width:
                nextPosition = data[r][newc]
        case ">":
            newc += 1
            if newc >= 0 and newc < width:
                nextPosition = data[r][newc]
        case "v":
            newr += 1
            if newr >= 0 and newr < height:
                nextPosition = data[newr][c]
    return (nextPosition, newr, newc)

def rotate(direction):
    match direction:
        case "^":
            return ">"
        case "<":
            return "^"
        case ">":
            return "v"
        case "v":
            return "<"


def move(data, width, height):
    found = False
    for r in range(height):
        for c in range(width):
            if data[r][c] in ("^","<",">","v"):
                r, c = r, c
                found = True
                break
        if found:
            break

    direction = data[r][c]
    
    visited = 0
    moves = 0
    (nextPosition, newr, newc) = get_next_position(direction, data, r, c, width, height)

    while(nextPosition != None):
        if moves >= width * height: return -1 # stuck in a loop
        match nextPosition:
            case "#":
                data[r][c] = rotate(direction)
                direction = data[r][c]
                (nextPosition, newr, newc) = get_next_position(direction, data, r, c, width, height)
            case "O":
                data[r][c] = rotate(direction)
                direction = data[r][c]
                (nextPosition, newr, newc) = get_next_position(direction, data, r, c, width, height)
            case ".":
                data[r][c] = "X"
                data[newr][newc] = direction
                r, c = newr, newc
                visited += 1
            case "X":
                data[r][c] = "X"
                data[newr][newc] = direction
                r, c = newr, newc
        moves += 1
        (nextPosition, newr, newc) = get_next_position(direction, data, r, c, width, height)
    return visited
        
with open("input.txt") as f:
    data = f.read().split("\n")
    data = [list(line) for line in data]
    width = len(data[0])
    height = len(data)
    # Part 1
    # We add one since it doesn't count the last tile
    # Smart copy thanks Google
    temp_data = [row[:] for row in data]
    visited = move(temp_data, width, height)
    visited += 1
    print(f"Part 1 answer: {visited}")
    # Part 2
    # Test each valid obstacle location and see how many loops we get
    # Time complexity is O(n**2) * O(n**2) = O(n**4) where n is 130, have fun
    result = 0
    for r in range(height):
        for c in range(width):
            if data[r][c] != ".":
                continue 
            temp_data = [row[:] for row in data]
            temp_data[r][c] = "O"
            if move(temp_data, width, height) == -1:
                result += 1
                print(f"\rConfig {r*width+c} / {width*height} is valid", end="")
    print(f"\nPart 2 answer: {result}")


