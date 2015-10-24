# flask-webapp
Use Flask To Build a WebApp

## Installation

Run the following two commands.

`python3 -m pip install lxml`
`python3 -m pip install flask`

If you are on windows - you might need to run the `lxml` installer[from this link](https://pypi.python.org/packages/3.2/l/lxml/lxml-3.4.4.win32-py3.2.exe#md5=bb06fe8dbb28f914deb8b70b7ad68fe4)

If that doesn't work for you - Google your error message.

Windows:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml


## Get CalDining Menu Data

We'll have to figure out how to get the menu information from the dining hall website.

Let's navigate to an example menu page for Foothill [here](http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?strCurLocation=06)

Let's get python to read it.

Open `caldining.py` and let's figure out how to use `lxml` to get the data.


## Running the webserver

Run this command in your terminal

`python3 server.py`

You should see something like

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat...
```

Then open your webbrowser and navigate to
[http://localhost:5000](http://localhost:5000)


## Play around with flask

- Let's create a new route
- Let's create a route with a parameter


## Hookup Flask with our scraper


## Make it look better. 

Instead of return 'hello' 

Let's try `return render_template('home.html')`

## Templates  

```
	<h1> Here's whats avaialble today at {{ name }} </h1>
```



