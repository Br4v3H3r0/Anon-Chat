import sys, os
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from encrypt import *
from ui import ChatUI
from curses import wrapper,nocbreak,echo,curs_set,endwin
    

channel = 'chat-channel'
pnconfig = PNConfiguration()
name_dict={"br4v3h3r0":0,"superhero":0} # ADD NAMES OF ALL PERMANENT MEMBERS OF CHAT HERE

name="superhero"        # SET YOUR name AS YOUR USERNAME FROM ABOVE LIST
# name="br4v3h3r0"

pnconfig.publish_key='demo'    # ENTER YOUR KEYS HERE
pnconfig.subscribe_key='demo'

pubnub = PubNub(pnconfig)
new_messages = []
ui = ""

def main(stdscr):
    global ui
    pubnub.add_listener(MySubscribeCallback())
    pubnub.subscribe().channels(channel).execute()
    
    stdscr.clear()
    ui = ChatUI(stdscr)
    ui.chatbuffer_add("ENTER \"exit\" or \"quit\" or \"q\" TO QUIT CHATROOM.")
    _m='Username: '+name
    ui.chatbuffer_add(_m)

    pubnub_publish({"name": encryptor(name), "message": encryptor("has connected.")})

    ui.userlist.append(name)
    ui.redraw_userlist()
    
    while 1:
        message_input = ui.wait_input()
        send_message(message_input)

def display_new_messages():
    while new_messages:
        if len(new_messages) > 0:
            msg = new_messages.pop(0)
            userName=decryptor(msg.get('name'))
            userMessage=decryptor(msg.get('message'))
            msg["name"]=userName
            msg["message"]=userMessage

            if userMessage.lower() == "has connected.":
                name_dict[userName]=1
                if userName != name:
                    ui.userlist.append(userName)
                    ui.redraw_userlist()
                pubnub_publish({"name": encryptor(name), "message": encryptor("is Online.")})
                msg = format_message(msg)
                ui.chatbuffer_add(msg)

            elif userMessage.lower() == "is online.":
                
                if userName!=name:
                    if name_dict[userName]==0:
                        ui.userlist.append(userName)
                        ui.redraw_userlist()
                        name_dict[userName]=1                        
                        msg = format_message(msg)
                        ui.chatbuffer_add(msg)
                        
            elif userMessage.lower() == "has disconnected.":
                ui.userlist.remove(userName)
                ui.redraw_userlist()
                msg = format_message(msg)                
                ui.chatbuffer_add(msg)


            else:
                msg = format_message(msg)                
                ui.chatbuffer_add(msg)

def send_message(message_input):
    if message_input.lower() == "exit" or message_input.lower() == "quit" or message_input.lower() == "q":
        exit_handler()
    else:
        pubnub_publish({"name": encryptor(name), "message": encryptor(message_input)}) #encrypt
        message_input = ""

def pubnub_publish(data):
    pubnub.publish().channel(channel).message(data).sync()

class MySubscribeCallback(SubscribeCallback):
    def message(self, pubnub, pn_message):
        new_messages.append(pn_message.message)
        display_new_messages()

def format_message(message_body):
    return message_body.get('name') + ": " + message_body.get('message')


def exit_handler():
    pubnub_publish({"name": encryptor(name), "message": encryptor("has disconnected.")})
    nocbreak()   # Turn off cbreak mode
    echo()       # Turn echo back on
    curs_set(1)  # Turn cursor back on
    endwin()
    sys.stdout.flush()
    os._exit(0)

wrapper(main)

