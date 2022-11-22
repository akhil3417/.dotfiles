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

#this script modifies exif values of an image
#such as the GPSZAccuracy
#based on info found here:
#https://exiftool.org/metafiles.html

if [[ $* < 1 ]]
then
  echo "Useage: $0 <image> <value1> <value 2>"
  echo "Example: $0 100_10_01.jpg 5.5 3.3"
  exit 1
fi

img="$1"
gpsz="$2"
gpsxy="$3"

#display original value
echo "Original Value:"
exiftool -s $img | grep GPS|grep Accuracy

#dump xmp data to xml formatted file
exiftool -xmp -b "$img" > DST.xmp
gpszo="$(grep "Camera:GPSZAccuracy" DST.xmp)"
gpszn="<Camera:GPSZAccuracy>$gpsz</Camera:GPSZAccuracy>"
gpsxyo="$(grep "Camera:GPSXYAccuracy" DST.xmp)"
gpsxyn="<Camera:GPSXYAccuracy>$gpsxy</Camera:GPSXYAccuracy>"

#update value
sed -i "s|$gpszo|$gpszn|g;s|$gpsxyo|$gpsxyn|g" DST.xmp

#restore it to img
exiftool -tagsfromfile DST.xmp -xmp "$img"

echo "New Value:"
exiftool -s $img | grep GPS|grep Accuracy
