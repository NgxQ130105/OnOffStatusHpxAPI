import requests
from mojang import MojangAPI

loginCondition = True
while loginCondition == True:
    api_key = "00297e7c-8c63-4e7c-8ce3-aa8a419e3fd0"

    userinput = "z3r0o2"
    uuid = MojangAPI.get_uuid(userinput)
    requestlink = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"

    hydata = requests.get(requestlink).json()

    player = hydata["player"]["displayname"]

    logoutime = hydata['player']['lastLogout']
    logintime = hydata['player']['lastLogin']

    while loginCondition == True:
        if logoutime < logintime:
            loginCondition = True
        else:
            loginCondition = False
            print(f"{player} is no longer online")
