#!/bin/bash

[[ -f "/tmp/timer.stmp" ]] &&
  start="$(cat "/tmp/timer.stmp")" ||
  start="$(date +%s)"

echo $start > "/tmp/timer.stmp"
while [ 1 ]
do
  clear
  figlet -f bigmono12 $(($(date +%s) - start))
  sleep 1
done
