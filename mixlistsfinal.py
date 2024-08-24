#mixlists
import random

def read_text_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Read the file containing file names
with open('./2mix.txt', 'r') as file:
    file_names = [line.strip() for line in file]

# Modify file names to add "snippet_list.txt"
file_names_with_snippet = [file_name + "snippet_list.txt" for file_name in file_names]

# Read the contents of each file into separate lists
lists = [read_text_file(file) for file in file_names_with_snippet]

# Group items by the numbers between '-' and '.mp4' in the filename
grouped_items = {}
for lst in lists:
    for item in lst:
        last_chars = item.split('-')[-1].split('.mp4')[0]
        if last_chars not in grouped_items:
            grouped_items[last_chars] = []
        grouped_items[last_chars].append(item)

# Shuffle the order of items within each group
for group in grouped_items.values():
    random.shuffle(group)

# Sort the keys to maintain numerical order
sorted_keys = sorted(grouped_items.keys(), key=lambda x: int(x))

# Interleave the shuffled groups in numerical order
interleaved_list = [item for key in sorted_keys for item in grouped_items[key]]

# Write the result to an output file or print it
with open('snippet_list.txt', 'w') as file:
    for item in interleaved_list:
        file.write(f"{item}\n")

with open('snippet_list.txt', 'r') as file:
    contents = file.read()

print(contents)
