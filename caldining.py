from lxml import html
import requests

CALDINING_URL='http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?strCurLocation=0'

def get_menu_items(dining_hall_id):
	url = CALDINING_URL + str(dining_hall_id)
	page = requests.get(url)
	html_tree = html.fromstring(page.text)
	items = html_tree.xpath('//font/text()')[3:]
	return items