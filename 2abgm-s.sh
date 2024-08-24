#!/bin/bash

# Define your input video and song file paths
inputvideo="$1"
inputsong="$2"

counter=1
while [ -f "result${counter}.mp4" ]; do
    counter=$((counter + 1))
done
outputfile="result${counter}.mp4"

# Get the length of the input video and song
video_length=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$inputvideo")
song_length=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$inputsong")

# Calculate the maximum start time and generate a random start time
max_start_time=$(awk "BEGIN {print $song_length - $video_length}")
if (( $(awk "BEGIN {print ($max_start_time > 0)}") )); then
    max_start_time_int=$(awk "BEGIN {printf \"%d\", $max_start_time}")
    start_time=$(( RANDOM % max_start_time_int ))
else
    start_time=0
fi

echo "cutting $inputsong at $start_time"
# Extract a segment from the input song
temp_song="temp_song.m4a"
ffmpeg -v error -i "$inputsong" -ss "$start_time" -t "$video_length" -c copy -y "$temp_song"