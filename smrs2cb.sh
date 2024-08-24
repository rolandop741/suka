#!/bin/bash
#sendmostrecentsuka2catbox

cd ./jimport/sukaaass


./u2cb.sh $(ls -t | grep mp4 | head -n 1) > r.txt

sleep 0.5

cat r.txt
