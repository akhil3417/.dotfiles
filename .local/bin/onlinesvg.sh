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
#downloads 10 random names and converts them to svg
#Be sure to download a font file and change the font var
#sudo apt install potrace imagemagick
font="fonts.ttf"
url="https://randomuser.me/api/?results=10&format=csv"
wget "$url" -qO-|cut -d\, -f3,4|tr "," " " |while read name
do
    convert -size 600x100 xc:white -font "$font" -pointsize 72 -fill black -draw "text 25,65 '$name'" "$name.bmp"
    potrace -s "$name.bmp" -o "$name.svg"
    rm "$name.bmp"
done
