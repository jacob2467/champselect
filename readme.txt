This program will accept a match, declare your character, ban your character, 
and then lock in your character. At the moment, it doesn't work if your character
gets banned, or your teammate wants to play the character you want to ban, or if
someone declines the ready check. You also have to have league set to the
resolution it's at by default, and it has to be on your primary monitor if you
have more than one. You also can't move it around much. I might fix some of
these issues at some point, but this project was mostly for fun and I doubt
anyone will actually use it so I'm not sure. Finally, if you downloaded the source code and not the release, the script won't work without libtesseract-5.dll, which was too large of a file to upload to GitHub. I've included a compressed version in /Tesseract-OCR, which is also where the extracted .dll file should go.

The values in the config.ini file should work for 1080p. Below are the values
for a few other resolutions that I've tested, including 1080p in case you want
to change it back:

-----------------------------------------------------------------------
1920 x 1080:

[SearchBar]
searchx = 1150
searchy = 265

[ChooseCharacter]
characterx = 700
charactery = 325

[LockInCharacter]
lockinx = 950
lockiny = 770

[AcceptMatch]
acceptx = 925
accepty = 700


# These values change the dimensions of the screenshot.
# X coordinate of top left
# Y of top left
# X of bottom right
# Y of bottom right

[WindowSize]
windowsize1 = 320
windowsize2 = 180 
windowsize3 = 1600
windowsize4 = 825

-----------------------------------------------------------------------
2560 x 1440:

[SearchBar]
searchx = 1150
searchy = 265

[ChooseCharacter]
characterx = 700
charactery = 325

[LockInCharacter]
lockinx = 950
lockiny = 770

[AcceptMatch]
acceptx = 925
accepty = 700


# These values change the dimensions of the screenshot.
# X coordinate of top left
# Y of top left
# X of bottom right
# Y of bottom right

[WindowSize]
windowsize1 = 320
windowsize2 = 180 
windowsize3 = 1600
windowsize4 = 825

-----------------------------------------------------------------------
2880 x 1800

[SearchBar]
searchx = 900
searchy = 200

[ChooseCharacter]
characterx = 475
charactery = 250

[LockInCharacter]
lockinx = 720
lockiny = 700

[AcceptMatch]
acceptx = 700
accepty = 650


# These values change the dimensions of the screenshot.
# X coordinate of top left
# Y of top left
# X of bottom right
# Y of bottom right

[WindowSize]
windowsize1 = 160
windowsize2 = 200
windowsize3 = 2724
windowsize4 = 1600
-----------------------------------------------------------------------