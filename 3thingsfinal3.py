#3things to drive, download output10x if not found. currently using hb1h
import subprocess
import os
import shutil
import sys
import random



#
musiclist_path = "./musiclist.txt"
directory_path = "./jimport/"
if not os.path.exists(musiclist_path):
    m4a_files = [f for f in os.listdir(directory_path) if f.endswith(".m4a")]
    with open(musiclist_path, 'w') as file:
        file.write("\n".join(m4a_files))
    with open(musiclist_path, 'r') as file:
        print(file.read())
#

#sys.exit(0)

# File containing the list of songs
file = "./musiclist.txt"

# Read the list of songs from the file
with open(file, 'r') as f:
    songs = [line.strip() for line in f if line.strip()]  # Read and clean up the lines

# Choose a random song from the list
if songs:
    song = random.choice(songs)
else:
    print("The music list is empty.")
    sys.exit(0)

# Check if the song exists, and copy it if it doesn't
if not os.path.exists(song):
    source_path = f'./jimport/{song}'
    if os.path.exists(source_path):
        shutil.copy(source_path, song)
        print(f"{song} was copied over")
    else:
        print(f"{song} doesn't exist in your stuff")
        sys.exit(0)
print(f"{song} is here")


#sys.exit(0)

#datetimenname
file_path = os.path.join("./", "user.txt")
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        whatisuser = file.read().strip()
    from datetime import datetime
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m%d%y")
    result = whatisuser + formatted_date
    print(result)
else:
    print("user.txt not found in ./jimport")
    print("add initals to /content/drive/MyDrive and re-run")
    sys.exit(0)
#datetimenname

#sys.exit(0)

# Define the text file containing the file number
file_number_file = 'sukanumber.txt'

# Initialize a list to store the names of deleted files
deleted_files = []

# Read the current file number from the text file
try:
    with open(file_number_file, 'r') as file:
        file_number = int(file.read())
except FileNotFoundError:
    # If the file doesn't exist, start from 1
    file_number = 1


# Run the first command to create 3thingsXX.mp4
input_file = 'snippet_list.txt'
output_file = f'3things{file_number}.mp4'
command1 = f'ffmpeg -f concat -safe 0 -i {input_file} -c:v libx264 -an {output_file}'
subprocess.call(command1, shell=True)



try:
    subprocess.run(["bash", "2abgm-s.sh", output_file, song], check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running the script: {e}")
    sys.exit(1)

#sys.exit(0)

song = 'temp_song.m4a'


# Run the second command to create outputsukaXX.mp4
input_file = f'3things{file_number}.mp4'
output_file = f'./jimport/sukaaass/{result}outputsuka{file_number}.mp4'
command2 = f'ffmpeg -v quiet -i {input_file} -i {song} -c:v copy -map 0:v -map 1:a -shortest -y {output_file}'
subprocess.call(command2, shell=True)
print(f"{result}outputsuka{file_number}")
# Increment the file number and update it in the text file
file_number += 1
with open(file_number_file, 'w') as file:
    file.write(str(file_number))

#
#sys.exit(0)
#

# Read the list of files from snippet_list.txt and extract the actual file names
with open('snippet_list.txt', 'r') as file:
    for line in file:
        if line.startswith("file '") and line.endswith("'\n"):
            filename = line[len("file '"): -2]
            deleted_files.append(filename)

# Delete the files referenced in snippet_list.txt
for filename in deleted_files:
    try:
        os.remove(filename)
    except OSError as e:
        print(f"Error deleting {filename}: {e}")

# Print the list of deleted files
print("Deleted files:")
for deleted_file in deleted_files:
    print(deleted_file)
