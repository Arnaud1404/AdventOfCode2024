def parse_disk_map(disk_map):
    # Convert string of digits into list of ints
    return [int(x) for x in disk_map]

def create_block_layout(lengths):
    # Convert lengths into block representation with file IDs
    layout = []
    file_id = 0
    is_file = True  # Alternate between file and gap
    
    for length in lengths:
        if is_file:
            layout.extend([str(file_id)] * length)
            file_id += 1
        else:
            layout.extend(['.'] * length)
        is_file = not is_file
        
    return layout

def defragment(layout):
    # Move files left until no gaps between files remain
    while True:
        # Find rightmost file block
        right = len(layout) - 1
        while right >= 0 and layout[right] == '.':
            right -= 1
            
        if right < 0:
            break
            
        # Find leftmost free space
        left = 0
        while left < right and layout[left] != '.':
            left += 1
            
        if left >= right:
            break
            
        # Move block left
        layout[left] = layout[right]
        layout[right] = '.'
        
    return layout

def calculate_checksum(layout):
    # Multiply position by file ID and sum
    return sum(int(block) * i for i, block in enumerate(layout) if block != '.')

def solve(disk_map):
    lengths = parse_disk_map(disk_map)
    layout = create_block_layout(lengths)
    final_layout = defragment(layout)
    return calculate_checksum(final_layout)

# Test with example
f = open("input.txt")
disk_map = f.read().strip()
# disk_map = "2333133121414131402"
result = solve(disk_map)
print(f"Checksum: {result}")