#     _    _    _     _ _
#    / \  | | _| |__ (_) |   Akhil
#   / _ \ | |/ / '_ \| | |   http://www.youtube.com/c/italented
#  / ___ \|   <| | | | | |   http://www.gitlab.com/akhil3417/
# /_/   \_\_|\_\_| |_|_|_|

### EXPORT
export TERM="xterm-256color"            # getting proper colors
export HISTCONTROL=ignoredups:erasedups # no duplicate entries
export ALTERNATE_EDITOR=""              # setting for emacsclient
export EDITOR="emacsclient -t -a ''"    # $EDITOR use Emacs in terminal
export VISUAL="emacsclient -c -a emacs" # $VISUAL use Emacs in GUI mode
export HISTCONTROL=ignorespace
export MPD_HOST=/home/shiva/.config/mpd/socket  # for some reason only absolute path works
export LC_ALL=en_US.UTF-8
# export MB_CONFIG=~/.config/mbsync/config
### SET MANPAGER
### Uncomment only one of these!

### "bat" as manpager --fucks up man-pages in void linux
# export MANPAGER="sh -c 'col -bx | bat -l man -p'"

### "vim" as manpager
# export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

### "nvim" as manpager
# export MANPAGER="nvim -c 'set ft=man' -"

### SET VI MODE ###
# Comment this line out to enable default emacs-like bindings
set -o vi
bind -m vi-command 'Control-l: clear-screen'
bind -m vi-insert 'Control-l: clear-screen'

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

### PROMPT
# This is commented out if using starship prompt
# PS1='[\u@\h \W]\$ '

### PATH
if [ -d "$HOME/.bin" ]; then
  PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ]; then
  PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/Applications" ]; then
  PATH="$HOME/Applications:$PATH"
fi

### SETTING OTHER ENVIRONMENT VARIABLES
if [ -z "$XDG_CONFIG_HOME" ]; then
  export XDG_CONFIG_HOME="$HOME/.config"
fi
if [ -z "$XDG_DATA_HOME" ]; then
  export XDG_DATA_HOME="$HOME/.local/share"
fi
if [ -z "$XDG_CACHE_HOME" ]; then
  export XDG_CACHE_HOME="$HOME/.cache"
fi
export XMONAD_CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/xmonad" # xmonad.hs is expected to stay here
export XMONAD_DATA_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/xmonad"
export XMONAD_CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/xmonad"

### CHANGE TITLE OF TERMINALS
case ${TERM} in
  xterm* | rxvt* | Eterm* | aterm | kterm | gnome* | alacritty | st | konsole*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
    ;;
  screen*)
    PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
    ;;
esac

#### autojump setup
. /usr/share/autojump/autojump.bash

### SHOPT
shopt -s autocd  # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend     # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s checkwinsize   # checks term size when bash regains control

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

### COUNTDOWN

cdown() {
  N=$1
  while [[ $((--N)) ]] >0; do
    echo "$N" | figlet -c | lolcat && sleep 1
  done
}

### ARCHIVE EXTRACTION
# usage: ex <file>
ex() {
  if [ -f $1 ]; then
    case $1 in
      *.tar.bz2) tar xjf $1 ;;
      *.tar.gz) tar xzf $1 ;;
      *.bz2) bunzip2 $1 ;;
      *.rar) unrar x $1 ;;
      *.gz) gunzip $1 ;;
      *.tar) tar xf $1 ;;
      *.tbz2) tar xjf $1 ;;
      *.tgz) tar xzf $1 ;;
      *.zip) unzip $1 ;;
      *.Z) uncompress $1 ;;
      *.7z) 7z x $1 ;;
      *.deb) ar x $1 ;;
      *.tar.xz) tar xf $1 ;;
      *.tar.zst) unzstd $1 ;;
      *) echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

### ALIASES ###

# root privileges
alias doas="doas --"
alias sudo="doas"

# navigation
up() {
  local d=""
  local limit="$1"

  # # Default to limit of 1
  # if [ -z "$limit" ] || [ "$limit" -le 0 ]; then
  #   limit=1
  # fi
  # for ((i = 1; i <= limit; i++)); do
  #   d="../$d"
  # done

  # perform cd. Show error if cd fails
  if ! cd "$d"; then
    echo "Couldn't go up $limit dirs."
  fi
}
pipdepuninstall() {
  pip install -q pipdeptree
  pipdeptree -p$1 -fj | jq ".[] | .package.key" | xargs pip uninstall -y
}
# vim and emacs
# alias vim="nvim"
alias em="/usr/bin/emacs -nw"
alias emacs="emacsclient -c -a 'emacs'"
# alias doom="~/.emacs.d/bin/doom"
alias doom="~/doom-emacs/bin/doom"

#void linux aliases
alias install='sudo xbps-install '
alias remove='sudo xbps-remove -Rv'
alias update='sudo xbps-install -S'
alias upgrade='sudo xbps-install -Suv'
alias findp='xbps-query -Rs'
alias orphan='sudo xbps-remove -ov'
alias clean='sudo xbps-remove -oOv'
alias flatpak='flatpak --user'
alias findpfzf='xbps-query -Rs "*" | fzf -i --exact --prompt="Select package(s) to install: " --multi | awk "{print \$2}" | xargs -ro sudo xbps-install -S'
alias b='pushd $(dirs -v | fzf)'
alias dirs='dirs -v'

# Changing "ls" to "exa"
# alias ls='exa -al --color=always --group-directories-first' # my preferred listing
# alias la='exa -a --color=always --group-directories-first'  # all files and dirs
# alias ll='exa -l --color=always --group-directories-first'  # long format
# alias lt='exa -aT --color=always --group-directories-first' # tree listing
# alias l.='exa -a | egrep "^\."'

# pacman and yay
# alias pacsyu='sudo pacman -Syyu'                 # update only standard pkgs
# alias yaysua='yay -Sua --noconfirm'              # update only AUR pkgs (yay)
# alias yaysyu='yay -Syu --noconfirm'              # update standard pkgs and AUR pkgs (yay)
# alias parsua='paru -Sua --noconfirm'             # update only AUR pkgs (paru)
# alias parsyu='paru -Syu --noconfirm'             # update standard pkgs and AUR pkgs (paru)
# alias unlock='sudo rm /var/lib/pacman/db.lck'    # remove pacman lock
# alias cleanup='sudo pacman -Rns (pacman -Qtdq)'  # remove orphaned packages

# get fastest mirrors
# alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
# alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
# alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
# alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# confirm before overwriting something
alias cp="cp -i"
alias rsync='mv -i'
# alias rm='rm -i'
alias rm='trash -v'

# adding flags
alias df='df -h'     # human-readable sizes
alias free='free -m' # show sizes in MB
alias lynx='lynx -cfg=~/.lynx/lynx.cfg -lss=~/.lynx/lynx.lss -vikeys'
alias vifm='./.config/vifm/scripts/vifmrun'
alias ncmpcpp='ncmpcpp ncmpcpp_directory=$HOME/.config/ncmpcpp/'
alias mocp='mocp -M "$XDG_CONFIG_HOME"/moc -O MOCDir="$XDG_CONFIG_HOME"/moc'

# ps
alias psa="ps auxf"
alias psgrep="ps aux | grep -v grep | grep -i -e VSZ -e"
alias psmem='ps auxf | sort -nr -k 4'
alias pscpu='ps auxf | sort -nr -k 3'
alias tsp='ts'

# Merge Xresources
alias merge='xrdb -merge ~/.Xresources'

# git
alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias stat='git status' # 'status' is protected name so using 'stat' instead
alias tag='git tag'
alias newtag='git tag -a'

# get error messages from journalctl
alias jctl="journalctl -p 3 -xb"

# gpg encryption
# verify signature for isos
alias gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
# receive the key of a developer
alias gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"

# youtube-dl
alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="youtube-dl --extract-audio --audio-format best "
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
# alias yta-opus="youtube-dl --extract-audio --audio-format opus "
alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "
alias ytv-best="youtube-dl -f bestvideo+bestaudio "

# alias yta-opus="yt-dlp -f 'ba' -x --audio-format opus --embed-thumbnail --embed-subs --embed-metadata --download-archive ~/Music/youtube-dl/download-archive/audios.txt --yes-playlist -o '/home/shiva/Music/youtube-dl/%(title)s-[%(id)s].%(ext)s' "
# alias yta-batchopus="yt-dlp -f 'ba' -x --audio-format opus --embed-thumbnail --embed-subs --embed-metadata --download-archive ~/Music/youtube-dl/download-archive/audios.txt --yes-playlist -o '/home/shiva/Music/youtube-dl/%(title)s-[%(id)s].%(ext)s'  --batch-file= "
alias yta-opus="yt-dlp --extract-audio --audio-format opus  --embed-subs --embed-metadata --download-archive ~/Music/youtube-dl/download-archive/audios.txt --yes-playlist -o '/home/shiva/Music/youtube-dl/%(title)s-[%(id)s].%(ext)s' "
# alias yta-opus="yt-dlp -f 'ba' -x --audio-format opus  --embed-subs --embed-metadata --download-archive ~/Music/youtube-dl/videos.txt --yes-playlist -o '/home/shiva/Music/youtube-dl/%(title)s-[%(id)s].%(ext)s' "
alias yta-batchopus="yt-dlp -f 'ba' -x --audio-format opus  --embed-subs --embed-metadata --download-archive ~/Music/youtube-dl/download-archive/audios.txt --yes-playlist -o '/home/shiva/Music/youtube-dl/%(title)s-[%(id)s].%(ext)s'  --batch-file= "

# switch between shells
# I do not recommend switching default SHELL from bash.
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Now log out.'"

# bare git repo alias for dotfiles
alias config="/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME"

# termbin
alias tb="nc termbin.com 9999"

# the terminal rickroll
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'

# Unlock LBRY tips
alias tips='lbrynet txo spend --type=support --is_not_my_input --blocking'

### DTOS ###
# Copy/paste all content of /etc/dtos over to home folder. A backup of config is created. (Be careful running this!)
alias mydotscopy='[ -d ~/.config ] || mkdir ~/.config && cp -Rf ~/.config ~/.config-backup-$(date +%Y.%m.%d-%H.%M.%S) && cp -rf /etc/mydots/* ~'
# Backup contents of /etc/dtos to a backup folder in $HOME.
alias mydotsbackup='cp -Rf /etc/mydots ~/mydots-backup-$(date +%Y.%m.%d-%H.%M.%S)'

### RANDOM COLOR SCRIPT ###
# Get this script from my GitLab: gitlab.com/dwt1/shell-color-scripts
# Or install it from the Arch User Repository: shell-color-scripts
# colorscript random

### BASH INSULTER ###
if [ -f /etc/bash.command-not-found ]; then
  . /etc/bash.command-not-found
fi

### SETTING THE STARSHIP PROMPT ###
eval "$(starship init bash)"
# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat /home/shiva/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source /home/shiva/.cache/wal/colors-tty.sh
# You can create a function for this in your shellrc (.bashrc, .zshrc).
# wal-tile() {
#   wal -n -i "$@"
#   feh --bg-tile "$(<"/home/shiva/.cache/wal/wal")"
# }

# Import the colors.
. "/home/shiva/.cache/wal/colors.sh"

# Create the alias.
alias dmenu='dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"'
# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
export YTFZF_EXTMENU='rofi -dmenu -fuzzy -width 1000'
export YTFZF_ENABLE_FZF_DEFUALT_OPTS=0
export YTFZF_PLAYER='vlc '
#(YTFZF_PLAYER)
alias chadwm='startx ~/.dotfiles/.config/chadwm/scripts/run.sh'

source /home/shiva/.config/broot/launcher/bash/br
# Use bash-completion, if available
[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] &&
  . /usr/share/bash-completion/bash_completion

pw() {
  export PASSWORD_STORE_CLIP_TIME=8
  export PASSWORD_STORE_X_SELECTION=primary
  pass -c2 $1
  sleep 5
  pass -c $1
  sleep 5
  pass otp -c $1
  exit
}
#for mspylsp
# export LIBGL_DRI3_DISABLE=1
export DOTNET_ROOT=$HOME/.dotnet
export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools
# Use the iHD driver for media
export LIBVA_DRIVER_NAME=iHD


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# __conda_setup="$('/home/shiva/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
# if [ $? -eq 0 ]; then
# eval "$__conda_setup"
# else
# if [ -f "/home/shiva/miniconda3/etc/profile.d/conda.sh" ]; then
# . "/home/shiva/miniconda3/etc/profile.d/conda.sh"
# else
# export PATH="/home/shiva/miniconda3/bin:$PATH"
# fi
# fi
# unset __conda_setup
# <<< conda initialize <<<

# export PATH="$HOME/gitclones/SlymeGPT/chromedriver:$PATH"

# eval $(keychain --eval --quiet id_ed25519)
source ~/.keychain/$HOSTNAME-sh
