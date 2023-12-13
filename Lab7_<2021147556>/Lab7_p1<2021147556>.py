import re

file_path = 'input_7_1.txt'

# Open the file and read
with open(file_path, 'r') as file:
    lines = file.readlines()

functions = {}

# Define a regular expression pattern to find "def name("
pat = re.compile(r'def\s+([a-zA-Z0-9_]*)\(')

# Iterate each line
for i, line in enumerate(lines, 1):
    def_funtion = pat.search(line)
    if def_funtion:
        # Extract funtion name
        name = def_funtion.group(1)
        # Store
        functions[name] = {'def': i, 'calls': []}

    for name, info in functions.items():
        if name != '':
            # Extract funtion name
            call = re.compile(rf'{name}\(').search(line)
            if call and i != info['def']:
                # Store
                functions[name]['calls'].append(i)

# Print
for name, info in functions.items():
    calls = ', '.join(str(call) for call in info['calls'])
    print(f"{name}: def in {info['def']}, calls in [{calls}]")
