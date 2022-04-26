# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

## Encoding to use for the editor.
## Type: Encoding
c.editor.encoding = 'utf-8'

## Editor (and arguments) to use for the `open-editor` command. The
## following placeholders are defined: * `{file}`: Filename of the file
## to be edited. * `{line}`: Line in which the caret is found in the
## text. * `{column}`: Column in which the caret is found in the text. *
## `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
## Same as `{column}`, but starting from index 0.
## Type: ShellCommand
# Edit fields in Emacs with Ctrl+E
#
# c.editor.command = ['st', '-T', 'dropdown_edit', '-e', '/usr/bin/nvim', '{file}']
# c.editor.command = ["emacsclient", "+{line}:{column}", "{file}"]
# c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.editor.command = ['emacsclient', '-c', '-F', r'((name . "dropdown_edit"))', '--eval', '(progn (find-file "{file}") (markdown-mode) (local-set-key (kbd "C-c C-c") (lambda () (interactive) (save-buffer) (unwind-protect (kill-buffer-and-window) (delete-frame)))))']

# c.editor.command = ['emacsclient', '-c', '-F', r'((name . "dropdown_edit"))', '--eval', '(progn (find-file "{file}") (markdown-mode) (local-set-key (kbd "C-c C-c") (lambda () (interactive) (save-buffer) (unwind-protect (kill-buffer-and-window) (delete-frame)))))']
#
