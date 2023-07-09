#!/bin/bash
set -euo pipefail
export IFS=$'\n\t'

export KEYID= # Put your key id here

GPG=$(which gpg) # the path for the gpg program
PASSWORD_STORE_DIR=${PASSWORD_STORE_DIR:=$HOME/.password-store}
TEMP_DIR=$(mktemp --directory)

for path in $(find ${PASSWORD_STORE_DIR} -iname '*.gpg'); do
    echo "Processing ${path}"
    temp_file="${TEMP_DIR}/${path##*/}"

    ${GPG} -q --decrypt "${path}" | ${GPG} --no-throw-keyids --encrypt -r $KEYID --output "${temp_file}"

    mv -f "${temp_file}" "${path}"
done

echo
echo "Creating git commit with all the changes"
read -n 1 -s -r -p "Press any key to continue, ctrl+c to stop"
echo
git commit -a -m "Adding key ids (i.e. gpg --no-throw-keyids)"

echo
echo "Pushing the commit"
read -n 1 -s -r -p "Press any key to continue, ctrl+c to stop"
echo
git push
