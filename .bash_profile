#!/usr/bin/env sh

# ~/.bash_profile fs
#
[[ -f ~/.bashrc ]] && . ~/.bashrc
# gpg has to be started here (or in .xinitrc.exwm), if we want to have encryption in exwm
export EDITOR=emacsclient -c -a 'emacs'

source /home/shiva/.config/broot/launcher/bash/br
