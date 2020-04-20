from websocket_server import WebsocketServer
import database

def on_message_recived(client, server, message):
	nick = message[:message.find(',')]
	message = message[message.find(',')+1:]
	temp_message = nick+': '+message
	message = temp_message
	sender_id = client['id']
	clients_to_notify = filter(lambda c: c['id'] != sender_id, server.clients)
	for dst_client in clients_to_notify:
		dst_client['handler'].send_message(message)


server = WebsocketServer(443, host='192.168.1.24')
server.set_fn_message_received(on_message_recived)
server.run_forever()