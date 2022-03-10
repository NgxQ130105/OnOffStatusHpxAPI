import requests
import json
from pprint import pprint

#reuqest info
def get_info(call):
    r = requests.get(call)
    return r.json()

#Get API_KEY
API_FILE = open("API.json", "r")
API_KEY = json.loads(API_FILE.read())["API-KEY"]

UUID = ""
player_url = "https://api.hypixel.net/skyblock"
