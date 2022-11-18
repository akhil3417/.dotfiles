#!/bin/bash
#Combines all videos in current folder with given extension
#into single file
#Created by Kris Occhipinti
#Copyright July 21th 2019
#License: GPLv3 - https://www.gnu.org/licenses/gpl-3.0.txt

if [ "$#" -eq 0 ];then
  echo "Extension needed"
  echo "Example: $0 MOV"
  exit 1
else
  ext="$1"
fi

echo "Combining $ext files"

tmp="videos.tmp"
rm $tmp
ls *.$ext|while read v
do
  echo "file $v" >> $tmp
done

ffmpeg -f concat -safe 0 -i $tmp -c copy output.$ext
mpv "output.$ext"
rm $tmp
