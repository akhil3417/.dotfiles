#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)
# Set fallback cursor.
if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi 
~/.fehbgn 'X'
TY
xsetroot -cursor_name left_ptr

# Set keyboard repeat rate.
xset r rate 300 50

exec xmonad
PS=/tmp/.volume-pipe
[[ -S $PS ]] || mkfifo $PS
XMMPCstop
