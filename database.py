from os import path

import sqlite3 as sql
import datetime

db_new = True
db_isOpen = False
db_connection = None
db_cursor = None

def db_check_exist():
	if path.exists("chat.db"):
		db_new = False

	try:
		db_connection = sql.connect("chat.db")
		db_cursor = db_connection.cursor()
		db_isOpen = True
	except:
		print("Cannot open the database...")
		return False

	if db_isOpen and db_new:
		db_cursor.execute('CREATE TABELE chat (post_date date,post_nick text,post_content text)')
	else:
		return True


def db_add_mesage(message, nick):
	message_date = datetime.datetime.now().date()
	db_cursor.execute(f"INSERT INTO chat ({message_date},{nick},{message})")


def db_read_last_20_messages():
	pass
