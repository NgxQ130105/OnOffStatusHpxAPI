#Import libs
import requests
from mojang import MojangAPI
import time
import hikari
import lightbulb


bot = lightbulb.BotApp(
    token="",
    default_enabled_guilds=(952060009863344148)
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started running!')

@bot.command
@lightbulb.command('afk', 'Checking AFK condition of the player')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Hello, you will be notified when you are logged out')
    api_key = "00297e7c-8c63-4e7c-8ce3-aa8a419e3fd0"
    userinput = "z3r0o2" #or input()

    #Getting the Hpx ID
    uuid = MojangAPI.get_uuid(userinput)
    requestName = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"
    hydata = requests.get(requestName).json()
    playerName = hydata["player"]["displayname"]

    while True:
        Outofthegame = False
        requestStatus = f"https://api.hypixel.net/status?key={api_key}&uuid={uuid}"

        hydata = requests.get(requestStatus).json()
        onHypixel = hydata["session"]["online"]
        # onSkyblock = hydata["session"]["gameType"]

        if onHypixel == True:
            if hydata["session"]["gameType"] != "SKYBLOCK" and hydata["session"]["mode"] != "dynamic":
                print("The player is no longer playing Skyblock")
                Outofthegame = True
                break
        if onHypixel == False:
            print("The player has been disconnected from Hypixel")
            Outofthegame = True
            break
        time.sleep(60)
    
    if Outofthegame == True:
        await ctx.respond(f'{playerName} is no longer playing Hypixel Skyblock or no longer online')
bot.run()


# #FOR TESTING PURPOSE
# onHypixel = hydata["session"]["online"]
# onSkyblock = hydata["session"]["gameType"]

# print(onHypixel)
# print(onSkyblock)
    

# Main function
# api_key = "00297e7c-8c63-4e7c-8ce3-aa8a419e3fd0"
# userinput = "z3r0o2" #or input()


# #Getting the Hpx ID
# uuid = MojangAPI.get_uuid(userinput)
# requestStatus = f"https://api.hypixel.net/status?key={api_key}&uuid={uuid}"


# #Main runtime
# while True:
#     requestStatus = f"https://api.hypixel.net/status?key={api_key}&uuid={uuid}"

#     hydata = requests.get(requestStatus).json()
#     onHypixel = hydata["session"]["online"]
#     # onSkyblock = hydata["session"]["gameType"]

#     if onHypixel == True:
#         if hydata["session"]["gameType"] != "SKYBLOCK" and hydata["session"]["mode"] != "dynamic":
#             print("The player is no longer playing Skyblock")
#             break
#     if onHypixel == False:
#         print("The player has been disconnected from Hypixel")
#         break
#     time.sleep(60)