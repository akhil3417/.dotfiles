### ADDING TO THE PATH
# First line removes the path; second line sets it.  Without the first line,
# your path gets massive and fish becomes very slow.
set -e fish_user_paths
set -U fish_user_paths $HOME/.local/bin $HOME/Applications $fish_user_paths

### EXPORT ###
set fish_greeting                                 # Supresses fish's intro message
set TERM "xterm-256color"                         # Sets the terminal type
set EDITOR "emacsclient -t -a ''"                 # $EDITOR use Emacs in terminal
set VISUAL "emacsclient -c -a emacs"              # $VISUAL use Emacs in GUI mode
export HISTCONTROL=ignorespace

export LIBGL_DRI3_DISABLE=1
# Use the iHD driver for media
export LIBVA_DRIVER_NAME=iHD
# export LIBGL_DRI3_DISABLE=1
#for mspylsp
# export DOTNET_ROOT=$HOME/.dotnet
# export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools
# export MB_CONFIG=~/.config/mbsync/config
### SET MANPAGER
### Uncomment only one of these!

### "bat" as manpager
# set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

### "vim" as manpager
# export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

### "nvim" as manpager
# export MANPAGER="nvim -c 'set ft=man' -"

if test -x (command -v fzf) && test -e "$HOME/.config/fzf/key-bindings.fish"
   source "$HOME/.config/fzf/key-bindings.fish"
   fzf_key_bindings
end

# Source aliases and abbreviations
source "$HOME/.config/fish/fish_aliases"
source "$HOME/.config/fish/fish_shortcuts"

# The following are modified in fzf/keybindings.fish
set --erase FZF_CTRL_T_COMMAND
set --erase FZF_ALT_C_COMMAND
set --erase FZF_CTRL_T_OPTS
set --erase FZF_ALT_C_OPTS
set -x FZF_CTRL_R_OPTS "--preview='echo {} | fold' --preview-window=up:3"
# set -g FZF_CTRL_T_COMMAND="command fd --type f --type d --type l -L -i --hidden -E .git \$dir"

function fzf-cdhist-widget -d 'cd to one of the previously visited locations'
	# Clear non-existent folders from cdhist.
	set -l buf
	for i in (seq 1 (count $dirprev))
		set -l dir $dirprev[$i]
		if test -d $dir
			set buf $buf $dir
		end
	end
	set dirprev $buf
	string join \n $dirprev | tac | sed 1d | eval (__fzfcmd) +m --tiebreak=index --toggle-sort=ctrl-r --query=\'$argv\' $FZF_CDHIST_OPTS | read -l result
	[ "$result" ]; and cd $result
	commandline -f repaint
end

function fzf-cd-home-widget -d "Change directory starting from home"
    set -lx FZF_ALT_C_COMMAND "
    command fd . --type d --hidden -L -i -E .git $HOME 2>/dev/null"
    fzf-cd-widget
end

function bind_bang
  switch (commandline -t)
  case "!"
    commandline -t $history[1]; commandline -f repaint
  case "*"
    commandline -i !
  end
end

function bind_dollar
  switch (commandline -t)
  case "!"
    commandline -t ""
    commandline -f history-token-search-backward
  case "*"
    commandline -i '$'
  end
end
# enables $?
function bind_status
  commandline -i (echo '$status')
end


# enables $$
function bind_self
  commandline -i (echo '%self')
end

# enable keybindings
function fish_user_key_bindings
  bind '$?' bind_status
  bind '$$' bind_self
  bind ! bind_bang
  bind '$' bind_dollar
  bind \eC fzf-cd-home-widget
end
[ -f ~/.fzf.colors ] && source ~/.fzf.colors

function sendq
  while read url
    xdg-open "$url" >/dev/null 2>&1
  end
end
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# eval /opt/miniconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

### "vim" as manpager
# set -x MANPAGER '/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

### "nvim" as manpager
# set -x MANPAGER "nvim -c 'set ft=man' -"

### SET EITHER DEFAULT EMACS MODE OR VI MODE ###
function fish_user_key_bindings
  # fish_default_key_bindings
  fish_vi_key_bindings
end
### END OF VI MODE ###

### AUTOCOMPLETE AND HIGHLIGHT COLORS ###
set fish_color_normal brcyan
set fish_color_autosuggestion '#7d7d7d'
set fish_color_command brcyan
set fish_color_error '#ff6c6b'
set fish_color_param brcyan

### SPARK ###
set -g spark_version 1.0.0

complete -xc spark -n __fish_use_subcommand -a --help -d "Show usage help"
complete -xc spark -n __fish_use_subcommand -a --version -d "$spark_version"
complete -xc spark -n __fish_use_subcommand -a --min -d "Minimum range value"
complete -xc spark -n __fish_use_subcommand -a --max -d "Maximum range value"

function spark -d "sparkline generator"
    if isatty
        switch "$argv"
            case {,-}-v{ersion,}
                echo "spark version $spark_version"
            case {,-}-h{elp,}
                echo "usage: spark [--min=<n> --max=<n>] <numbers...>  Draw sparklines"
                echo "examples:"
                echo "       spark 1 2 3 4"
                echo "       seq 100 | sort -R | spark"
                echo "       awk \\\$0=length spark.fish | spark"
            case \*
                echo $argv | spark $argv
        end
        return
    end

    command awk -v FS="[[:space:],]*" -v argv="$argv" '
        BEGIN {
            min = match(argv, /--min=[0-9]+/) ? substr(argv, RSTART + 6, RLENGTH - 6) + 0 : ""
            max = match(argv, /--max=[0-9]+/) ? substr(argv, RSTART + 6, RLENGTH - 6) + 0 : ""
        }
        {
            for (i = j = 1; i <= NF; i++) {
                if ($i ~ /^--/) continue
                if ($i !~ /^-?[0-9]/) data[count + j++] = ""
                else {
                    v = data[count + j++] = int($i)
                    if (max == "" && min == "") max = min = v
                    if (max < v) max = v
                    if (min > v ) min = v
                }
            }
            count += j - 1
        }
        END {
            n = split(min == max && max ? "▅ ▅" : "▁ ▂ ▃ ▄ ▅ ▆ ▇ █", blocks, " ")
            scale = (scale = int(256 * (max - min) / (n - 1))) ? scale : 1
            for (i = 1; i <= count; i++)
                out = out (data[i] == "" ? " " : blocks[idx = int(256 * (data[i] - min) / scale) + 1])
            print out
        }
    '
end
### END OF SPARK ###


### FUNCTIONS ###
# Spark functions
function letters
    cat $argv | awk -vFS='' '{for(i=1;i<=NF;i++){ if($i~/[a-zA-Z]/) { w[tolower($i)]++} } }END{for(i in w) print i,w[i]}' | sort | cut -c 3- | spark | lolcat
    printf  '%s\n' 'abcdefghijklmnopqrstuvwxyz'  ' ' | lolcat
end

function commits
    git log --author="$argv" --format=format:%ad --date=short | uniq -c | awk '{print $1}' | spark | lolcat
end

# Functions needed for !! and !$
function __history_previous_command
  switch (commandline -t)
  case "!"
    commandline -t $history[1]; commandline -f repaint
  case "*"
    commandline -i !
  end
end

function __history_previous_command_arguments
  switch (commandline -t)
  case "!"
    commandline -t ""
    commandline -f history-token-search-backward
  case "*"
    commandline -i '$'
  end
end
# The bindings for !! and !$
if [ $fish_key_bindings = "fish_vi_key_bindings" ];
  bind -Minsert ! __history_previous_command
  bind -Minsert '$' __history_previous_command_arguments
else
  bind ! __history_previous_command
  bind '$' __history_previous_command_arguments
end

# Function for creating a backup file
# ex: backup file.txt
# result: copies file as file.txt.bak
function backup --argument filename
    cp $filename $filename.bak
end

# Function for copying files and directories, even recursively.
# ex: copy DIRNAME LOCATIONS
# result: copies the directory and all of its contents.
function copy
    set count (count $argv | tr -d \n)
    if test "$count" = 2; and test -d "$argv[1]"
	set from (echo $argv[1] | trim-right /)
	set to (echo $argv[2])
        command cp -r $from $to
    else
        command cp $argv
    end
end
#download partial youtube videos
#https://gist.github.com/anakaiti/6c02ba44f2a0db260803b5526aceb511
function youtube -d 'Download partial youtube videos' -a url start duration out
    set mp4 (youtube-dl -g -f 22 $url)
    set -q out; or set out 'out.mp4'
    ffmpeg -ss $start -i $mp4 -t $duration -c copy $out
end
# Function for printing a column (splits input on whitespace)
# ex: echo 1 2 3 | coln 3
# output: 3
function coln
    while read -l input
        echo $input | awk '{print $'$argv[1]'}'
    end
end

# Function for printing a row
# ex: seq 3 | rown 3
# output: 3
function rown --argument index
    sed -n "$index p"
end

# Function for ignoring the first 'n' lines
# ex: seq 10 | skip 5
# results: prints everything but the first 5 lines
function skip --argument n
    tail +(math 1 + $n)
end

# Function for taking the first 'n' lines
# ex: seq 10 | take 5
# results: prints only the first 5 lines
function take --argument number
    head -$number
end

# Function for org-agenda
function org-search -d "send a search string to org-mode"
    set -l output (/usr/bin/emacsclient -a "" -e "(message \"%s\" (mapconcat #'substring-no-properties \
        (mapcar #'org-link-display-format \
        (org-ql-query \
        :select #'org-get-heading \
        :from  (org-agenda-files) \
        :where (org-ql--query-string-to-sexp \"$argv\"))) \
        \"
    \"))")
    printf $output
end
###autojump
###
# function j
#     set new_path (autojump $argv)

#     if test -d "$new_path"
#         echo $new_path
#         cd "$new_path"
#     else
#         echo "autojump: directory '$argv' not found"
#         echo "Try \`autojump --help\` for more information."
#         false
#     end
# end

. /usr/share/autojump/autojump.fish
### END OF FUNCTIONS ###



### RANDOM COLOR SCRIPT ###
# Get this script from my GitLab: gitlab.com/dwt1/shell-color-scripts
# Or install it from the Arch User Repository: shell-color-scripts
# colorscript random

### SETTING THE STARSHIP PROMPT ###
starship init fish | source
# Import the colors.
# . "$HOME/.cache/wal/colors.sh"

# Create the alias.
# alias dmenu='dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"'
cat ~/.cache/wal/sequences &
# source ~/.cache/wal/colors.fish

