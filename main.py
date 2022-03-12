#Import libs
import requests
from mojang import MojangAPI
import time
import hikari
import lightbulb


bot = hikari.GatewayBot(token="OTUyMDU4MjM4Nzc2NTEyNjAz.YiwfVA.vCQO21Xb_NNBlhGwY6g3xt8uQCg" , 
    default_enabled_guild = (952060009863344148)
)


@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong')
bot.run()
api_key = "00297e7c-8c63-4e7c-8ce3-aa8a419e3fd0"

userinput = "z3r0o2"
uuid = MojangAPI.get_uuid(userinput)
requestlink = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"

hydata = requests.get(requestlink).json()


#Main runtime
while True:
    hydata = requests.get(requestlink).json()

    player = hydata["player"]["displayname"]

    logoutime = hydata['player']['lastLogout']
    logintime = hydata['player']['lastLogin']
    
    if logoutime > logintime:
        print(f"{player} is no longer online")
        break
    time.sleep(60)
    