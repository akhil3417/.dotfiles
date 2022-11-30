#!/usr/bin/env sh
# requires: peerflix
# EXTERN_LINK / $W3M_CURRENT_LINK = under cursor
# EXTERN / $W3M_URL               = current page
echo "W3m-control: BACK"
echo "W3m-control: EXTERN_LINK ts peerflix --mpv -a"
