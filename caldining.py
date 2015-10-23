from lxml import html
import requests

CALDINING_URL='http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?strCurLocation=0'

def get_menu_items(dining_hall_id):
    return []