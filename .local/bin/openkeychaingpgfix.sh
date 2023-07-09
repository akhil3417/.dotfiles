#!/bin/bash
# this script aims to solve the issue faced with openkeychain file decryption saying
# Error "Encountered an error reading input data" when decrypting files created by gpg2.3 onwards
#
# reson for bug ? : as openkeychain app in no longer maintained , its incompatible with newer gnupg
#
# issuse reported links
#
#https://github.com/android-password-store/Android-Password-Store/issues/1456
#https://github.com/open-keychain/open-keychain/issues/2096
#
#
#after looking for half an hour i found the solution  here https://github.com/android-password-store/Android-Password-Store/issues/173
# added throw-keyids to ~/.gnupg/gpg.conf which forced gpg to not put the recipient key IDs into the
# encrypted gpg files for pass (which made it so that openkeychain couldn't open/decrypt the file
# so this script solves that issue
#

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
