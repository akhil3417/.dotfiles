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

list="$HOME/tmpexpdir/.myshoppinglist.lst"

touch "$list"
red=`echo -en "\e[31m"`
normal=`echo -en "\e[0m"`

function main(){
  [[ "$1" == "print" ]] && print_list
  menu
  [[ "$item" ]] || exit 1
  [[ "$item" == "NEW ITEM" ]] && new_item
  [[ "$item" == "QUIT" ]] && exit
  item_select
}

function menu(){
  l=$(sort -u "$list")
  item="$(echo -e "QUIT\nNEW ITEM\n$l" |fzf)"
}

function print_list(){
  sort -u "$list"
  exit
}

function new_item(){
  read -p "New Item: " new_item
  echo "$new_item" >> $list
  main
}

function item_select(){
  read -n1 -p "Do you want to remove '${red}$item${normal}' from the list? [Y/n]: " a
  echo ""
  [[ "$a" != "n" ]] && sed -i "/^$item$/d" "$list"
  main
}

main $*
