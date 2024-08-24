#!/bin/bash

file=$1

folder=$2

token="4zYPtWv3UDjXbkeufFkZmxOrjPtqeqE5"

curl -X POST 'https://store1.gofile.io/contents/uploadfile' -H "Authorization: Bearer $token" -F "file=@$file" -F "folderId=$folder"
