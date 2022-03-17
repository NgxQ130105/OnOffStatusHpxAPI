#Import libs
from asyncio import events
import asyncio
import aiohttp #Replacing request module with aiohttp
from mojang import MojangAPI #Mojang api to get Json API Data 
import hikari #Hikari module for Python Discord bot
import lightbulb #Lightbulb extension for more Hikari Utils


bot = lightbulb.BotApp(
    token="OTUyNDYzOTM1NjIwMTI0NzEy.Yi2ZKg.2_ewOLMXxS_QqWw3GwGrMnSsai0",
    default_enabled_guilds=(952060009863344148)
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started running!')

#Create Pinging request to Discord bot using Slash Command (Decorator)
@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    
    if event.content.startswith("hk.ping"):
        await event.message.respond('Hello, you will be notified when you are logged out')
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

        #Website API (Json Parametters)
        async with aiohttp.ClientSession() as session:
            async with session.get(statusURL) as response:
                data = await response.json() #request Data API from api.hypixel.net
                onHypixel = data["session"]["online"] #get online from session from json Dict
                
        if onHypixel == True:
            onSkyblock = data["session"]["gameType"] #get gameType from session from json Dict
            onWhichIs = data["session"]["mode"] #get mode from session from json Dict
            if onSkyblock != "SKYBLOCK" and onWhichIs != "dynamic":
                await event.message.respond(f'{playerName} is no longer playing Hypixel Skyblock or no longer online')
        if onHypixel == False:
            await event.message.respond(f'{playerName} is no longer playing Hypixel Skyblock or no longer online')
        asyncio.sleep(60)
        
bot.run()

