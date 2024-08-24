import subprocess
import random
import sys
import os
import string
import argparse
import urllib.request
import shutil

# Check if vbgm.py exists, and if not, download it
vbgm_script_path = 'vbgm.py'

vbgm_script_path = 'vbgm.py'
if not os.path.exists(vbgm_script_path):
    try:
        shutil.copy('/content/drive/MyDrive/jimport/vbgm.py', vbgm_script_path)
    except FileNotFoundError:
        print("Error: vbgm.py not found in /content/drive/MyDrive/jimport/")
        sys.exit(1)

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Process videos with vbgm2.py")
    parser.add_argument("argument1", type=int, help="Value to pass as argument1")
    args = parser.parse_args()
    return args

# Rest of your script (with modifications to accept input_video_names)

min_value = 150
max_value = 170
r = random.randint(min_value, max_value)

# Parse command line arguments
args = parse_arguments()
argument1 = args.argument1

# Read the list of input video names from a text file
input_video_names = []

file_path = '/content/2mix.txt'

with open(file_path, 'r') as file:
    for line in file:
        video_name = line.strip()
        input_video_names.append(video_name)

# Process each video in the list
for video_name in input_video_names:
    video_name_with_extension = f"/content/drive/MyDrive/jimport/{video_name}.mp4"
    command = f"python vbgm2.py {video_name_with_extension} 0 d {argument1} 0.22 k"
    print(command)
    os.system(command)
    print(f"{video_name} is done")
