#!/usr/bin/env sh
# requires: mpv
# EXTERN_LINK / $W3M_CURRENT_LINK = under cursor
# EXTERN / $W3M_URL               = current page
# echo "W3m-control: ts pinch -i EXTERN_LINK 1>/dev/null "
echo "W3m-control: BACK"
echo "W3m-control: EXTERN_LINK ts pinch -i  1>/dev/null"
