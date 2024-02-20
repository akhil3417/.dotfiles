#!/usr/bin/env sh
mpc playlist | sort | uniq -d -c | while read song; do count=$(echo "$song" |
sed -e "s/^[ \t]*//" | cut -d" " -f1); song=$(echo "$song" | sed -e "s/^[
\t]*//" | cut -d" " -f2-); for (( i = 2 ; i <= $count; i++ )); do mpc playlist |
grep -n "$song" | tail -n 1 | cut -d: -f1 | mpc del; done; done
