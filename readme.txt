This program will accept a match, declare your character, ban your character, 
and then lock in your character. At the moment, it doesn't work if your character
gets banned, or your teammate wants to play the character you want to ban, or if
someone declines the ready check. You also have to have league set to the
resolution it's at by default, and it has to be on your primary monitor if you
have more than one. You also can't move it around much. I might fix some of
these issues at some point, but this project was mostly for fun and I doubt
anyone will actually use it so I'm not sure.

The values in the config.ini file should work for 1080p. Below are the values
for a few other resolutions that I've tested, including 1080p in case you want
to change it back:

1920 x 1080:
searchx = 1150
searchy = 265
characterx = 700
charactery = 325
lockinx = 950
lockiny = 770
acceptx = 925
accepty = 700
windowsize1 = 320
windowsize2 = 180 
windowsize3 = 1600
windowsize4 = 825

2560 x 1440:
searchx = 1450
searchy = 375
characterx = 950
charactery = 450
lockinx = 1250
lockiny = 1000
acceptx = 1250
accepty = 900
# Window size is currently set to capture the entire screen because I haven't tested it for 1440p yet.
windowsize1 = 0
windowsize2 = 0
windowsize3 = 2560
windowsize4 = 1440

2880 x 1800:
searchx = 900
searchy = 200
characterx = 475
charactery = 250
lockinx = 720
lockiny = 700
acceptx = 700
accepty = 650
windowsize1 = 160
windowsize2 = 200
windowsize3 = 2724
windowsize4 = 1600

Finally, if you downloaded the source code and not the release, the script
won't work without libtesseract-5.dll, which was too large of a file to upload
to GitHub. I've included a compressed version in /Tesseract-OCR, which is also
where the extracted .dll should go.