import sys
sys.path.append('../')
#python3 ./-/read.py

from gamesale.func import *

with db:
	for i in db.execute("SELECT * FROM users"): print(i)
	for i in db.execute("SELECT * FROM discounts"): print(i)