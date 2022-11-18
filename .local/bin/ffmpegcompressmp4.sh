#!/bin/bash
######################################################################
#Copyright (C) 2022  Kris Occhipinti
#https://filmsbykris.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
######################################################################

dir="compressed"
log=""
mkdir -p "$dir"

for i in *.mp4;
do
  ffmpeg -i "$i" -vcodec libx264 -crf 24 "$dir/$i";
  log+="$(ls -lha "$i"|awk '{print $9 " " $5" : "}')"
  log+="$(ls -lha "$dir/$i"|awk '{print $5 "|"}')"
done

echo $log|tr "|" "\n"
