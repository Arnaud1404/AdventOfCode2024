from typing import List, Tuple

def parse_data(data: str) -> List[int]:
    return [int(x) for x in data]

def create_block_layout(lengths: List[int]) -> List[str]:
    layout = []
    file_id = 0
    is_file = True
    
    for length in lengths:
        if is_file:
            layout.extend([str(file_id)] * length)
            file_id += 1
        else:
            layout.extend(['.'] * length)
        is_file = not is_file
    
    return layout

def find_file_bounds(data: List[str], file_id: int) -> Tuple[int, int]:
    file_str = str(file_id)
    start = -1
    size = 0
    
    for i, char in enumerate(data):
        if char == file_str:
            if start == -1:
                start = i
            size += 1
            
    return start, size

def find_free_space(data: List[str], start_pos: int, needed_size: int) -> int:
    count = 0
    pos = 0
    
    while pos < start_pos:
        if data[pos] == '.':
            count += 1
            if count == needed_size:
                return pos - count + 1
        else:
            count = 0
        pos += 1
    
    return -1

def defragment_blocks(data: List[str]) -> List[str]:
    while True:
        right = len(data) - 1
        while right >= 0 and data[right] == '.':
            right -= 1
            
        if right < 0:
            break
            
        left = 0
        while left < right and data[left] != '.':
            left += 1
            
        if left >= right:
            break
            
        data[left] = data[right]
        data[right] = '.'
        
    return data

def defragment_whole_files(data: List[str]) -> List[str]:
    max_id = max(int(x) for x in data if x != '.')
    
    for file_id in range(max_id, -1, -1):
        start, size = find_file_bounds(data, file_id)
        if start == -1:
            continue
            
        target = find_free_space(data, start, size)
        if target != -1:
            file_data = data[start:start + size]
            data[target:target + size] = file_data
            data[start:start + size] = ['.'] * size
    
    return data

def defragment(data: List[str], part2: bool = False) -> List[str]:
    if part2:
        return defragment_whole_files(data)
    return defragment_blocks(data)

def calculate_checksum(data: List[str]) -> int:
    return sum(int(block) * i for i, block in enumerate(data) if block != '.')

def solve(data: str, part2: bool = False) -> int:
    lengths = parse_data(data)
    data = create_block_layout(lengths)
    final_data = defragment(data, part2)
    return calculate_checksum(final_data)

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
        result1 = solve(data, False)
        print(f"Part 1 Checksum: {result1}")
        result2 = solve(data, True)
        print(f"Part 2 Checksum: {result2}")