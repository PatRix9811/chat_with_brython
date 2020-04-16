from browser import document, alert, websocket, window
from browser.session_storage import storage
from browser.html import DIV
import datetime

if 'chat-nickname' not in storage.keys():
	window.location.href = 'http://localhost/python_chat/'

send_button = document['send-button']
txtarea = document['txtarea']
ws = websocket.WebSocket("ws://192.168.1.24:443")
nickname = storage['chat-nickname']


def append_to_chat_area(data, is_mine=False):
	chat_area = document['chat-area']
	time_as_str = str(datetime.datetime.now().time())
	separator = " | "
	if not is_mine:
		main_msg_css_class = 'text-left alert alert-primary'
		message = time_as_str+separator+data
	else:
		main_msg_css_class = 'text-right alert alert-dark'
		message = data+separator+time_as_str
	chat_area <= DIV(message, Class=main_msg_css_class)
	send_button.scrollIntoView()


def on_click_on_send_button(ev):
	ev.preventDefault()
	message = txtarea.value
	txtarea.value = ''
	if not message:
		return
	ws.send((nickname,message))
	append_to_chat_area(message,is_mine=True)


send_button.bind('click',on_click_on_send_button)


def on_connection_open(evt):
	del send_button.attrs['disabled']


def on_message(evt):
	msg = evt.data
	append_to_chat_area(msg)


def on_close(evt):
	alert("Connection is closed")


ws.bind('open', on_connection_open)
ws.bind('message', on_message)
ws.bind('close', on_close)