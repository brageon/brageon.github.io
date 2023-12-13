import os, re
def find_pattern_positions(filename, pattern):
    with open(filename, 'r') as f:
        lines = f.readlines()
    pattern = re.compile(pattern)
    positions = []
    for line_index, line in enumerate(lines):
        matches = pattern.finditer(line)
        for match in matches:
            positions.append((line_index + 1, match.start() + 1))
    return positions
for filename in os.listdir('gui'):
    if filename.endswith('.txt'):
        pattern = '9'
        target_filename = os.path.join('gui', filename)
        pattern_positions = find_pattern_positions(target_filename, pattern)
        if pattern_positions:
            print(f"File: {filename}")
            print(f"Pattern '{pattern}' found at positions {pattern_positions} in {target_filename}")
        else:
            print(f"Pattern '{pattern}' not found in {target_filename}")