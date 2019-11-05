import eel
import os
import psycopg2

eel.init('web');



def connect_to_database():
	global c
	global con
	DATABASE_URL = os.getenv('DATABASE_URL' , 'postgresql://postgres:1234@localhost/flitz')
	con = psycopg2.connect(DATABASE_URL) #, sslmode='require')
	c = con.cursor()
	print('connected to database')


def disconnect():
	c.close()
	con.close()
	print('disconnected')

def create_table():
	c.execute('''CREATE TABLE IF NOT EXISTS "USER"(
		SNO BIGSERIAL PRIMARY KEY NOT NULL,
		NAME VARCHAR NOT NULL,
		MESSAGE TEXT NOT NULL )''')
	con.commit()
	print('Table is created')


connect_to_database()
create_table()

@eel.expose
def get_message(username, message):
	print(username, message)
	c.execute(''' INSERT INTO "USER"(NAME , MESSAGE) VALUES(%s , %s) ''' , (username,message))
	con.commit();
	return 'working'




eel.start('main.html' , size=[1000,600])

disconnect()