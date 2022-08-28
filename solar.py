import os
try: 
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System 
except ModuleNotFoundError:
    os.system(f'cmd /c "pip install pystyle"')

count = 0
printSpaces = " "
if not os.path.exists('logs/'): 
    os.makedirs('logs/')
    Write.Print("Made logs folder\n", Colors.purple_to_blue, interval=0.005)
    print(" ")

if not os.path.exists('commands/'): 
    os.makedirs('commands/')
    Write.Print("Made commands folder\n", Colors.purple_to_blue, interval=0.005)
    print(" ")

if not os.path.exists('theme/'): 
    os.makedirs('theme/')
    Write.Print("Made themes folder\n", Colors.purple_to_blue, interval=0.005)
    print(" ")

def install(package):
    os.system(f'cmd /c "pip install {package}"')

def uninstall(package):
    os.system(f'cmd /c "pip uninstall {package}"')

open("logs/info.log", "w").write(" ")
Write.Print("Resetting info log\n", Colors.purple_to_blue, interval=0.005)
open("logs/warning.log", "w").write(" ")
Write.Print("Resetting warning log\n", Colors.purple_to_blue, interval=0.005)
open("logs/error.log", "w").write(" ")
Write.Print("Resetting error log\n", Colors.purple_to_blue, interval=0.005)
open("logs/critical.log", "w").write(" ")
Write.Print("Resetting critical log\n", Colors.purple_to_blue, interval=0.005)
print(" ")

if not os.path.isfile('config.json'):
    with open('config.json', "w") as f:
        f.write("""
{
    "Main": {
        "Prefix": ">>",
        "Delete Timer": 50,
        "Theme Name": "Solar",
        "Hex Console Color": "#4c00ff"
    },
    "Login": {
        "Token": ""
    },
    "Modes": {
        "RiskyMode": "True",
        "Embeds": "True"
    }
}
        
        """)
        f.close()
    Write.Print("Creating `config.json\n", Colors.purple_to_blue, interval=0.005)
    Write.Print("Created `config.json\n", Colors.purple_to_blue, interval=0.005)

if not os.path.isfile('theme/Solar.json'):
    f = open('theme/Solar.json', "w")
    f.write("""
{
    "title": "Solar",
    "color": "#4c00ff",
    "footer": "Creds to Scope <3",
    "mini_image": "",
    "author_image": "https://i.imgur.com/Eh3Sxxm.png",
    "large_image": "",
    "footer_image": ""
}

    """)
    f.close()
    Write.Print("Creating `Solar.json\n", Colors.purple_to_blue, interval=0.005)
    Write.Print("Created `Solar.json\n", Colors.purple_to_blue, interval=0.005)


try:
    from aiohttp.helpers import TOKEN
except ModuleNotFoundError:
    install("aiohttp")

try:
    import discord
except ModuleNotFoundError:
    install("discord")



try:
    import youtube_dl
except ModuleNotFoundError:
    install("youtube_dl")

try:
    import psutil
except ModuleNotFoundError:
    install("psutil")

try:
    import pyfade
except ModuleNotFoundError:
    install("pyfade")

try:
    import requests
except ModuleNotFoundError:
    install("requests")

try:
    import pause
except ModuleNotFoundError:
    install("pause")

try:
    import logging
except ModuleNotFoundError:
    install("logging")

try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    install("colorama")

try:
    from colored import fg, attr
except ModuleNotFoundError:
    install("colored")

try:
    from sty import fg, bg, ef, rs, Style, RgbFg
except ModuleNotFoundError:
    install("sty")

try:
    import subprocess
except ModuleNotFoundError:
    install("subprocess")

try:
    import random
    import string
    import time
    import sys
    from datetime import datetime, timedelta
    from discord import message
    from discord.ext import commands
    from discord import Member
    import asyncio
    import json
    import ctypes
except Exception as e:
    logging.warning(e) 

__v__ = "7"

with open("config.json") as f:
    config5 = json.load(f)
consoleColor = config5["Main"]["Hex Console Color"]

def hex_to_rgb(hex_string):
        r_hex = hex_string[1:3]
        g_hex = hex_string[3:5]
        b_hex = hex_string[5:7]

        red = int(r_hex, 16)
        green = int(g_hex, 16)
        blue = int(b_hex, 16)

        return red, green, blue

if sys.platform == "win32":
        ccolourred, ccolourgreen, ccolourblue = hex_to_rgb(consoleColor)
        fg.consoleColourr = Style(RgbFg(ccolourred, ccolourgreen, ccolourblue))

        fg.cRed = Style(RgbFg(255, 81, 69))
        fg.cOrange = Style(RgbFg(255, 165, 69))
        fg.cYellow = Style(RgbFg(255, 255, 69))
        fg.cGreen = Style(RgbFg(35, 222, 57))
        fg.cBlue = Style(RgbFg(69, 119, 255))
        fg.cPurple = Style(RgbFg(177, 69, 255))
        fg.cPink = Style(RgbFg(255, 69, 212))

        fg.cGrey = Style(RgbFg(207, 207, 207))
        fg.cBrown = Style(RgbFg(199, 100, 58))
        fg.cBlack = Style(RgbFg(0, 0, 0))
        fg.cWhite = Style(RgbFg(255, 255, 255))

try:
    logging.basicConfig(filename="logs/info.log", level=logging.INFO, format=f'[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
    logging.basicConfig(filename="logs/warning.log", level=logging.WARNING, format=f'[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
    logging.basicConfig(filename="logs/error.log", level=logging.ERROR, format=f'[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
    logging.basicConfig(filename="logs/critical.log", level=logging.CRITICAL, format=f'[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
except FileNotFoundError as e:
    print('Err, contact developer immediatley!')

start = time.time()

def printVal(txt):
    time=datetime.now().strftime("%H:%M")
    print(f"{fg.consoleColourr}[{fg.cWhite}{time} {fg.consoleColourr}| {fg.cWhite}Solar{fg.consoleColourr}] {fg.cWhite}{txt}")




def cls():
    os.system("cls")


try:
    json.load(open("config.json"))

    CONFIG = json.load(open("config.json")) 

    __prefix__ = CONFIG["Main"]["Prefix"]
    __theme_file__ = CONFIG["Main"]["Theme Name"]
    __deletetimeout__ = CONFIG["Main"]["Delete Timer"]

    __token__ = CONFIG["Login"]["Token"]

    __rmode__ = CONFIG["Modes"]["RiskyMode"]

    THEME = json.load(open(f"theme/{__theme_file__}.json"))

    __embedtitle__ = THEME["title"]
    __embedcolour__ = int(THEME["color"].replace('#', '0x'), 0)
    __embedcolourraw__ = THEME["color"]
    __embedfooter__ = THEME["footer"]
    __embedimage__ = THEME["mini_image"]
    __embedauthorimage__ = THEME["author_image"]
    __embedlargeimage__ = THEME["large_image"]
    __footerimage__ = THEME["footer_image"]
    __embedmode__ = CONFIG["Modes"]["Embeds"]

except Exception as e:
    logging.warning(e)

def get_random_user_agent():
    userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
    userAgent = random.choice(userAgents)
    return userAgent    

__headers__={'authorization': __token__, "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"}
Solar = commands.Bot(command_prefix=__prefix__, self_bot=True, case_insensitive=True)
api="https://discord.com/api/v9/"
r = requests.get('https://discord.com/api/v6/users/@me', headers=__headers__)
cls()
if r.status_code == 200:
    pass
else:
    cls()
    Write.Print("Failed to connect to token in config.json! Please enter a valid one and restart.\n", Colors.purple_to_blue, interval=0.005)
    Write.Input("Press enter to exit...\n", Colors.purple_to_blue, interval=0.005)
    os._exit(0)

def centerize(l:list,w:int)->str:
    padding =  ' '*(w//2)
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

def friends():
    request = requests.get("https://discord.com/api/users/@me/relationships", headers={"Authorization": __token__})
    json = request.json()
    friends = []
    for item in json:
        if item["type"] == 1:
            friends.append(item["user"])
    return friends


@Solar.event
async def on_ready():

    text1 = f"""

███████╗ ██████╗ ██╗      █████╗ ██████╗ 
██╔════╝██╔═══██╗██║     ██╔══██╗██╔══██╗
███████╗██║   ██║██║     ███████║██████╔╝
╚════██║██║   ██║██║     ██╔══██║██╔══██╗
███████║╚██████╔╝███████╗██║  ██║██║  ██║
╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

    """
    os_size = os.get_terminal_size().columns
    colored_stuff = f"{fg.consoleColourr}{text1}"
    print(centerize(colored_stuff.splitlines(),int(os_size)))
    printVal(f'{fg.consoleColourr}Connected:{fg.cWhite} {Solar.user.name}#{Solar.user.discriminator}')
    printVal(f'{fg.consoleColourr}Friend(s):{fg.cWhite} {len(friends())}')
    printVal(f'{fg.consoleColourr}RiskMode:{fg.cWhite} {__rmode__}')
    printVal(f'{fg.consoleColourr}Prefix:{fg.cWhite} {Solar.command_prefix}')
    print(Fore.RESET)
    

def pfpUrl(id, pfp):
        url = ""
        if not str(pfp).startswith("http"):
            if str(pfp).startswith("a_"):
                url = f"https://cdn.discordapp.com/avatars/{id}/{pfp}.gif?size=1024"
            else:
                url = f"https://cdn.discordapp.com/avatars/{id}/{pfp}.png?size=1024"

            return url
        else:
            return pfp

Solar.remove_command("help") 



@Solar.event
async def on_command(et):
    try:
        await et.message.delete()
    except:
        pass
    printVal(f"{__prefix__}{et.command.name}")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Solar SelfBot ║ Connected {Solar.user.name}#{Solar.user.discriminator} ║ {__v__} ║ Friend(s) {len(friends())} ║ RiskMode {__rmode__} ║ Prefix: {__prefix__}")



@Solar.event
async def on_command_error(et, error):
    try:
        await et.message.delete()
    except:
        pass
    if isinstance(error, commands.CommandNotFound):
        printVal(f"Unknown command: {error}")
    elif isinstance(error, commands.CheckFailure):
        printVal(f"No embed perms")
    elif isinstance(error, commands.MissingRequiredArgument):
        printVal(f"Missing arguments: {error}")
    else:
        printVal(f"Error: {error}")



        

@Solar.command(name="allcmds", description="Get a list of every single command", usage="allcmds", aliases=["acmds"])
async def allcmds(et):
    x = []
    for cmd in Solar.commands:
        x.append('`'+cmd.name+'`')
        y = ' '.join(x)
    if __embedmode__.lower() == "true":
        embed = discord.Embed(title=f"All Commands [{len(Solar.commands)}]", description=y, color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.set_image(url=__embedlargeimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)          
    else:
        await et.send(y)

@Solar.command(name="search", description="Search for commands.", usage="search [term]")
async def search(et, *, command = None):
    if command is None:
        embed = discord.Embed(title=f"", color=__embedcolour__, description="Please enter a command to search for.")
        embed.set_author(name="Search")
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.set_image(url=__embedlargeimage__)
        embed.timestamp = datetime.now()
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        text = ""
        text2 = ""
        searchedItems = 0
        for cmd in Solar.commands:
            if command in cmd.name or command in cmd.aliases:
                searchedItems += 1
                text += f"**{Solar.command_prefix}{cmd.usage}** » ```{cmd.description}.```\n"
                text2 += f"{Solar.command_prefix}{cmd.usage} » {cmd.description}\n"
        try:
            embed = discord.Embed(title=f"Search results...", description=f"Found `{searchedItems}` matches for `{command}`.\n\n{text}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            embed.set_image(url=__embedlargeimage__)
            embed.timestamp = datetime.now()
            await et.send(embed=embed, delete_after=__deletetimeout__)
        except:
            embed = discord.Embed(title=f"Check console for search results", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            embed.set_image(url=__embedlargeimage__)
            embed.timestamp = datetime.now()
            await et.send(embed=embed, delete_after=__deletetimeout__)
            print(text2)



@Solar.command(name="help", description="Get help", usage="help <category/cmd>", aliases=[])
async def help(et, category=None):
    await et.message.delete()
    if category is None:
        embed = discord.Embed(title=f"Solar Commands [{len(Solar.commands)}]", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.add_field(name=f"`In development...`", value=f"Type {__prefix__}allcmds for a list of the current commands. Help commands will be released in the next version", inline=True)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.set_image(url=__embedlargeimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)     
    elif str(category).lower() == "5345jhaj3240a0pdfsk@-__52a":
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.description = f"**`GENERAL COMMANDS`**\n`{__prefix__}help <category>` - returns all commands of that category\n`{__prefix__}ping` - return the bot's latency\n`{__prefix__}lockpc` - locking the pc\n`{__prefix__}shutdown` - shutdown the selfbot\n`{__prefix__}uptime` - returns the bot runtime\n`{__prefix__}sbinfo` - returns info about the selfbot"
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        for cmd in Solar.commands:
            if category == cmd.name or category in cmd.aliases:
                if not cmd.aliases:
                    cmd.aliases.append("No aliases")
                embed = discord.Embed(title=f"{cmd.name}", color=__embedcolour__)
                embed.add_field(name="Usage", value=f"```{cmd.usage}```", inline=False)
                embed.add_field(name="Description", value=f"```{cmd.description}```", inline=False)
                embed.add_field(name="Aliases", value=', '.join(cmd.aliases))
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
                embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
                embed.timestamp = datetime.now()
                await et.send(embed=embed, delete_after=__deletetimeout__)



@Solar.command(name="newyear", description="Find out when the new year is.", usage="newyear <year>", aliases=["newy"])
async def newyear(et, year: int):
    try:
        def dateDiffInSeconds(date1, date2):
            timedelta = date2 - date1
            return timedelta.days * 24 * 3600 + timedelta.seconds

        def daysHoursMinutesSecondsFromSeconds(seconds):
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            return (days, hours, minutes, seconds)

        req = datetime.strptime(f"{year}-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.add_field(name=("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req))), value=f"```Till year: {year}!```", inline=False)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    except Exception as e:
        logging.error(e)
        embed = discord.Embed(title="Range must be from 2000, to 9999", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="uptime", description="Length of Solar being running (current session)", usage="uptime", aliases=["```upt```"])
async def uptime(et):
    embed = discord.Embed(title="", color=__embedcolour__)
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_thumbnail(url=__embedimage__)
    embed.add_field(name=("Uptime"), value=f"`{str(timedelta(seconds=int(round(time.time() - start))))}`", inline=False)
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="Solarinfo", description="Get current info on your session", usage="Solarinfo", aliases=["```cpi```"])
async def Solarinfo(et):
    embed = discord.Embed(title="", color=__embedcolour__)
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_thumbnail(url=__embedimage__)
    embed.add_field(name=("Solar Commands:"), value=f"`{int(len(Solar.commands))}`", inline=False)
    embed.add_field(name=("Version:"), value=f"`{__v__}`", inline=False)
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="poll", description="Create a simple poll that lasts for a choice of time", usage="poll <seconds> <question>", aliases=[])
async def poll(et, seconds, poll):
    embed = discord.Embed(title="", color=__embedcolour__)
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_thumbnail(url=__embedimage__)
    embed.add_field(name=("Poll"), value=f"{poll}", inline=False)
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    message = await et.send(embed=embed, delete_after=int(seconds))
    await message.add_reaction("✅")
    await message.add_reaction("❎")

# INFO ------------------- INFO ------------------ INFO ------------------ INFO ------------------ INFO ------------------- INFO #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# INFO ------------------- INFO ------------------ INFO ------------------ INFO ------------------ INFO ------------------- INFO #


@Solar.command(name="embed", description="Embed any text", usage="embed <text>", aliases=["```ebd```"], category="text")
async def embed(et, message):
    embed = discord.Embed(color=__embedcolour__, description=f"{message}")
    await et.send(embed=embed, delete_after=__deletetimeout__)


# IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- # 
# IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE #

@Solar.command(name="pfp", description="Get any users pfp", usage="pfp", aliases=[], category="image")
async def pfp(et, *, user: discord.User):
    embed = discord.Embed(title="", color=__embedcolour__)
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.add_field(name=("Profile picture"), value=f"`of {user}`", inline=False)
    embed.set_image(url=pfpUrl(user.id, user.avatar))
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="slap", description="Slap someone or yourself", usage="slap <@user>", aliases=["```sp```"], category="image")
async def slap(et, user: None):
    res = requests.get(f"https://nekos.life/api/v2/img/slap")
    if res.status_code == 200:
        if user:
            embed = discord.Embed(title=f"Slaps {user}", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
        else:
            embed = discord.Embed(title=f"Slaps themselvs!", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="cuddle", description="Hud/Cuddle someone or yourself?", usage="cuddle <@user>", aliases=["```hug```"], category="image")
async def cuddle(et, user: None):
    res = requests.get(f"https://nekos.life/api/v2/img/cuddle")
    if res.status_code == 200:
        if user:
            embed = discord.Embed(title=f"Cuddles {user.mention}", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
        else:
            embed = discord.Embed(title="Hugs themselvs? How!", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="pat", description="Pat someone, or yourself?", usage="pat <@user>", aliases=[], category="image")
async def pat(et, user: None):
    res = requests.get(f"https://nekos.life/api/v2/img/pat")
    if res.status_code == 200:
        if user:
            embed = discord.Embed(title=f"Pats {user.mention}", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
        else:
            embed = discord.Embed(title=f"Pats themselvs?", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)



@Solar.command(name="iphonex", description="Convert a users pfp into an iphoneX", usage="iphonex <@user>", aliases=["ipx"], category="image")
async def iphonex(et, user: discord.User):
    if user:
        res = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={user.avatar_url}")
        if res.status_code == 200:
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["message"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="awooify", description="Awoo any users pfp", usage="awooify <@user>", aliases=["awoi"], category="image")
async def awooify(et, user: discord.User):
    if user:
        res = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={user.avatar_url}")
        if res.status_code == 200:
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["message"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)



@Solar.command(name="cry", description="Make someone cry or yourself", usage="cry <@user>", aliases=[], category="image")
async def cry(et, user: discord.User):
    if user:
        res = requests.get(f"http://api.nekos.fun:8080/api/cry")
        if res.status_code == 200:
            embed = discord.Embed(title=f"{user} cries", color=__embedcolour__)
            embed.set_author(name=f'{user.mention} cries',icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["image"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)       


@Solar.command(name="feed", description="Feed someone or yourself", usage="feed <@user>", aliases=[], category="image")
async def feed(et, user: discord.User):
    if user:
        res = requests.get(f"http://api.nekos.fun:8080/api/feed")
        if res.status_code == 200:
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name='Fed Roman',icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["image"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)       


@Solar.command(name="baguette", description="Make someone eat a baguette", usage="baguette <@user>", aliases=["bagu"], category="bagu")
async def baguette(et, user: discord.User):
    if user:
        res = requests.get(f"https://nekobot.xyz/api/imagegen?type=baguette&url={user.avatar_url}")
        if res.status_code == 200:
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=res.json()["message"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)        


@Solar.command(name="clyde", description="Make clyde say something", usage="clyde <text>", aliases=[])
async def clyde(et, *, text):
    if text:
        res = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}")
        if res.status_code == 200:
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            embed.set_image(url=res.json()["message"])
            await et.send(embed=embed, delete_after=__deletetimeout__)
        else:
            embed = discord.Embed(title="Provide text to make clyde say!", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="birb", description="Get images of birds", usage="birb", aliases=["bird"])
async def birb(et):
    res = requests.get(f"https://api.alexflipnote.dev/birb")
    if res.status_code == 200:
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_image(url=res.json()["file"])
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        printVal('HTTP Request Invalid, try again.')

@Solar.command(name="cats", description="Get images of cats", usage="cats", aliases=["cat"])
async def cats(et):
    res = requests.get(f"https://api.alexflipnote.dev/cats")
    if res.status_code == 200:
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_image(url=res.json()["file"])
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        printVal('HTTP Request Invalid, try again.')

@Solar.command(name="dogs", description="Get images of dogs", usage="dogs", aliases=["dog"])
async def dogs(et):
    res = requests.get(f"https://api.alexflipnote.dev/dogs")
    if res.status_code == 200:
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_image(url=res.json()["file"])
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        printVal('HTTP Request Invalid, try again.')
        
@Solar.command(name="sadcat", description="Get sad images of cats", usage="sadcat", aliases=["scat"])
async def sadcat(et):
    res = requests.get(f"https://api.alexflipnote.dev/sadcat")
    if res.status_code == 200:
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_image(url=res.json()["file"])
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        printVal('HTTP Request Invalid, try again.')

#@Solar.command(name="phcomment", description="Get sad images of cats", usage="phcoment <user> <text>", aliases=["phc"])
#async def phcomment(et, user: discord.User, *, comment):
#    embed = discord.Embed(title="", color=__embedcolour__)
#    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
#    r = requests.get(
#        f"https://nekobot.xyz/api/imagegen?type=phcomment&text={comment}&username={user.name}&image={str(user.avatar_url_as(format='png'))}".replace(" ", "%20"))
#    res = r.json()
 #   embed.set_image(url=res["message"])
#    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
#    await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="trumptweet", description="Make trump tweet something", usage="trumptweet <text>", aliases=["trt"])
async def trumptweet(et, *, text):
    p = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}")
    if __embedmode__.lower() == "true":    
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_image(url=p.json()["message"])
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        await et.send(p.json()["message"])

@Solar.command(name="userbanner", description="Get someones user banner", usage="userbanner <@user>", aliases=["usrbnr"])
async def userbanner(et, user:discord.Member=None):
    if user == None:
        user = et.author
    req = await Solar.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.gif"
        is_a_gif = requests.get(banner_url, timeout=3)
        if is_a_gif.status_code != 200:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.png"
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name=("Profile Banner"), value=f"`of {user}`", inline=False)
        embed.set_image(url=f"{banner_url}?size=1024")
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        req = await Solar.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_hex = req["banner_color"]
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name=("Profile Banner"), value=f"`of {user}`\n`Hex code: {banner_hex}`", inline=False)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="mcachievment", description="Generate a mc achievement", usage="mcachievment", aliases=["mca"])
async def mcachievment(et, *, text):
    embed = discord.Embed(title="", color=__embedcolour__)
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_image(url=f"https://api.iapetus11.me/mc/achievement/{text.replace(' ', '%20')}")
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)   

@Solar.command(name="ytthumbnail", description="Gets a youtube thumbnail", usage="ytthumbnail <ytlink>", aliases=["ytth"])
async def ytthumbnail(et, yt_url):
    if "https://youtu.be/" in yt_url:
        a,b,c,d=yt_url.split("/")
        video_id=d
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name=("Thumbnail "), value=f"`of <{yt_url}>`", inline=False)
        embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    elif "youtube.com/watch?v" in yt_url:
        a,b=yt_url.split("=")
        video_id=b
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name=("Thumbnail "), value=f"`of <{yt_url}>`", inline=False)
        embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.add_field(name="Err", value=f"`Invalid url: <{yt_url}>`")
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="captcha", description="Create a captcha out of someone pfp", usage="captcha <@user> <text>", aliases=["ctc"])
async def captcha(et, user: discord.User, *, text):
    if user:
        p = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={user.avatar_url}&username={text}")
        if __embedmode__.lower() == "true":    
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_image(url=p.json()["message"])
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await et.send(p.json()["message"]) 
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="ucaptcha", description="Create a captcha out of a url", usage="ucaptcha <url> <text>", aliases=["uctc"])
async def ucaptcha(et, captchalink, *, text):
    if captchalink:
        p = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={captchalink}&username={text}")
        if __embedmode__.lower() == "true":   
            try: 
                embed = discord.Embed(title="", color=__embedcolour__)
                embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
                embed.set_image(url=p.json()["message"])
                embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
                await et.send(embed=embed, delete_after=__deletetimeout__)
            except:
                printVal('Failed sending as embed, most likely API err')
                await et.send(p.json()["message"])
        else:
            await et.send(p.json()["message"]) 
    else:
        embed = discord.Embed(title="Mention a user!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

# IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- # 
# IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE ----------------- IMAGE #


# API ------------------- API ------------------- API ------------------- API -------------------- API -------------------- API #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- # 
# API ------------------- API ------------------- API ------------------- API -------------------- API -------------------- API #

@Solar.command(name="kanye", description="kanye quote", usage="kanye", aliases=["```kq```"], category="text")
async def kanye(et):
    res = requests.get(f"https://api.kanye.rest/")
    if res.status_code == 200:
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.add_field(name=("Kanye"), value=(res.json()["quote"])+" ~ Kanye", inline=False)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.set_image(url=__embedlargeimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="roast", description="Roast someone or generate a roast", usage="roast <@user>", aliases=[])
async def roast(et, user: discord.User=None):
    insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json").json()["insult"]
    if user:
        embed = discord.Embed(color=__embedcolour__,description=f"roast for {user.mention}: {str(insult).lower()}")
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(color=__embedcolour__,description=f"{str(insult).lower()}")
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="joke", description="Get a random joke", usage="joke", aliases=[])
async def joke(et, contente):
    contxnt = requests.get(f"https://v2.jokeapi.dev/joke/Any?safe-mode").json()["joke"]
    embed = discord.Embed(color=__embedcolour__,description=str(contente))
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="yomama", description="Generate a yomama joke or to someone", usage="yomama <@user>", aliases=["yom"])
async def yomama(et, user: discord.User=None):
    insult = requests.get("https://api.yomomma.info/").json()["joke"]
    if user:
        embed = discord.Embed(color=__embedcolour__,description=f"yomama {user.mention}: {str(insult).lower()}")
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(color=__embedcolour__,description=f"{str(insult).lower()}")
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="darkhumor", description="Get a random darkhumor joke", usage="darkhumor", aliases=["darkh"])
async def darkhumor(et):
    res = requests.get("https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw")
    pause.seconds(4)
    try:
        setup = res.json()["setup"]
        delivery = res.json()["delivery"]
    except: 
        printVal('HTTP Request Failed, Retry')
    if __embedmode__.lower() == "true":
        embed = discord.Embed(color=__embedcolour__,description=str(setup))
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=3)
        embed2 = discord.Embed(color=__embedcolour__,description=str(delivery))
        embed2.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed2.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        pause.seconds(3)
        await et.send(embed=embed2, delete_after=__deletetimeout__)
    else:
        await et.send(str(setup))
        pause.seconds(3)
        await et.send(str(delivery))

@Solar.command(name="gender", description="Find the most likely gender of any name", usage="gender <name>", aliases=[])
async def gender(et, name):
    res = requests.get(f"https://api.genderize.io/?name={name}")
    pause.seconds(4)
    try:
        gender = res.json()["gender"]
        probability = res.json()["probability"]
    except: 
        printVal('HTTP Request Failed, Retry')
    if __embedmode__.lower() == "true":
        embed = discord.Embed(color=__embedcolour__,description=f"`{name}` Is most likely: `{str(gender)}`, probablity: `{str(probability)}`")
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        await et.send(f"`{name}` Is most likely: `{str(gender)}`, probablity: `{str(probability)}`")



@Solar.command()
async def dadjoke(et):   
    request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
    data = request.json()
    joke = data['joke']
    embed = discord.Embed(color=__embedcolour__,description=str(joke))
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_thumbnail(url=__embedimage__)
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    embed.set_image(url=__embedlargeimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)

# API ------------------- API ------------------- API ------------------- API -------------------- API -------------------- API #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------- # 
# API ------------------- API ------------------- API ------------------- API -------------------- API -------------------- API #


# ANNOYING ------------- ANNOYING -------------- ANNOYING -------------- ANNOYING -------------- ANNOYING ------------- ANNOYING #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# ANNOYING ------------- ANNOYING -------------- ANNOYING -------------- ANNOYING -------------- ANNOYING ------------- ANNOYING #


@Solar.command(name="nitrogen", description="Generate nitro codes to troll people", usage="nitrogen <amount>", aliases=["ngen"])
async def nitrogen(et, num: int):
    with open("nitrocodes.txt", "w") as f:
        for i in range(num): 
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            )) 
            f.write(f"https://discord.gift/{code}\n")
    with open("nitrocodes.txt", "rb") as file:
        await et.send(file=discord.File(file, "nitrocodes.txt"))
    os.remove("nitrocodes.txt")
    printVal("nitrogen: Sent nitrocodes.txt")


@Solar.command(name="typing", description="Start typing to troll people into thinking you're creating a long paragraph", usage="typing <time>", aliases=[])
async def typing(et, time: int):
    printVal(f"typing: Starting typing for {time} seconds")
    async with et.typing():
        await asyncio.sleep(time)
    printVal(f"typing: Finished typing")


@Solar.command(name="purgehack", description="'Purgehack' generates a load of invisible characters to fake purge the chat", usage="purgehack", aliases=["phack"])
async def purgehack(et, amount=1):
    for i in range(amount):
        await et.send("ﾠ"+"\n" * 400 + "ﾠ")
        await asyncio.sleep(1)

@Solar.command(usage="gspam <gcname> <amount> <*users>", description="Create as many gcs as you want")
async def gspam(et, gcname, amount: int, *users: discord.User):
    if __rmode__.lower() == "true":
        await et.message.delete()
        for x in range(amount):
            group_channel = await Solar.user.create_group(*users)
            await group_channel.edit(name=gcname)
            await asyncio.sleep(1.75)
            await group_channel.send(content=gcname)
            await group_channel.leave()
            await asyncio.sleep(1.75)
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

# ANNOYING ------------- ANNOYING -------------- ANNOYING -------------- ANNOYING -------------- ANNOYING ------------- ANNOYING #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# ANNOYING ------------- ANNOYING -------------- ANNOYING -------------- ANNOYING -------------- ANNOYING ------------- ANNOYING #


# RISKY ------------------ RISKY ----------------- RISKY ----------------- RISKY ----------------- RISKY ----------------- RISKY #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# RISKY ------------------ RISKY ----------------- RISKY ----------------- RISKY ----------------- RISKY ----------------- RISKY #


@Solar.command(name="hypesquad", description="Set your hypesquad", usage="hypesquad <hypehouse>", aliases=["hsquad"])
async def hypesquad(et, hype_house: str):
    if __rmode__.lower() == "true":
        houses = {"bravery": 1, "brilliance": 2, "balance": 3}
        hype_house = hype_house.lower()
        if hype_house in houses:
            h={'house_id': houses[hype_house]}
            r=requests.post("https://discord.com/api/v9/hypesquad/online", headers=__headers__, json=h)
            house_value=f"`Changed hypesquad to {hype_house}`"
        elif hype_house == "clear":
            r=requests.delete("https://discord.com/api/v9/hypesquad/online", headers=__headers__)
            house_value=f"`Cleared hypesquad house`"
        else:
            house_value=f"**Invalid option,** please pick one of these: `bravery, brilliance, balance, clear`"
            embed = discord.Embed(title="", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_thumbnail(url=__embedimage__)
            embed.add_field(name="Hypesquad", value=house_value)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="leaveallservers", description="Leave all of your servers", usage="leaveallservers", aliases=["lall"])
async def leaveallservers(et):
    if __rmode__.lower() == "true":
        try:
            leave_all_servers_request = requests.get(
                "https://canary.discord.com/api/v9/users/@me/guilds", headers=__headers__
            ).json()
            for guild in leave_all_servers_request:
                requests.delete(
                    f"https://canary.discord.com/api/v9/users/@me/guilds/{guild['id']}",
                    headers=__headers__,
                )
            printVal("Left all servers")
        except Exception as e:
            logging.error(e)
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)



@Solar.command(name="dmallfriends", description="DM's all friends with your message", usage="nitrogen <amount>", aliases=["dmaf"])
async def dmallfriends(et, message):
    if __rmode__.lower() == "true":
        r=requests.get(
            "https://canary.discord.com/api/v9/users/@me/channels", headers=__headers__
        ).json()
        for channel in r:
            json = {"content": message}
            r = requests.post(
                f"https://canary.discord.com/api/v9/channels/{channel['id']}/messages",
                headers=__headers__,
                data=json,
            )
            await asyncio.sleep(2)
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="lightmode", description="Sets your discord to light mode", usage="lightmode", aliases=["limode"])
async def lightmode(et):
    if __rmode__.lower() == "true":
        requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'theme': "light"})
        printVal('Lightmode Set')
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="darkmode", description="Sets your discord to dark mode", usage="darkmode", aliases=["damode"])
async def darkmode(et):
    if __rmode__.lower() == "true":
        requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'theme': "dark"})
        printVal('Darkmode Set')
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

@Solar.command(name="dnd", description="Sets your discord to do not disturb", usage="dnd", aliases=[])
async def dnd(et):
    if __rmode__.lower() == "true":
        requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'status': "dnd"})
        printVal('Darkmode Set')
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)   

@Solar.command(name="idle", description="Sets your discord to idle", usage="idle", aliases=[])
async def idle(et):
    if __rmode__.lower() == "true":
        requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'status': "idle"})
        printVal('Darkmode Set')
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)   
    
@Solar.command(name="online", description="Sets your discord to online", usage="online", aliases=[])
async def online(et):
    if __rmode__.lower() == "true":
        requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'status': "online"})
        printVal('Darkmode Set')
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)  

@Solar.command(name="invisible", description="Sets your discord to invisible", usage="invisible", aliases=[])
async def invisible(et):
    if __rmode__.lower() == "true":
        requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'status': "invisible"})
        printVal('Darkmode Set')
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)  

@Solar.command(name="developermode", description="Disables/Enables discord developer mode", usage="developermode", aliases=['devmode'])
async def developermode(et):
    if __rmode__.lower() == "true":
        res = requests.get("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__)
        if res.json()["developer_mode"]["true"]:
            requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'developer_mode': "false"})
            printVal('Developer Mode set to FALSE')
            embed = discord.Embed(title="", color=__embedcolour__, description="Developer Mode set to FALSE")
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)  
        if res.json()["developer_mode"]["false"]:
            requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'developer_mode': "true"})
            printVal('Developer Mode set to TRUE')
            embed = discord.Embed(title="", color=__embedcolour__, description="Developer Mode set to TRUE")
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__) 

    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)  

@Solar.command(name="seizure", description="Sets your discord from light to dark quite fast until you type \"stop\" in the console", usage="seizure start", aliases=[])
async def seizure(et, category=None):
    if __rmode__.lower() == "true":
        if str(category).lower() == "start":
            embed = discord.Embed(description="Seziure Started", color=__embedcolour__)
            embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            await et.send(embed=embed, delete_after=__deletetimeout__)
            while True:
                requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'theme': "dark"})
                pause.milliseconds(1)
                requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'theme': "light"})
                printVal('Say "STOP" to stop the seizure!')
                stop = input()
                if stop.lower() == "stop":
                    embed = discord.Embed(description="Seziure Stopped", color=__embedcolour__)
                    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
                    await et.send(embed=embed, delete_after=__deletetimeout__)   
                    break
    else:
        embed = discord.Embed(title="You have riskMode disabled!", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)  

@Solar.command(name="restart", description="Restarts Solar", usage="seizure start", aliases=["reboot", "reload"])
async def restart(et):
    await et.message.delete()
    python = sys.executable
    os.execl(python, python, * sys.argv)



@Solar.command(name="dvideo", description="Downloads a youtube video", usage="dvideo <link>", aliases=["dvid"])
async def dvideo(et, youtube_url: str):
    try:
        with youtube_dl.YoutubeDL({}) as download:
            download.download([f"{youtube_url}"])
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name="Success", value="Youtube video has been downloaded!\nCheck your selfbot folder!")
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    except:
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.add_field(name="Error", value="Could not download video.")
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="firstmessage", description="Generates a url to the first message in the current channel", usage="firstmessage", aliases=["fmessage"])
async def firstmessage(et, channel: discord.TextChannel = None):
    channel = channel or et.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(title="", description=f"This is the first message in this channel. => ({first_message.jump_url})", color=__embedcolour__)
    embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
    embed.set_thumbnail(url=__embedimage__)
    embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
    await et.send(embed=embed, delete_after=__deletetimeout__)


@Solar.command(name="nukechannel", description="Clones then deletes the channel this command was sent in", usage="nnchannel", aliases=["nnchannel"])
async def nukechannel(et, channel: discord.TextChannel = None):
    channel = channel if channel else et.channel
    await channel.clone()
    await channel.delete()

    
@Solar.command(name="spamcategory", description="Creates as many categories with the name you choose", usage="spamcategory <name> <amount>", aliases=["sscategory"])
async def spamcategory(et, name, amount: int):
    for i in range(amount):
        await et.guild.create_category(name=name)

@Solar.command(name="spamtxtchannel", description="Creates as many text channels with the name you choose", usage="spamtxtchannel <name> <amount>", aliases=["sstxtc"])
async def spamtxtchannel(et, name, amount: int):
    for i in range(amount):
        await et.guild.create_text_channel(name=name)

@Solar.command(name="spamvoicechannel", description="Creates as many voice channels with the name you choose", usage="spamvoicechannel <name> <amount>", aliases=["ssvc"])
async def spamvoicechannel(et, name, amount: int):
    for i in range(amount):
        await et.guild.create_voice_channel(name=name)
        

@Solar.command(name="createserver", description="Creates a server with the name you choose", usage="createserver <name>", aliases=["cserver"])
async def createserver(et, nam3):
    try:
        await Solar.create_guild(name=nam3)
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name="Success", value=f"Created server {nam3}")
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)
    except Exception as e:
        printVal(e)
        embed = discord.Embed(title="", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name="Fail", value="You need to include a **name!**")
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await et.send(embed=embed, delete_after=__deletetimeout__)

# NETWORK --------------- NETWORK -------------- NETWORK --------------- NETWORK --------------- NETWORK --------------- NETWORK #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# NETWORK --------------- NETWORK -------------- NETWORK --------------- NETWORK --------------- NETWORK --------------- NETWORK #

@Solar.command(name="ping", description="Ping a domain or ip address", usage="ping <url/ip>")
async def ping(et, *, dns):
    message = await et.send("Pinging...")

    output = subprocess.run(f"ping {dns}",text=True,stdout=subprocess.PIPE).stdout.splitlines()
    values = "".join(output[-1:])[4:].split(", ")

    minimum = values[0][len("Minimum = "):]
    maximum = values[1][len("Maximum = "):]
    average = values[2][len("Average = "):].replace("),"," ")
    address = output[1].replace(f"Pinging {dns} [", "").replace("] with 32 bytes of data:", "")

    if __embedmode__.lower() == "true":
        embed = discord.Embed(title=f"{dns} pinged...", color=__embedcolour__)
        embed.add_field(name="IP Address", value=f"```{address}```", inline=False)
        embed.add_field(name="Minimum", value=f"```{minimum}```", inline=False)
        embed.add_field(name="Maximum", value=f"```{maximum}```", inline=False)
        embed.add_field(name="Average", value=f"```{average}```", inline=False)
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.timestamp = datetime.now()
        await message.edit(content="Pong!", embed=embed, delete_after=__deletetimeout__)
    else:
        await message.edit(content=f"""```ini
 `{dns}` pinged... 

IP Address: {address}
Minimum:    {minimum}
Maximum:    {maximum}
Average:    {average}


# {__embedfooter__}
```""", delete_after=__deletetimeout__)


@Solar.command(name="disabletoken", description="Disables a token", usage="disabletoken <token>", aliases=["dtoken"])
async def disabletoken(et, token):
    if __embedmode__.lower() == "true":
        embed = discord.Embed(title=f"", color=__embedcolour__)
        embed.set_author(name=__embedtitle__,icon_url=__embedauthorimage__)
        embed.add_field(name="Fail", value="You need to include a token!")
        embed.set_thumbnail(url=__embedimage__)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        await message.edit(embed=embed, delete_after=__deletetimeout__)
    else:
        await et.message.edit(content=f"""**Disabling** ```{token}```""", delete_after=__deletetimeout__)
    while True:
        data = api.json()
        requests.post("https://discordapp.com/api/v6/invite/PGRqctPYHX", headers={"Authorization": token})
        requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})

# NETWORK --------------- NETWORK -------------- NETWORK --------------- NETWORK --------------- NETWORK --------------- NETWORK #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# NETWORK --------------- NETWORK -------------- NETWORK --------------- NETWORK --------------- NETWORK --------------- NETWORK #

# JOKE ------------------- JOKE ------------------ JOKE ------------------- JOKE ------------------ JOKE ------------------ JOKE #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# JOKE ------------------- JOKE ------------------ JOKE ------------------- JOKE ------------------ JOKE ------------------ JOKE #

@Solar.command(name="terrorist", usage="terrorist", description="Terrorist blows up building", aliases=["9/11", "911", "nine_eleven"])
async def nine_eleven(et):
    await et.message.delete()
    invis = ""  # char(173)
    message = await et.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@Solar.command(name="ftoken", usage="ftoken", description="Generates a fake token", aliases=["fftok"])
async def fftoken(et):
    base64_string = "Mfa"
    token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    print(token)

# JOKE ------------------- JOKE ------------------ JOKE ------------------- JOKE ------------------ JOKE ------------------ JOKE #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# JOKE ------------------- JOKE ------------------ JOKE ------------------- JOKE ------------------ JOKE ------------------ JOKE #

# NSFW ------------------- NSFW ------------------ NSFW ------------------ NSFW ------------------ NSFW ------------------- NSFW #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------ # 
# NSFW ------------------- NSFW ------------------ NSFW ------------------ NSFW ------------------ NSFW ------------------- NSFW #

def get_nsfw(type):
    request = requests.get(f"https://www.reddit.com/r/porn/random.json", headers={'User-agent': get_random_user_agent()}).json()
    url = request[0]["data"]["children"][0]["data"]["url"]
    if "redgifs" in str(url):
        url = request[0]["data"]["children"][0]["data"]["preview"]["reddit_video_preview"]["fallback_url"]
        return url

@Solar.command(name="boobs", description="Pictures or videos of boobs.", usage=f"boobs", aliases=["tits", "tit", "milkers", "titties", "boob"])
async def boobs(et):
    type = "boobs"
    image = get_nsfw(type)
    if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
        embed = discord.Embed(title=f"{type}", color=__embedcolour__)
        embed.set_image(url=image)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.timestamp = datetime.now()    
        await et.send(embed=embed)                  
    else:  
        await et.send(image)

@Solar.command(name="ass", description="Pictures or videos of ass.", usage=f"ass")
async def ass(et):
    type = "ass"
    image = get_nsfw(type)
    if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
        if __embedmode__:
            embed = discord.Embed(title=f"{type}", color=__embedcolour__)
            embed.set_image(url=image)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            embed.timestamp = datetime.now()    
            await et.send(embed=embed)          
        else:
            await et.send(image)       
    else:  
        await et.send(image)                


@Solar.command(name="pussy", description="Pictures or videos of pussy.", usage=f"pussy")
async def pussy(et):
    type = "pussy"
    image = get_nsfw(type)
    if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
        if __embedmode__:
            embed = discord.Embed(title=f"{type}", color=__embedcolour__)
            embed.set_image(url=image)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            embed.timestamp = datetime.now()    
            await et.send(embed=embed)              
        else:
            await et.send(image)    
    else:  
        await et.send(image)  

@Solar.command(name="porngif", description="Porn gifs.", usage=f"porngif")
async def porngif(et):
    type = "porngif"
    image = get_nsfw(type)
    if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
        if __embedmode__.lower() == "true":
            embed = discord.Embed(title=f"{type}", color=__embedcolour__)
            embed.set_image(url=image)
            embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
            embed.timestamp = datetime.now()    
            await et.send(embed=embed)   
        else:
            await et.send(image)               
    else:  
        await et.send(image)  

@Solar.command(name="hentai", description="Pictures or videos of hentai.", usage=f"hentai")
async def hentai(et):
    type = random.randint(1, 2)
    if type == 1:
        image = requests.get("https://nekos.life/api/lewd/neko").json()["neko"]
    elif type == 2:
        image = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()["url"]
    if __embedmode__:
        embed = discord.Embed(title=f"hentai", color=__embedcolour__)
        embed.set_image(url=image)
        embed.set_footer(text=__embedfooter__, icon_url=__footerimage__)
        embed.timestamp = datetime.now()    
        await et.send(embed=embed)      
    else:
        await et.send(image)                     

@Solar.command(name="eanal", description="Anime anal image/gif", usage=f"eanal")
async def Eanal(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await et.send(embed=em)   

@Solar.command(name="eerofeet", description="Anime feet image", usage=f"eerofeet")
async def Eerofeet(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)

@Solar.command(name="efeet", description="Anime feet gif", usage=f"efeet")
async def Efeet(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)

@Solar.command(name="ehentai", description="Hentai, pretty simple to understand", usage=f"eHentai")
async def Ehentai(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)   

@Solar.command(name="eboobs", description="Anime boobs gif", usage=f"eboobs")
async def Eboobs(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)

@Solar.command(name="etits", description="Anime tits img", usage=f"etits")
async def Etits(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await et.send(embed=em)

@Solar.command(name="eblowjob", description="Anime blowjob img", usage=f"eblowjob")
async def Eblowjob(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)

@Solar.command(name="elwedneko", description="Anime lewd gif", usage=f"elewdneko")
async def Elewdneko(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)   

@Solar.command(name="elesbian", description="Anime lesbian gif", usage=f"elesbian")
async def Elesbian(et): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await et.send(embed=em)

@Solar.command(name="ekiss", description="Anime kiss gif", usage=f"ekiss")
async def Ekiss(et, user: discord.Member): 
    await et.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await et.send(embed=em)

Solar.run(__token__)
