#Import libs
import asyncio
import aiohttp #Replacing request module with aiohttp
from mojang import MojangAPI #Mojang api to get Json API Data 
import hikari #Hikari module for Python Discord bot
import lightbulb #Lightbulb extension for more Hikari Utils
from lightbulb.ext import tasks


bot = lightbulb.BotApp(
    token="",
    default_enabled_guilds=(952060009863344148)
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started running!')

#Create Pinging request to Discord bot using Slash Command (Decorator)
@bot.command
@lightbulb.command('afk', 'Checking AFK condition of the player')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Hello, you will be notified when you are logged out')
    api_key = "00297e7c-8c63-4e7c-8ce3-aa8a419e3fd0"
    
    userinput = "z3r0o2" #or input()

    
    #Getting the Hpx ID
    uuid = MojangAPI.get_uuid(userinput)
    
    statusURL = f"https://api.hypixel.net/status?key={api_key}&uuid={uuid}"
    
    playerURL = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"
    
    async with aiohttp.ClientSession() as session1:
        async with session1.get(playerURL) as response1:
            data1 = await response1.json() #request Data API from api.hypixel.net
        
    playerName = data1["player"]["displayname"]
    while True:

        #Website API (Json Parametters)
        async with aiohttp.ClientSession() as session:
            async with session.get(statusURL) as response:
                data = await response.json() #request Data API from api.hypixel.net
                onHypixel = data["session"]["online"] #get online from session from json Dict
                
        if onHypixel == True:
            onSkyblock = data["session"]["gameType"] #get gameType from session from json Dict
            onWhichIs = data["session"]["mode"] #get mode from session from json Dict
            if onSkyblock != "SKYBLOCK" and onWhichIs != "dynamic":
                await ctx.respond(f'{playerName} is no longer playing Hypixel Skyblock or no longer online')
        
        if onHypixel == False:
            await ctx.respond(f'{playerName} is no longer playing Hypixel Skyblock or no longer online')
        
        await asyncio.sleep(0)
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task_one = loop.create_task(ping())
    loop.run_forever()
