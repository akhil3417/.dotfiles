# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401

config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

import os

## Custom CSS for sites
# c.content.user_stylesheets = ["~/.config/qutebrowser/css/apprentice-all-sites.css"]
config.bind(
    "<Ctrl-R>",
    'config-cycle content.user_stylesheets "~/.config/qutebrowser/css/solarized-dark-all-sites.css" "~/.config/qutebrowser/css/darculized-all-sites.css" "~/.config/qutebrowser/css/nord-dark-all-sites.css" ""',
)

config.bind("<Ctrl-w>", "nop", "normal")
## Readline bindings in insert mode
config.bind("<Ctrl-h>", "fake-key <Backspace>", "insert")
config.bind("<Ctrl-a>", "fake-key <Home>", "insert")
config.bind("<Ctrl-e>", "fake-key <End>", "insert")
config.bind("<Ctrl-b>", "fake-key <Left>", "insert")
config.bind("<Mod1-b>", "fake-key <Ctrl-Left>", "insert")
config.bind("<Ctrl-f>", "fake-key <Right>", "insert")
config.bind("<Mod1-f>", "fake-key <Ctrl-Right>", "insert")
config.bind("<Ctrl-p>", "fake-key <Up>", "insert")
config.bind("<Ctrl-n>", "fake-key <Down>", "insert")
config.bind("<Mod1-d>", "fake-key <Ctrl-Delete>", "insert")
config.bind("<Ctrl-d>", "fake-key <Delete>", "insert")
config.bind("<Ctrl-w>", "fake-key <Ctrl-Backspace>", "insert")
config.bind("<Ctrl-u>", "fake-key <Shift-Home><Delete>", "insert")
config.bind("<Ctrl-k>", "fake-key <Shift-End><Delete>", "insert")
# config.bind('<Ctrl-x><Ctrl-e>', 'open-editor', 'insert')
config.bind("<Ctrl-s>", "edit-text", "insert")

## Userscript bindings
# Password filling
config.bind("<,><f><f>", "spawn --userscript qute-pass")
config.bind("<,><f><u>", "spawn --userscript qute-pass --username-only")
config.bind("<,><f><p>", "spawn --userscript qute-pass --password-only")
config.bind("<,><f><o>", "spawn --userscript qute-pass --otp-only")
config.bind("<,><z><l>", "hint links userscript qute-zotero")
config.bind(",Z", "spawn --userscript qute-zotero")
c.aliases.update({"zotero": "spawn --userscript qute-zotero"})
config.bind(
    "<,><a><a>",
    "spawn --userscript qute-capture read -f ~/read-later.org -H Read-Later",
)
# Read later via wallabag
config.bind(",rl", "hint links spawn --userscript qute-readlater {hint-url}")
config.bind(",rL", "spawn --userscript qute-readlater")
c.aliases.update({"readlater": "spawn --userscript qute-readlater"})

## Bindings for normal mode
config.bind("<Ctrl-m>", "hint mpv_type spawn mpv {hint-url}")
config.bind("<Ctrl-Shift-M>", "spawn mpv {url}")
config.bind("<Ctrl-Alt-m>", "hint mpv_type spawn umpv_last {hint-url}")
config.bind("<Ctrl-Alt-Shift-M>", "spawn umpv_last {url}")
config.bind("<Alt-m>", "hint mpv_type spawn umpv {hint-url}")
config.bind("<Alt-Shift-M>", "spawn umpv {url}")

config.bind(";mr", "hint --rapid mpv_type spawn umpv {hint-url}")
config.bind(";mm", "spawn umpv {url}")
config.bind(";mo", "hint mpv_type spawn umpv {hint-url}")
config.bind(";mh", "hint mpv_type spawn umpv --profile=protocol-hd-video {hint-url}")
config.bind(";ma", "hint mpv_type spawn umpv --video=no {hint-url}")

config.bind(";mM", "spawn mpv {url}")
config.bind(";mO", "hint mpv_type spawn mpv {hint-url}")
config.bind(";mH", "hint mpv_type spawn mpv --profile=protocol-hd-video {hint-url}")
config.bind(";mA", "hint mpv_type spawn mpv --video=no --force-window=yes {hint-url}")
config.bind("<Alt-E>", "edit-text")

config.bind("M", "hint links spawn mpv {hint-url}")
config.bind("Z", "hint links spawn st -e youtube-dl {hint-url}")
config.bind("t", "cmd-set-text -s :open -t")
config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind(
    "xx",
    "config-cycle statusbar.show always never;; config-cycle tabs.show always never",
)

# Bindings for cycling through CSS stylesheets from Solarized Everything CSS:
# https://github.com/alphapapa/solarized-everything-css
config.bind(
    ",ap",
    'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""',
)
config.bind(
    ",dr",
    'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""',
)
config.bind(
    ",gr",
    'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""',
)
config.bind(
    ",sd",
    'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""',
)
config.bind(
    ",sl",
    'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""',
)

# Make Ctrl+g quit everything like in Emacs
config.bind("<Ctrl-g>", "leave-mode", mode="insert")
config.bind("<Ctrl-g>", "leave-mode", mode="command")
config.bind("<Ctrl-g>", "leave-mode", mode="prompt")
config.bind("<Ctrl-g>", "leave-mode", mode="hint")
# config.bind('v', 'spawn ~/.dotfiles/bin/umpv {url}')
# config.bind('V', 'hint links spawn ~/.dotfiles/bin/umpv {hint-url}')

# Tweak some keybindings
config.unbind("d")  # Don't close window on lower-case 'd'
config.bind("yy", "yank")

# Vim-style movement keys in command mode
config.bind("<Ctrl-j>", "completion-item-focus --history next", mode="command")
config.bind("<Ctrl-k>", "completion-item-focus --history prev", mode="command")
config.bind(
    "<Ctrl-r>",
    "spawn python "
    + os.environ["HOME"]
    + '/.config/doom/org-roam-protocol-handler.py "{url:pretty}" "{title}"',
)

config.bind(";i", "hint images download")

## Bindings for insert mode
config.bind("<Alt-E>", "edit-text", mode="insert")
config.bind("ed", "download-open")
# config.bind('<Escape>', 'leave-mode', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text {primary}', mode='insert')
# config.bind("'", 'enter-mode jump_mark')
#
# some instresing keybinds
#
# config.bind(',v', 'spawn mpv {url}')
# config.bind(',d', 'spawn ytdl {url}')

# bookmarks
config.bind(",ba", "bookmark-add")
config.bind(",bb", "cmd-set-text -s :bookmark-load")
config.bind(",bl", "bookmark-list")
config.bind(",bj", "bookmark-list --jump")
config.bind(",bt", "cmd-set-text -s :bookmark-load -t")
config.bind(",bw", "cmd-set-text -s :bookmark-load -w")
config.bind(",bql", "cmd-set-text -s :quickmark-load")
config.bind(",bqL", "cmd-set-text -s :quickmark-load -t")
config.bind(",bqs", "quickmark-save")
config.bind(",bqw", "cmd-set-text -s :quickmark-load -w")

# config cycle
config.bind(
    ",cCH",
    "config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",cCh",
    "config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",cCu",
    "config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(",cIH", "config-cycle -p -u *://*.{url:host}/* content.images ;; reload")
config.bind(",cIh", "config-cycle -p -u *://{url:host}/* content.images ;; reload")
config.bind(",cIu", "config-cycle -p -u {url} content.images ;; reload")
config.bind(",cPH", "config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload")
config.bind(",cPh", "config-cycle -p -u *://{url:host}/* content.plugins ;; reload")
config.bind(",cPu", "config-cycle -p -u {url} content.plugins ;; reload")
config.bind(
    ",cSH", "config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload"
)
config.bind(
    ",cSh", "config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload"
)
config.bind(",cSu", "config-cycle -p -u {url} content.javascript.enabled ;; reload")
config.bind(
    ",ccH",
    "config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",cch",
    "config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",ccu",
    "config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(",ch", "back -t")
config.bind(",ciH", "config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload")
config.bind(",cih", "config-cycle -p -t -u *://{url:host}/* content.images ;; reload")
config.bind(",ciu", "config-cycle -p -t -u {url} content.images ;; reload")
config.bind(",cl", "forward -t")
config.bind(
    ",cpH", "config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload"
)
config.bind(",cph", "config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload")
config.bind(",cpu", "config-cycle -p -t -u {url} content.plugins ;; reload")
config.bind(
    ",csH",
    "config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload",
)
config.bind(
    ",csh",
    "config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload",
)
config.bind(",csu", "config-cycle -p -t -u {url} content.javascript.enabled ;; reload")

# downloads
config.bind(",da", "download-cancel")
config.bind(",dd", "download")
config.bind(",dc", "download-clear")
config.bind(",dy", "spawn ytdl {url}")

# dev tools
config.bind(",Dd", "devtools")
config.bind(",Df", "devtools-focus")
config.bind(",Dc", "devtools left")
config.bind(",Dt", "devtools bottom")
config.bind(",Ds", "devtools top")
config.bind(",Dr", "devtools right")
config.bind(",Dw", "devtools window")

# save
config.bind("fs", "save")

# hints
config.bind(",hd", "hint links download")
config.bind(",hh", "hint")
config.bind(",hH", "hint all hover")
config.bind(",hii", "hint images")
config.bind(",hiI", "hint images tab")
config.bind(",hIi", "hint inputs")
config.bind(",hIf", "hint inputs --first")
config.bind(",hO", "hint links fill :open -t -r {hint-url}")
config.bind(",ho", "hint links fill :open {hint-url}")
config.bind(",hR", "hint --rapid links window")
config.bind(",hr", "hint --rapid links tab-bg")
config.bind(",htb", "hint all tab-bg")
config.bind(",htf", "hint all tab-fg")
config.bind(",htt", "hint all tab")
config.bind(",hw", "hint all window")
config.bind(",hy", "hint links yank")
config.bind(",hY", "hint links yank-primary")
# Bindings for hint mode
config.bind("<Ctrl-B>", "hint all tab-bg", mode="hint")
config.bind("<Ctrl-F>", "hint links", mode="hint")
config.bind("<Ctrl-R>", "hint --rapid links tab-bg", mode="hint")
config.bind("<Escape>", "mode-leave", mode="hint")
config.bind("<Return>", "hint-follow", mode="hint")

# Move
config.bind("<Ctrl-PgDown>", "tab-next")
config.bind("<Ctrl-C>", "back -w")
config.bind("<Ctrl-R>", "forward -w")
config.bind("<Ctrl-h>", "home")
config.bind("T", "tab-next")
config.bind("S", "tab-prev")
config.bind("C", "back")
config.bind("R", "forward")

# cmd
config.bind(",sb", "cmd-set-text -s :bind")
config.bind(",st", "cmd-set-text -s :set -t")
config.bind(",ss", "set")
config.bind(",sS", "cmd-set-text -s :set")

# open
config.bind("<Ctrl-N>", "open -w")
config.bind("<Ctrl-Shift-N>", "open -p")
config.bind("<Ctrl-T>", "open -t")
config.bind(",ob", "cmd-set-text -s :open -b")
config.bind(",oB", "cmd-set-text :open -b -r {url:pretty}")
config.bind(",oP", "cmd-set-text :open -t -r {url:pretty}")
config.bind(",ott", "open -t")
config.bind(",otT", "cmd-set-text -s :open -t")
config.bind(",ow", "cmd-set-text -s :open -w")
config.bind(",oW", "cmd-set-text :open -w {url:pretty}")
config.bind(",occ", "open -- {clipboard}")
config.bind(",ocC", "open -t -- {clipboard}")
config.bind(",ocp", "open -- {primary}")
config.bind(",ocP", "open -t -- {primary}")
config.bind(",ocw", "open -w -- {clipboard}")
config.bind(",ocW", "open -w -- {primary}")
config.bind("o", "cmd-set-text -s :open")
config.bind("O", "cmd-set-text :open {url:pretty}")

# tabs
config.bind("<Alt-1>", "tab-focus 1")
config.bind("<Alt-2>", "tab-focus 2")
config.bind("<Alt-3>", "tab-focus 3")
config.bind("<Alt-4>", "tab-focus 4")
config.bind("<Alt-5>", "tab-focus 5")
config.bind("<Alt-6>", "tab-focus 6")
config.bind("<Alt-7>", "tab-focus 7")
config.bind("<Alt-8>", "tab-focus 8")
config.bind("<Alt-9>", "tab-focus -1")
config.bind("<Alt-m>", "tab-mute")
config.bind("<Ctrl-Tab>", "tab-focus last")
config.bind("<Ctrl-W>", "tab-close")
config.bind(",tT", "tab-move +")
config.bind(",tS", "tab-move -")
config.bind(",tn", "tab-next")
config.bind(",tp", "tab-prev")
config.bind(",t«", "tab-focus -1")
config.bind(",t»", "tab-focus 1")
config.bind(",tC", "tab-clone")
config.bind(",tD", "tab-only")
config.bind(",td", "tab-close")
config.bind(",tf", "cmd-set-text -sr :tab-focus")
config.bind(",tg", "tab-give")
config.bind(",tl", "tab-focus last")
config.bind(",tm", "tab-move")
config.bind(",tP", "tab-pin")
config.bind(",ts", "cmd-set-text -s :tab-select")

# scoll
config.bind("G", "scroll-to-perc")
config.bind("gg", "scroll-to-perc 0")
# config.bind('c',        'scroll left')
# config.bind('t',        'scroll down')
# config.bind('s',        'scroll up')
# config.bind('r',        'scroll right')

config.bind("h", "scroll left")
config.bind("j", "scroll down")
config.bind("k", "scroll up")
config.bind("l", "scroll right")

config.bind("<Ctrl-F>", "scroll-page 0 1")
config.bind("<Ctrl-B>", "scroll-page 0 -1")
config.bind("<Ctrl-D>", "scroll-page 0 0.5")
config.bind("<Ctrl-U>", "scroll-page 0 -0.5")

# navigate
config.bind(",nd", "navigate decrement")
config.bind(",ni", "navigate increment")
config.bind(",nn", "navigate prev")
config.bind(",nN", "navigate next -t")
config.bind(",np", "navigate next")
config.bind(",nP", "navigate prev -t")
config.bind(",nu", "navigate up")
config.bind(",nU", "navigate up -t")

# search
config.bind("n", "search-next")
config.bind("N", "search-prev")

# print
config.bind("<Ctrl-Alt-p>", "print")

config.bind(",qq", "quit")
config.bind(",qs", "quit --save")
config.bind(",qw", "close")
config.bind("<Ctrl-Q>", "quit")

# reload
config.bind(",rr", "reload")
config.bind(",rR", "reload -f")
config.bind("<F5>", "reload")
config.bind("<Ctrl-F5>", "reload -f")

# view
config.bind(",vh", "history")
config.bind(",vs", "view-source")

# yank
config.bind("yd", "yank domain")
config.bind("yD", "yank domain -s")
config.bind("yi", "yank inline [{title}]({url})")
config.bind("yI", "yank inline [{title}]({url}) -s")
config.bind("yp", "yank pretty-url")
config.bind("yP", "yank pretty-url -s")
config.bind("yt", "yank title")
config.bind("yT", "yank title -s")
config.bind("yy", "yank")
config.bind("yY", "yank -s")

config.bind("<Escape>", "clear-keychain ;; search ;; fullscreen --leave")

config.bind("+", "zoom-in")
config.bind("-", "zoom-out")
config.bind("=", "zoom")

config.bind("?", "cmd-set-text ?")
config.bind("/", "cmd-set-text /")
config.bind(":", "cmd-set-text :")
config.bind(".", "repeat-command")

config.bind("<Ctrl-Shift-Tab>", "nop")
config.bind("<Ctrl-s>", "stop")
config.bind("<F11>", "fullscreen")

config.bind("<Return>", "selection-follow")
config.bind("<Ctrl-Return>", "selection-follow -t")

config.bind("<back>", "back")
config.bind("<forward>", "forward")


config.bind("<Ctrl-V>", "mode-enter passthrough")
config.bind("'", "mode-enter jump_mark")
config.bind("v", "mode-enter caret")
config.bind("V", "mode-enter caret ;; selection-toggle --line")
config.bind("`", "mode-enter set_mark")
config.bind("i", "mode-enter insert")

config.bind("q", "macro-record")
config.bind("@", "macro-run")

config.bind("U", "undo -w")
config.bind("<Ctrl-Shift-T>", "undo")
config.bind("u", "undo")

# Bindings for caret mode
config.bind("C", "scroll left", mode="caret")
config.bind("T", "scroll down", mode="caret")
config.bind("S", "scroll up", mode="caret")
config.bind("R", "scroll right", mode="caret")
config.bind("h", "move-to-prev-char", mode="caret")
config.bind("j", "move-to-next-line", mode="caret")
config.bind("k", "move-to-prev-line", mode="caret")
config.bind("l", "move-to-next-char", mode="caret")

config.bind("$", "move-to-end-of-line", mode="caret")
config.bind("0", "move-to-start-of-line", mode="caret")
config.bind("<Ctrl-Space>", "selection-drop", mode="caret")
config.bind("<Escape>", "mode-leave", mode="caret")
config.bind("<Return>", "yank selection", mode="caret")
config.bind("<Space>", "selection-toggle", mode="caret")
config.bind("v", "selection-toggle", mode="caret")
config.bind("V", "selection-toggle --line", mode="caret")
config.bind("y", "yank selection", mode="caret")
config.bind("Y", "yank selection -s", mode="caret")
config.bind("[", "move-to-start-of-prev-block", mode="caret")
config.bind("]", "move-to-start-of-next-block", mode="caret")
config.bind("{", "move-to-end-of-prev-block", mode="caret")
config.bind("}", "move-to-end-of-next-block", mode="caret")
config.bind("b", "move-to-prev-word", mode="caret")
config.bind("e", "move-to-end-of-word", mode="caret")
config.bind("gg", "move-to-start-of-document", mode="caret")
config.bind("G", "move-to-end-of-document", mode="caret")
config.bind("n", "mode-enter normal", mode="caret")
config.bind("o", "selection-reverse", mode="caret")
config.bind("w", "move-to-next-word", mode="caret")

# Bindings for command mode
config.bind("<Alt-B>", "rl-backward-word", mode="command")
config.bind("<Alt-Backspace>", "rl-backward-kill-word", mode="command")
config.bind("<Alt-D>", "rl-kill-word", mode="command")
config.bind("<Alt-F>", "rl-forward-word", mode="command")
config.bind("<Ctrl-?>", "rl-delete-char", mode="command")
config.bind("<Ctrl-A>", "rl-beginning-of-line", mode="command")
config.bind("<Ctrl-B>", "rl-backward-char", mode="command")
config.bind("<Ctrl-C>", "completion-item-yank", mode="command")
config.bind("<Ctrl-D>", "completion-item-del", mode="command")
config.bind("<Ctrl-E>", "rl-end-of-line", mode="command")
config.bind("<Ctrl-F>", "rl-forward-char", mode="command")
config.bind("<Ctrl-H>", "rl-backward-delete-char", mode="command")
config.bind("<Ctrl-K>", "rl-kill-line", mode="command")
config.bind("<Ctrl-N>", "command-history-next", mode="command")
config.bind("<Ctrl-P>", "command-history-prev", mode="command")
config.bind("<Ctrl-Return>", "command-accept --rapid", mode="command")
config.bind("<Ctrl-Shift-C>", "completion-item-yank --sel", mode="command")
config.bind("<Ctrl-Shift-Tab>", "completion-item-focus prev-category", mode="command")
config.bind("<Ctrl-Tab>", "completion-item-focus next-category", mode="command")
config.bind("<Ctrl-U>", "rl-unix-line-discard", mode="command")
config.bind("<Ctrl-W>", "rl-unix-word-rubout", mode="command")
config.bind("<Ctrl-Y>", "rl-yank", mode="command")
config.bind("<Down>", "completion-item-focus --history next", mode="command")
config.bind("<Escape>", "mode-leave", mode="command")
config.bind("<PgDown>", "completion-item-focus next-page", mode="command")
config.bind("<PgUp>", "completion-item-focus prev-page", mode="command")
config.bind("<Return>", "command-accept", mode="command")
config.bind("<Shift-Delete>", "completion-item-del", mode="command")
config.bind("<Shift-Tab>", "completion-item-focus prev", mode="command")
config.bind("<Tab>", "completion-item-focus next", mode="command")
config.bind("<Up>", "completion-item-focus --history prev", mode="command")

# Bindings for insert mode
config.bind("<Ctrl-E>", "edit-text", mode="insert")
config.bind("<Escape>", "mode-leave", mode="insert")
config.bind("<Shift-Escape>", "fake-key <Escape>", mode="insert")
config.bind("<Shift-Ins>", "insert-text -- {primary}", mode="insert")

# Bindings for passthrough mode
config.bind("<Shift-Escape>", "mode-leave", mode="passthrough")

# Bindings for prompt mode
config.bind("<Alt-B>", "rl-backward-word", mode="prompt")
config.bind("<Alt-Backspace>", "rl-backward-kill-word", mode="prompt")
config.bind("<Alt-D>", "rl-kill-word", mode="prompt")
config.bind("<Alt-F>", "rl-forward-word", mode="prompt")
config.bind("<Alt-Shift-Y>", "prompt-yank --sel", mode="prompt")
config.bind("<Alt-Y>", "prompt-yank", mode="prompt")
config.bind("<Ctrl-?>", "rl-delete-char", mode="prompt")
config.bind("<Ctrl-A>", "rl-beginning-of-line", mode="prompt")
config.bind("<Ctrl-B>", "rl-backward-char", mode="prompt")
config.bind("<Ctrl-E>", "rl-end-of-line", mode="prompt")
config.bind("<Ctrl-F>", "rl-forward-char", mode="prompt")
config.bind("<Ctrl-H>", "rl-backward-delete-char", mode="prompt")
config.bind("<Ctrl-K>", "rl-kill-line", mode="prompt")
config.bind("<Ctrl-P>", "prompt-open-download --pdfjs", mode="prompt")
config.bind("<Ctrl-U>", "rl-unix-line-discard", mode="prompt")
config.bind("<Ctrl-W>", "rl-unix-word-rubout", mode="prompt")
config.bind("<Ctrl-X>", "prompt-open-download", mode="prompt")
config.bind("<Ctrl-Y>", "rl-yank", mode="prompt")
config.bind("<Down>", "prompt-item-focus next", mode="prompt")
config.bind("<Escape>", "mode-leave", mode="prompt")
config.bind("<Return>", "prompt-accept", mode="prompt")
config.bind("<Shift-Tab>", "prompt-item-focus prev", mode="prompt")
config.bind("<Tab>", "prompt-item-focus next", mode="prompt")
config.bind("<Up>", "prompt-item-focus prev", mode="prompt")

# Bindings for register mode
config.bind("<Escape>", "mode-leave", mode="register")

# Bindings for yesno mode
config.bind("<Alt-Shift-Y>", "prompt-yank --sel", mode="yesno")
config.bind("<Alt-Y>", "prompt-yank", mode="yesno")
config.bind("<Escape>", "mode-leave", mode="yesno")
config.bind("<Return>", "prompt-accept", mode="yesno")
config.bind("N", "prompt-accept --save no", mode="yesno")
config.bind("Y", "prompt-accept --save yes", mode="yesno")
config.bind("n", "prompt-accept no", mode="yesno")
config.bind("y", "prompt-accept yes", mode="yesno")
# org-capture
config.bind("cit", "spawn --userscript org-protocol capture Pit")
config.bind("cl", "spawn --userscript org-protocol store-link")
# mpv
config.bind(",M", 'spawn emacsclient -n -e "(mpv-enqueue-maybe-archive \\"{url}\\")"')
config.bind(
    ",m",
    'hint links spawn emacsclient -n -e "(mpv-enqueue-maybe-archive \\"{hint-url}\\")"',
)
config.bind(
    ",n",
    'hint --rapid links spawn emacsclient -n -e "(mpv-enqueue-maybe-archive \\"{hint-url}\\")"',
)

config.bind(",P", 'spawn emacsclient -n -e "(mpv-build-playlist \\"{url}\\")"')
config.bind(
    ",p", 'hint links spawn emacsclient -n -e "(mpv-build-playlist \\"{hint-url}\\")"'
)
config.bind(
    ",l",
    'hint --rapid links spawn emacsclient -n -e "(mpv-build-playlist \\"{hint-url}\\")"',
)

config.bind(
    ",y", 'hint links spawn emacsclient -n -e "(ytdl-downloader \\"{hint-url}\\")"'
)
config.bind(",Y", 'spawn emacsclient -n -e "(ytdl-downloader \\"{url}\\")"')
## Backend to use to display websites. qutebrowser supports two different
## web rendering engines / backends, QtWebKit and QtWebEngine. QtWebKit
## was discontinued by the Qt project with Qt 5.6, but picked up as a
## well maintained fork: https://github.com/annulen/webkit/wiki -
## qutebrowser only supports the fork. QtWebEngine is Qt's official
## successor to QtWebKit. It's slightly more resource hungry than
## QtWebKit and has a couple of missing features in qutebrowser, but is
## generally the preferred choice.
## Type: String
## Valid values:
##   - webengine: Use QtWebEngine (based on Chromium).
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari).
# c.backend = 'webengine'

## This setting can be used to map keys to other keys. When the key used
## as dictionary-key is pressed, the binding for the key used as
## dictionary-value is invoked instead. This is useful for global
## remappings of keys, for example to map Ctrl-[ to Escape. Note that
## when a key is bound (via `bindings.default` or `bindings.commands`),
## the mapping is ignored.
## Type: Dict
# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}

# config.bind('+', 'zoom-in')
# config.bind('-', 'zoom-out')
# config.bind('.', 'repeat-command')
# config.bind('/', 'cmd-set-text /')
# config.bind(':', 'cmd-set-text :')
# config.bind(';I', 'hint images tab')
# config.bind(';O', 'hint links fill :open -t -r {hint-url}')
# config.bind(';R', 'hint --rapid links window')
# config.bind(';Y', 'hint links yank-primary')
# config.bind(';b', 'hint all tab-bg')
# config.bind(';d', 'hint links download')
# config.bind(';f', 'hint all tab-fg')
# config.bind(';h', 'hint all hover')
# config.bind(';i', 'hint images')
# config.bind(';o', 'hint links fill :open {hint-url}')
# config.bind(';r', 'hint --rapid links tab-bg')
# config.bind(';t', 'hint inputs')
# config.bind(';y', 'hint links yank')
# config.bind('<Alt-1>', 'tab-focus 1')
# config.bind('<Alt-2>', 'tab-focus 2')
# config.bind('<Alt-3>', 'tab-focus 3')
# config.bind('<Alt-4>', 'tab-focus 4')
# config.bind('<Alt-5>', 'tab-focus 5')
# config.bind('<Alt-6>', 'tab-focus 6')
# config.bind('<Alt-7>', 'tab-focus 7')
# config.bind('<Alt-8>', 'tab-focus 8')
# config.bind('<Alt-9>', 'tab-focus -1')
# config.bind('<Alt-m>', 'tab-mute')
# config.bind('<Ctrl-A>', 'navigate increment')
# config.bind('<Ctrl-Alt-p>', 'print')
# config.bind('<Ctrl-B>', 'scroll-page 0 -1')
# config.bind('<Ctrl-D>', 'scroll-page 0 0.5')
# config.bind('<Ctrl-F5>', 'reload -f')
# config.bind('<Ctrl-F>', 'scroll-page 0 1')
# config.bind('<Ctrl-N>', 'open -w')
# config.bind('<Ctrl-PgDown>', 'tab-next')
# config.bind('<Ctrl-PgUp>', 'tab-prev')
# config.bind('<Ctrl-Q>', 'quit')
# config.bind('<Ctrl-Return>', 'follow-selected -t')
# config.bind('<Ctrl-Shift-N>', 'open -p')
# config.bind('<Ctrl-Shift-T>', 'undo')
# config.bind('<Ctrl-Shift-Tab>', 'nop')
# config.bind('<Ctrl-Shift-W>', 'close')
# config.bind('<Ctrl-T>', 'open -t')
# config.bind('<Ctrl-Tab>', 'tab-focus last')
# config.bind('<Ctrl-U>', 'scroll-page 0 -0.5')
# config.bind('<Ctrl-V>', 'enter-mode passthrough')
# config.bind('<Ctrl-W>', 'tab-close')
# config.bind('<Ctrl-X>', 'navigate decrement')
# config.bind('<Ctrl-^>', 'tab-focus last')
# config.bind('<Ctrl-h>', 'home')
# config.bind('<Ctrl-p>', 'tab-pin')
# config.bind('<Ctrl-s>', 'stop')
# config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
# config.bind('<F11>', 'fullscreen')
# config.bind('<F5>', 'reload')
# config.bind('<Return>', 'follow-selected')
# config.bind('<back>', 'back')
# config.bind('<forward>', 'forward')
# config.bind('=', 'zoom')
# config.bind('?', 'cmd-set-text ?')
# config.bind('@', 'run-macro')
# config.bind('B', 'cmd-set-text -s :quickmark-load -t')
# config.bind('D', 'tab-close -o')
# config.bind('F', 'hint all tab')
# config.bind('G', 'scroll-to-perc')
# config.bind('H', 'back')
# config.bind('J', 'tab-next')
# config.bind('K', 'tab-prev')
# config.bind('L', 'forward')
# config.bind('M', 'bookmark-add')
# config.bind('N', 'search-prev')
# config.bind('O', 'cmd-set-text -s :open -t')
# config.bind('PP', 'open -t -- {primary}')
# config.bind('Pp', 'open -t -- {clipboard}')
# config.bind('R', 'reload -f')
# config.bind('Sb', 'open qute://bookmarks#bookmarks')
# config.bind('Sh', 'open qute://history')
# config.bind('Sq', 'open qute://bookmarks')
# config.bind('Ss', 'open qute://settings')
# config.bind('T', 'tab-focus')
# config.bind('ZQ', 'quit')
# config.bind('ZZ', 'quit --save')
# config.bind('[[', 'navigate prev')
# config.bind(']]', 'navigate next')
# config.bind('`', 'enter-mode set_mark')
# config.bind('ad', 'download-cancel')
# config.bind('b', 'cmd-set-text -s :quickmark-load')
# config.bind('cd', 'download-clear')
# config.bind('co', 'tab-only')
# config.bind('d', 'tab-close')
# config.bind('f', 'hint')
# config.bind('g$', 'tab-focus -1')
# config.bind('g0', 'tab-focus 1')
# config.bind('gB', 'cmd-set-text -s :bookmark-load -t')
# config.bind('gC', 'tab-clone')
# config.bind('gD', 'tab-give')
# config.bind('gO', 'cmd-set-text :open -t -r {url:pretty}')
# config.bind('gU', 'navigate up -t')
# config.bind('g^', 'tab-focus 1')
# config.bind('ga', 'open -t')
# config.bind('gb', 'cmd-set-text -s :bookmark-load')
# config.bind('gd', 'download')
# config.bind('gf', 'view-source')
# config.bind('gg', 'scroll-to-perc 0')
# config.bind('gi', 'hint inputs --first')
# config.bind('gl', 'tab-move -')
# config.bind('gm', 'tab-move')
# config.bind('go', 'cmd-set-text :open {url:pretty}')
# config.bind('gr', 'tab-move +')
# config.bind('gt', 'cmd-set-text -s :buffer')
# config.bind('gu', 'navigate up')
# config.bind('h', 'scroll left')
# config.bind('i', 'enter-mode insert')
# config.bind('j', 'scroll down')
# config.bind('k', 'scroll up')
# config.bind('l', 'scroll right')
# config.bind('m', 'quickmark-save')
# config.bind('n', 'search-next')
# config.bind('o', 'cmd-set-text -s :open')
# config.bind('pP', 'open -- {primary}')
# config.bind('pp', 'open -- {clipboard}')
# config.bind('q', 'record-macro')
# config.bind('r', 'reload')
# config.bind('sf', 'save')
# config.bind('sk', 'cmd-set-text -s :bind')
# config.bind('sl', 'cmd-set-text -s :set -t')
# config.bind('ss', 'cmd-set-text -s :set')
# config.bind('tIH', 'config-cycle -p -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tIh', 'config-cycle -p -u *://{url:host}/* content.images ;; reload')
# config.bind('tIu', 'config-cycle -p -u {url} content.images ;; reload')
# config.bind('tPH', 'config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tPh', 'config-cycle -p -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tPu', 'config-cycle -p -u {url} content.plugins ;; reload')
# config.bind('tSH', 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSh', 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSu', 'config-cycle -p -u {url} content.javascript.enabled ;; reload')
# config.bind('th', 'back -t')
# config.bind('tiH', 'config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tih', 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload')
# config.bind('tiu', 'config-cycle -p -t -u {url} content.images ;; reload')
# config.bind('tl', 'forward -t')
# config.bind('tpH', 'config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tph', 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tpu', 'config-cycle -p -t -u {url} content.plugins ;; reload')
# config.bind('tsH', 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsh', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsu', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')
# config.bind('u', 'undo')
# config.bind('v', 'enter-mode caret')
# config.bind('wB', 'cmd-set-text -s :bookmark-load -w')
# config.bind('wO', 'cmd-set-text :open -w {url:pretty}')
# config.bind('wP', 'open -w -- {primary}')
# config.bind('wb', 'cmd-set-text -s :quickmark-load -w')
# config.bind('wf', 'hint all window')
# config.bind('wh', 'back -w')
# config.bind('wi', 'inspector')
# config.bind('wl', 'forward -w')
# config.bind('wo', 'cmd-set-text -s :open -w')
# config.bind('wp', 'open -w -- {clipboard}')
# config.bind('xO', 'cmd-set-text :open -b -r {url:pretty}')
# config.bind('xo', 'cmd-set-text -s :open -b')
# config.bind('yD', 'yank domain -s')
# config.bind('yM', 'yank markdown -s')
# config.bind('yP', 'yank pretty-url -s')
# config.bind('yT', 'yank title -s')
# config.bind('yY', 'yank -s')
# config.bind('yd', 'yank domain')
# config.bind('ym', 'yank markdown')
# config.bind('yp', 'yank pretty-url')
# config.bind('yt', 'yank title')
# config.bind('yy', 'yank')
# config.bind('{{', 'navigate prev -t')
# config.bind('}}', 'navigate next -t')

## Bindings for caret mode
# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'drop-selection', mode='caret')
# config.bind('<Escape>', 'leave-mode', mode='caret')
# config.bind('<Return>', 'yank selection', mode='caret')
# config.bind('<Space>', 'toggle-selection', mode='caret')
# config.bind('G', 'move-to-end-of-document', mode='caret')
# config.bind('H', 'scroll left', mode='caret')
# config.bind('J', 'scroll down', mode='caret')
# config.bind('K', 'scroll up', mode='caret')
# config.bind('L', 'scroll right', mode='caret')
# config.bind('Y', 'yank selection -s', mode='caret')
# config.bind('[', 'move-to-start-of-prev-block', mode='caret')
# config.bind(']', 'move-to-start-of-next-block', mode='caret')
# config.bind('b', 'move-to-prev-word', mode='caret')
# config.bind('c', 'enter-mode normal', mode='caret')
# config.bind('e', 'move-to-end-of-word', mode='caret')
# config.bind('gg', 'move-to-start-of-document', mode='caret')
# config.bind('h', 'move-to-prev-char', mode='caret')
# config.bind('j', 'move-to-next-line', mode='caret')
# config.bind('k', 'move-to-prev-line', mode='caret')
# config.bind('l', 'move-to-next-char', mode='caret')
# config.bind('v', 'toggle-selection', mode='caret')
# config.bind('w', 'move-to-next-word', mode='caret')
# config.bind('y', 'yank selection', mode='caret')
# config.bind('{', 'move-to-end-of-prev-block', mode='caret')
# config.bind('}', 'move-to-end-of-next-block', mode='caret')

## Bindings for command mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='command')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt-D>', 'rl-kill-word', mode='command')
# config.bind('<Alt-F>', 'rl-forward-word', mode='command')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl-C>', 'completion-item-yank', mode='command')
# config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
# config.bind('<Ctrl-N>', 'command-history-next', mode='command')
# config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-Return>', 'command-accept --rapid', mode='command')
# config.bind('<Ctrl-Shift-C>', 'completion-item-yank --sel', mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
# config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='command')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
# config.bind('<Down>', 'completion-item-focus --history next', mode='command')
# config.bind('<Escape>', 'leave-mode', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'completion-item-focus --history prev', mode='command')

## Bindings for hint mode
# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
# config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
# config.bind('<Escape>', 'leave-mode', mode='hint')
# config.bind('<Return>', 'follow-hint', mode='hint')


## Bindings for passthrough mode
# config.bind('<Shift-Escape>', 'leave-mode', mode='passthrough')

## Bindings for prompt mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
# config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
# config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='prompt')
# config.bind('<Alt-Y>', 'prompt-yank', mode='prompt')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
# config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
# config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Escape>', 'leave-mode', mode='prompt')
# config.bind('<Return>', 'prompt-accept', mode='prompt')
# config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')

## Bindings for register mode
# config.bind('<Escape>', 'leave-mode', mode='register')

## Bindings for yesno mode
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
# config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
# config.bind('<Escape>', 'leave-mode', mode='yesno')
# config.bind('<Return>', 'prompt-accept', mode='yesno')
# config.bind('n', 'prompt-accept no', mode='yesno')
# config.bind('y', 'prompt-accept yes', mode='yesno')
