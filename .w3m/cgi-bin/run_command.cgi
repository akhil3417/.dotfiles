#!/bin/sh

# run w3m command from clipboard
printf "%s\r\n" "W3m-control: $(xsel -opsb)";
