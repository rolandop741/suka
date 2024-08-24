#3things to drive, download output10x if not found. currently using hb1h
import subprocess
import os
import shutil
import sys



#song ornot startbeta
import os
import shutil
song = 'deathbyechno1.m4a'
if not os.path.exists(song):
  source_path = f'/content/drive/MyDrive/jimport/{song}'
  if os.path.exists(source_path):
    shutil.copy(source_path, song)
    #songpath = source_path,song
    print(f"{song} was copied over")
  else:
    print(f"{song} doesnt exist in your stuff")
    sys.exit(0)
print(f"{song} is here")
#song ornot endbeta



#datetimenname
file_path = os.path.join("/content/drive/MyDrive", "user.txt")
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        whatisuser = file.read().strip()
    from datetime import datetime
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m%d%y")
    result = whatisuser + formatted_date
    print(result)
else:
    print("user.txt not found in /content/drive/MyDrive")
    sys.exit(0)
#datetimenname

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
command1 = f'ffmpeg -v quiet -f concat -safe 0 -i {input_file} -c:v h264_nvenc -an {output_file}'
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
output_file = f'/content/drive/MyDrive/jimport/sukaaass/{result}outputsuka{file_number}.mp4'
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
