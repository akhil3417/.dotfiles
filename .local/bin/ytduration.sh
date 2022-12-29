#!/usr/bin/env sh
#
# Use =youtube-dl --youtube-skip-dash-manifest -g "URL"= to get the video and audio streams.
# TODO: read url and length from user
start_time="14:30"
duration="7:00"
output_name="Kanha Re Thoda Sa Pyar de"
# The first URL
video_url="https://rr2---sn-ci5gup-a3vl.googlevideo.com/videoplayback?expire=1670665032&ei=6P6TY8TSI9CxwgPf4ICwBg&ip=2401%3A4900%3A1f3c%3A237c%3A672d%3A8152%3Af6ec%3A2b0&id=o-AD1D5XX85s0I7gSTnKKQViz-wxwD9qc345cltTAKjtYx&itag=303&source=youtube&requiressl=yes&mh=zn&mm=31%2C29&mn=sn-ci5gup-a3vl%2Csn-ci5gup-qxak&ms=au%2Crdu&mv=m&mvi=2&pcm2cms=yes&pl=56&initcwndbps=1000000&spc=SFxXNuCOrcBH0Yul9zVerxoNf8GVXZI&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=504624268&dur=1644.800&lmt=1614080312585018&mt=1670643190&fvip=8&keepalive=yes&fexp=24001373%2C24007246&c=ANDROID&txp=6416222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALfYqkW4XmjoCIbvhtLzyjOiKlCf1Sf4G8Jz5A-OUZarAiEAyVNi5wEgS7N5e6JWm0SxIAL-AkNbgNEkZnidQbeR9bw%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgWyUqBqjlx0-IYCRG7v-PjneD3v4p6CuB2tjURNuLf0QCIQDIKERnS7X-P_yRoGHYRLdd4JPDG-8_Xzq8GRbUg1zBnw%3D%3D"
# The second URL
audio_url="https://rr2---sn-ci5gup-a3vl.googlevideo.com/videoplayback?expire=1670665032&ei=6P6TY8TSI9CxwgPf4ICwBg&ip=2401%3A4900%3A1f3c%3A237c%3A672d%3A8152%3Af6ec%3A2b0&id=o-AD1D5XX85s0I7gSTnKKQViz-wxwD9qc345cltTAKjtYx&itag=251&source=youtube&requiressl=yes&mh=zn&mm=31%2C29&mn=sn-ci5gup-a3vl%2Csn-ci5gup-qxak&ms=au%2Crdu&mv=m&mvi=2&pcm2cms=yes&pl=56&initcwndbps=1000000&spc=SFxXNuCOrcBH0Yul9zVerxoNf8GVXZI&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=22731712&dur=1644.821&lmt=1614080324967166&mt=1670643190&fvip=8&keepalive=yes&fexp=24001373%2C24007246&c=ANDROID&txp=6411222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgOy86svBWllINUYEZvOzkplJlGcd8Z2ClyKDBTKe8KkwCIBfNyxsxLZ3IHBUEY4wTtfLTtztCN317C-N9l8rOm5o3&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgWyUqBqjlx0-IYCRG7v-PjneD3v4p6CuB2tjURNuLf0QCIQDIKERnS7X-P_yRoGHYRLdd4JPDG-8_Xzq8GRbUg1zBnw%3D%3D"
ffmpeg -ss "$start_time" -i "$video_url" -ss "$start_time" -i "$audio_url" -map 0:v -map 1:a -ss 30 -t "$duration" -c:v libx264 -c:a aac "$output_name".mkv
# ffmpeg -ss 14:30 -i "$video_url" -ss 14:30 -i "$audio_url" -map 0:v -map 1:a -ss 30 -t 7:00 -c:v libx264 -c:a aac Kanha.mkv
