#getsomevids wip

import os
import random

# Set the directory path
directory_path = "./jimport/"

# List all files in the directory
file_list = os.listdir(directory_path)

# Ensure that the directory contains at least 10 files
if len(file_list) < 3:
    print("There are not enough files in the directory.")
else:
    # Select 10 random filenames from the list (without extensions)
    random_files = random.sample([os.path.splitext(filename)[0] for filename in file_list if filename.endswith(".mp4")], 3)

    # Define the path for the output text file
    output_file_path = "2mix.txt"

    # Write the selected filenames to the text file
    with open(output_file_path, "w") as output_file:
        for filename in random_files:
            output_file.write(filename + "\n")
            print(f"{filename}")