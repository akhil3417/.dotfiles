#!/bin/bash
######################################################################
#Copyright (C) 2021 Kris Occhipinti
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

default_resolution="1920x1080"

function main(){
  display="$(get_display)"
  resolution="$(get_resolution)"
  position="$(get_position)"
  display2="$(get_display)"

  eval xrandr --output $display --mode $resolution $position $display2

}

function error(){
  echo $*
  exit 1
}

function get_position(){
  p="$(echo -e "--right-of\n--left-of\n--above\n--below\n--same-as"|fzf --prompt "Select a position: ")"
  [[ "$p" == "" ]] && error "No Position Selected."
  echo "$p"
}

function get_resolution(){
  r="$(xrandr |grep "^   "|awk '{print $1}'|sort -u;echo "$default_resolution")"
  r="$(echo -e "$r" |fzf --tac --prompt "Select a resolution: ")"
  [[ "$r" == "" ]] && error "No Resolution Selected."
  echo $r
}

function get_display(){
  d="$(xrandr |grep " connected "|awk '{print $1}'|fzf --prompt "Select a display: ")"
  [[ "$d" == "" ]] && error "No Display Selected."
  echo "$d"
}

main $*
