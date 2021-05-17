# Anon-Chat
Python script to create a chat app inside the terminal using ncurses, pubnub and custom encryption.

This script uses the Pubnub free API to transfer messages and uses custom encryption technique implemented in encrypt.py
Feel free to use your own encryption methods :)

You can also randomise the data inside encrypt.py using a script which i will upload soon, but make sure all of your members use the same encryption protocol.

## STEPS

1) You’ll need to sign up for PubNub to get your keys if you haven’t already. Once you have, your keys are available in the PubNub Admin Dashboard.

Signup - https://dashboard.pubnub.com/signup
Admin Dashboard - https://dashboard.pubnub.com/login

Also use the command - pip3 install -r requirements.txt to install the dependencies

2) Note down your keys and enter them in line number 18,19 of app.py

3) Enter the names of the permanent members of your team as a dictionary entry in line number 13 of app.py

4) Distribute the package to your team members

5) Set your name as one of the names present in the dictionary in line 15 of app.py and tell your members to do the same.

6) You're all set!! Run python3 app.py and invite all the members for a private chat!


## NOTE

You can also use pyinstaller or pyexe to close source the program. I will upload a script to do that soon :)

Feel free to customise the ui inside ui.py and add colors to it. I will do that soon once i get time :)

I know the above steps are cumbersome, i will include a script to make it automatic and user-friendly, so stay tuned ;) and enjoy! 
