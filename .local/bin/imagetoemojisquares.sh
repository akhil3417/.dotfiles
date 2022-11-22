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

if [[ $# < 1 ]];
then
  echo "Input Image Needed"
  echo "Example: $0 hello.png"
  exit 1
fi

#convert image to text with a value of either black or white
txt="$(convert "$1"  -threshold 50% txt:-)"

#get count of how many pixels are in each row
count="$(echo "$txt"|head -n1|cut -d\: -f2|cut -d\, -f1|awk '{print $1}')"

#replace all pixels with squares
echo "$txt"|grep -v '^#'|awk '{print $4}'|sed 's/white/⬜/g;s/black/⬛/g'|tr -d "\n"|sed -e "s/.\{$count\}/&\n/g"
