from func import *

with db:
	db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, verified int, name text, surname text, sex int, birthday text, photo text, address text, language text, phone int, timezone int, home text, vkid int, vknick text, platform text, days int, genre text)")
	db.execute("CREATE TABLE discounts (id int, name text, original real, steam real, description text)")