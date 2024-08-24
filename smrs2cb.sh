#!/bin/bash
#sendmostrecentsuka2catbox

cd /root/mystuff/localsuka/jimport/sukaaass


./u2cb.sh $(ls -t | grep mp4 | head -n 1) > r.txt

sleep 0.5

cat r.txt
