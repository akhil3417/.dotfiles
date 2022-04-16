#!/bin/env sh
sed -E -e 's/^# (.*)/\.NH\n\1\n\.LP\n/g' -e 's/^## (.*)/\.NH\n\1\n\.LP\n/g' -e 's/\*(.*)\*/\\f[I]\1\\f[]/g' $1 | groff -ms -Tpdf -ek | zathura -
#heading 1 ----------^
#heading 2 -----------------------------------------^
#italics --------------------------------------------------------------------------------^
#bold --------------------------------------------------------------------------------^
