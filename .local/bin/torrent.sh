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

#search and download torrents
#requirements - fzf aria2c

url="https://thepiratebay.party/search"

[[ $1 ]] && q="$*" || read -p "Enter Search Query: " q

echo "$url/$q"
page="$(wget -qO- "$url/$q")"
list="$(echo "$page"|grep magnet|grep -v '<meta'|sed 's/href="magnet/\nmagnet/g'|grep magnet|cut -d\" -f1|awk -F\& '{print $2 "|" $1}'|tr "+" " "|sed 's/dn=//g')"

selection="$(echo -e "$list"|cut -d\| -f1|fzf)"

[[ $selection ]] || exit 1

#display File Size and Seeds
title="$(echo -e "$selection"|tr " " "+")"
echo -n "$page"|grep "$title" -A2|tail -n2 |sed 's/&nbsp;/ /g'|cut -d\> -f2|cut -d\< -f1|tr "\n" " "
echo "Seeds"

magnet="$(echo -e "$list"|grep "$selection"|cut -d\| -f2)"

[[ $magnet ]] || exit 1
echo ": $(date +%s):0;aria2c --seed-time=1 '$magnet'" >> $HOME/.zsh_history
echo "$magnet"
# aria2c --seed-time=1 "$magnet"
