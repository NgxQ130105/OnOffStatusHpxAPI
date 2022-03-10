import requests
import json
from pprint import pprint

#Get API_KEY
API_FILE = open("API.json", "r")
API_KEY = json.loads(API_FILE.read())["API-KEY"]

