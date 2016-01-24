from flask import Flask, render_template, g
from caldining import get_menu_items as food
import sqlite3 as s

app = Flask(__name__)
#c.execute('''CREATE TABLE meals (name text, hall text)''') Dont need
#doesn't change unless Berk builds another dining hall LOL
PLACES = ['clarkkerr', 'foothill', 'cafe3', 'crossroads']

@app.route('/<hall>')
def fetch_menu(hall):
	name = hall
	num = hall_to_num(hall)
	if num == 0:
		return "I don't know that place to eat."
	items = food(num)
	for item in items:
		if (item, hall) not in db_read_food():
			db_add_food(item, hall)
	places = PLACES[:]
	places.remove(hall)
	#print(places)
	return render_template('menu.html', items=items, name=name, places=places)

@app.route('/about')
def about():
	return render_template('about.html', places=PLACES)

@app.route('/foods')
def foods():
	return render_template('foods.html', places=PLACES, entries=db_read_food())

@app.route('/ratings')
def ratings():
	return render_template('ratings.html')
@app.route('/api/ratings')
def receive_ratings():
	print(request.form)
	db_add_food(request.form['entry'], request.form['hall'], request.form['rating'])

@app.route('/')
def home():
	return render_template('home.html', places=PLACES)

@app.teardown_appcontext
def close_connection():
	conn = s.connect('meals.db')
	c = conn.cursor()
	conn.close()

def db_read_food():
	conn = s.connect('meals.db')
	c = conn.cursor()
	c.execute("SELECT * FROM meals")
	return c.fetchall()

def db_add_food(food, hall, rating=0):
	conn = s.connect('meals.db')
	c = conn.cursor()
	assert isinstance(food, str), "food must be a string."
	info = (food, hall, rating)
	foods = c.execute("SELECT * FROM meals")
	if info not in foods:
		c.execute("INSERT INTO meals VALUES (?, ?, ?)", info)
	#c.execute("DELETE FROM meals WHERE name NOT IN SELECT name FROM meals")
	conn.commit()



def hall_to_num(hall):
	num = 0
	if hall.lower() == "foothill":
		num = 6
	elif hall.lower() == "clarkkerr":
		num = 4
	elif hall.lower() == "cafe3":
		num = 3
	elif hall.lower() == "crossroads":
		num = 1
	return num

if __name__ == '__main__':
	app.run(debug=True)
