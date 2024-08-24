#!/bin/bash
#sendmostrecentsuka2catbox

cd ./jimport/testing1

u2cb $(ls -t | grep mp4 | head -n 1) > r.txt
