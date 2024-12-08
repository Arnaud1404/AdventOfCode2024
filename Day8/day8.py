def offset(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return (x1-x2, y1-y2)

with open("example.txt") as f:
    data = f.read().split()
    data = [list(line) for line in data]
    n = len(data) # Always a square matrix
    antennas = {} # key = antenna:str
                  # value = List of each coordinates (r:int,c:int)
    antinodes = set() # Set of coordinates, no dupes allowed

    for r in range(n):
        for c in range(n):
            if data[r][c] != ".":
                antenna = data[r][c]
                antennas.setdefault(antenna, []).append((r,c))

    # Part 1
    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                dx, dy = offset(coords[i], coords[j])
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                
                new_x, new_y = x1+dx, y1+dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    antinodes.add((new_x, new_y))
                    if data[new_x][new_y] == ".":
                        data[new_x][new_y] = "#"

                new_x, new_y = x2-dx, y2-dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    antinodes.add((new_x, new_y))
                    if data[new_x][new_y] == ".":
                        data[new_x][new_y] = "#"
    print(f"Result 1 = {len(antinodes)}")
    
    # Part 2
    def trace_line(start_x, start_y, dx, dy):
        x, y = start_x, start_y
        while 0 <= x < n and 0 <= y < n:
            antinodes.add((x, y))
            if data[x][y] == ".":
                data[x][y] = "#"
            x, y = x + dx, y + dy
        
        x, y = start_x - dx, start_y - dy
        while 0 <= x < n and 0 <= y < n:
            antinodes.add((x, y))
            if data[x][y] == ".":
                data[x][y] = "#"
            x, y = x - dx, y - dy

    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                dx, dy = offset(coords[i], coords[j])
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                trace_line(x1, y1, dx, dy)
                trace_line(x2, y2, dx, dy)
    print(f"Result 2 = {len(antinodes)}")

                
            