import subprocess
import random
import sys
import os
import string
import argparse

def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Extract and combine video snippets")
    parser.add_argument("input_video", help="Input video file")
    parser.add_argument("start_time", type=float, help="Start time in seconds")
    parser.add_argument("end_time", help="End time in seconds or 'd' for default")
    parser.add_argument("num_snippets", type=int, help="Number of snippets to extract")
    parser.add_argument("snippet_duration", type=float, help="Duration of each snippet in seconds")
    parser.add_argument("action", choices=["k", "e"], help="Specify 'k' to keep snippet files or 'e' to discard them")

    args = parser.parse_args()

    # Generate a random prefix for all the output files
    random_prefix = "s" + random_string(4)

    input_video = args.input_video
    input_video_name, _ = os.path.splitext(os.path.basename(input_video))

    start_time = args.start_time
    end_time = args.end_time
    num_snippets = args.num_snippets
    snippet_duration = args.snippet_duration

    snippet_files = []

    # Get the video duration
    video_duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video]))

    if end_time.lower() == 'd':
        end_time = video_duration
    else:
        end_time = float(end_time)

    start_time = max(0, start_time)
    end_time = min(end_time, video_duration)

    # Calculate the total duration of the snippets
    total_snippets_duration = num_snippets * snippet_duration

    # Create a list of randomly spaced start times for the snippets
    start_times = []
    while len(start_times) < num_snippets:
        random_start_time = random.uniform(start_time, end_time - total_snippets_duration)
        if all(abs(random_start_time - start) >= snippet_duration for start in start_times):
            start_times.append(random_start_time)

    start_times.sort()

    variance = 73

    for i, start_time in enumerate(start_times):
        output_file = f"{random_prefix}_{input_video_name}_{snippet_duration}-{i + 1}.mp4"
        snippet_files.append(output_file)



        min_range = snippet_duration * (1 - variance / 100)
        max_range = snippet_duration * (1 + variance / 100)

        random_duration = random.uniform(min_range, max_range)
        random_duration = round(random_duration, 3 - len(str(int(random_duration))))

        cmd = [
            "ffmpeg",
            "-v", "quiet",
            "-ss", str(start_time),
            "-i", input_video,
            "-t", str(random_duration),
            "-an",
            "-r", "30",
            output_file
        ]

        print(f"Iteration {i + 1}: {cmd}")

        subprocess.run(cmd)

    

    input_video_name, _ = os.path.splitext(os.path.basename(args.input_video))
    
    # Combine the individual snippet files into one big file
    with open(f"{input_video_name}snippet_list.txt", "w") as list_file:
        for file_name in snippet_files:
            list_file.write(f"file '{file_name}'\n")

   

    # Handle the action to either keep or discard snippet files
    if args.action == "e":
        print("Discarding individual snippet files.")
        for snippet_file in snippet_files:
            os.remove(snippet_file)

if __name__ == "__main__":
    main()
