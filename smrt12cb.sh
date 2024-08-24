#!/bin/bash
#sendmostrecentsuka2catbox

cd /root/mystuff/localsuka/jimport/testing1

u2cb $(ls -t | grep mp4 | head -n 1) > r.txt
