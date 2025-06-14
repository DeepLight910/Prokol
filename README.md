# Hello
This is simple rat virus for my friends
Code was written by me (well, not all code, some was a product of vibe codding)
## Functions
For using it you need to be authorized in BotKxrvPersonal.py in AllowedUser variable
To use you need to send some commands to my bot in Telegram (@KxrvPersonal_bot)
### Commands 
/scr (top:n left:n width:n height:n)optional - sends screenshot of bot's screen (where n are cords in pixels)

/move X Y abs:t/f(optional) dur:n(optional) - moves/shifts cursor to X Y, X Y are cords in pixels of screen, remember that 0 0 is top left corner of screen and 1920 1080 is bottom right, abs if f the cursor will be moved to X Y pixels of top left corner, if t cursor will be shifted from its position to X Y, dur is speed in seconds, e.g. /move 100 100 dur:5 the cursor will be on 100 100 cords in 5 seconds

/click B d(optional) - clicks on mouse button, where B is one of l (LMB), r (RMB), m (MMB) and d if given is double click

/kb b:p+etc - presses given keyboard key where :p if given key will be pressed but not released until first key without :p or in end of the keys, e.g. /kb alt:p+f4 - the alt key will be hold and then the F4 key will be pressed and released both of keys

/disable - disables user input from mouse and keyboard (no effect on /move /cl and /kb commands)

/enable - due to some reason need to be sent 3 times, enables user input from mouse and keyboard

/text t - open notebook with given text, where t is given text

/wp set/restore - if set change wallpapers to screams/2.png, if restore changes wallpapers back

/kill - close all apps exclude discord, python, cmd, explorer and zapret

/hide - simply win+d hotkey, may not work, I don't know why

/web url - open given url in browser

/play url - plays sound from given url

/kys - kill script itself and removes its task from windows task scheduler if there was

/bsod - simple invoke bsod, may need to be accepted from user

/hico - hide all desktops icons

/sico - show all desktops icons

/check - checks if there task in windows tasks scheduler or not

# P.S.
If script was executed from .exe file then it creates task in windows task scheduler to open this .exe file again on boot