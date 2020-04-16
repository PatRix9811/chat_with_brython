from browser import document, window
from browser.session_storage import storage

if 'chat-nickname' in storage.keys():
     window.location.href = 'http://192.168.1.24/python_chat/chat.html'
else:
     print("Session nie ustawiono")


def in_button_on_click(evt):
     print("On_click")
     nick = document['nick-area'].value
     if len(nick) > 0:
          storage['chat-nickname'] = nick
     else:
          document['nick-area'].value = ''


document["in-button"].bind("click",in_button_on_click)
