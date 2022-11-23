#!/bin/sh

# sauron - w3m

# current link under cursor in w3m
url="${W3M_CURRENT_LINK}"   

# if the current link contains a url pipe it into grep,
# remove the google redirect and decode the url
# if the current link is empty set the url to the page url
if [ ! -z "${url}" ]; then
   result=$(echo "${url}" | \
            grep -oP '(?<=google.com\/url\?q=)[^&]*(?=&)' \
            | python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read()));")
   [ ! -z "${result}" ] && url="${result}" || url="${url}"
else
    url="${W3M_URL}"
fi

# mpd and taskspooler
audio() {
      tsp pinch -i "${url}" 1>/dev/null 
}

copy_link() {
      echo -n "${url}" | xsel -b 1>/dev/null 
}

download() {
     TS_SOCKET=/tmp/download \
      ts \
      yt-dlp -ciw \
      --no-playlist \
      -f 'bv*[height=1080]+ba' --embed-thumbnail --download-archive ~/Music/youtube-dl/download-archive/videos.txt \
      -o "$HOME/Downloads/yt-dl/videos/%(title)s-[%(id)s].%(ext)s" \
      --external-downloader aria2c --external-downloader-args '-c -j 10 -x 3 -s 3 -k 1M' \
      "${url}" 1>/dev/null
}
# youtube-dl and taskspooler
downloadaudio() {
     TS_SOCKET=/tmp/download \
      ts \
      yt-dlp -ciw \
      --no-playlist \
      -f 'ba' -x --audio-format opus --embed-subs --embed-metadata --download-archive ~/Music/youtube-dl/download-archive/audios.txt \
      -o "$HOME/Music/youtube-dl/%(title)s-[%(id)s].%(ext)s" \
      --external-downloader aria2c --external-downloader-args '-c -j 10 -x 3 -s 3 -k 1M' \
      "${url}" 1>/dev/null
}

# mpv fullscreen on second display and taskspooler
fullscreen() {
     TS_SOCKET=/tmp/videos \
      ts mpv --fs --screen=0 "${url}" 1>/dev/null
}

# mpv and taskspooler
video() {
     TS_SOCKET=/tmp/videos \
      ts mpv --no-terminal "${line}" 1>/dev/null
	   notify-send "Now Playing ♫" "${name}"
}

# fzf prompt variables spaces to line up menu options
audio_tsp='audio      - mpd play audio'
copy_tsp='copy       - xsel copy url under the cusor to the clipboard'
download_tsp='download   - youtube-dl download links'
downloadaud_tsp='download   - youtube-dl download links'
fullscreen_tsp='fullscreen - mpv play fullscreen on second display'
video_tsp='video      - mpv play video on current display'

# fzf prompt to specify function to run on links from ytfzf
menu=$(printf "%s\n" \
	      "${audio_tsp}" \
	      "${copy_tsp}" \
	      "${download_tsp}" \
	      "${downloadaud_tsp}" \
	      "${fullscreen_tsp}" \
	      "${video_tsp}" \
	      | fzf-tmux -d 15% --delimiter='\n' --prompt='Pipe links to: ' --info=inline --layout=reverse --no-multi)

# case statement to run function based on fzf prompt output
case "${menu}" in
   audio*) audio;;
   copy*) copy_link;;
   download*) download;;
   downloadaud*) downloadaud;;
   fullscreen*) fullscreen;;
   video*) video;;
   *) exit;;
esac
