
# #FOR TESTING PURPOSE(AIOHTTP + ASYNCIO)
import aiohttp
import asyncio


uuid = "8404f895-d977-4336-8ca8-13687d6badca"
api_key = "00297e7c-8c63-4e7c-8ce3-aa8a419e3fd0"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.hypixel.net/status?key={api_key}&uuid={uuid}") as response:
            data = await response.json()
            onHypixel = data["session"]["online"]
            print(onHypixel)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
 
# #FOR TESTING PURPOSE (Old request Library Example)
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