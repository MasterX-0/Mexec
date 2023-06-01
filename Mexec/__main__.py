import os
import sys

import time
import requests
import urllib.request
from datetime import datetime
from time import sleep
import asyncio
from asyncio import *
# import pyrogram
# from pyrogram import *
# from pyrogram.types import *
from requests import get,post
from plugins.colors import C
from Mexec import LOGGER
import platform

system = platform.system()
release = platform.release()

class MEXECFIG(object):
	REQ_FILE = "req.py"

async def CLS():
	os.system('cls' if os.name == 'nt' else 'clear')

async def INSTALL_REQ():
	if os.path.isfile(f"{MEXECFIG.REQ_FILE}"):
		os.system(f"python3 {MEXECFIG.REQ_FILE}")
	else:
		await LOGGER(INFO=f"{C.LIGHT_WHITE}Requirements are not found !!", TMexec=int(3))
		await LOGGER(INFO=f"Installing requirements...", TMexec=int(1))
		await LOGGER(INFO=f"Plz wait...", TMexec=int(1))

MEXEC_SLOGO = f"""
{C.RED} ___ ___{C.LIGHT_BLUE}
{C.RED}|   Y   .{C.LIGHT_BLUE}-----.--.--.-----.----.
{C.RED}|{C.LLIGHT_GREEN}.{C.RED}      |{C.LIGHT_BLUE}  -__|_   _|  -__|  __|
{C.RED}|{C.LLIGHT_GREEN}.{C.RED} \_/  |{C.LIGHT_CYAN}_____|__.__|_____|____|
{C.YELLOW}|{C.LLIGHT_GREEN}:{C.RED}  |   |
{C.YELLOW}|{C.LLIGHT_GREEN}::.{C.RED}|{C.LLIGHT_GREEN}:.{C.RED} |{C.LIGHT_WHITE}                   {C.BOLD}v1.1
{C.YELLOW}`--- ---'{C.END}
"""

async def LOGO():
	print ()
	print (MEXEC_SLOGO)

async def CHK_INTERNET(google='https://www.google.com/'):
    try:
        urllib.request.urlopen(google)
        return True
    except:
        return False

async def PRINT_HELP():
	print (f"""
{C.BOLD}Mexec Pormapt Commands :{C.END}

    {C.FAINT}start{C.END} - Start the SSH Crack.
    {C.FAINT}help{C.END} - Get the Mexec help message.
    {C.FAINT}clear{C.END} - Clear the terminal.
    {C.FAINT}exit{C.END} - Exit the Mexec.
""")

async def EXIT():
        print ()
        l=['|','/','-','\\','|','/','-','\\']
        for i in l+l+l:
                sys.stdout.write('\r'f'{C.YELLOW}Exiting... '+i)
                sys.stdout.flush()
                time.sleep (0.2)
        print (" \n")
        sys.exit(1)

async def START_MENU():
        await CLS()
        await LOGO()

async def PORMAPT():
	while True:
		try:
			mexec_z = input(f"{C.LIGHT_RED}Mexec{C.END} :{C.BLUE}~{C.END}>{C.END} ")
		except KeyboardInterrupt:
			await LOGGER(INFO=f"Stop signal received !", TMexec=int(1))
			await LOGGER(INFO=f"Please wait !", TMexec=int(1))
			await LOGGER(INFO=f"Exiting...", TMexec=int(1))
			await EXIT()
		if mexec_z == "exit" or mexec_z == "Exit":
			await EXIT()
		elif mexec_z == "" or mexec_z == " " or mexec_z == "  " or mexec_z == "   ":
			pass
		elif mexec_z == "Clear" or mexec_z == "clear":
			await CLS()
			await LOGO()
		elif mexec_z == "Help" or mexec_z == "help":
			await PRINT_HELP()
		else:
			try:
				if mexec_z == "start":
					print ()
					ssh_ip = input(f"{C.END}Enter Target IP : ")
					ssh_user = input(f"{C.END}Enter SSH Username : ")
					pass_list = input(f"{C.END}Enter Passwords File : ")
					if os.path.exists(pass_list) == False:
						print ()
						await LOGGER(INFO=f"That passwords file does not exist !", TMexec=int(4))
						await LOGGER(INFO=f"Please try again.", TMexec=int(4))
						await sleep(3)
						await PORMAPT()
				else:
					await LOGGER(INFO=f"{C.LIGHT_WHITE}[{C.END}{C.ITALIC}{mexec_z}{C.END}{C.LIGHT_WHITE}] -{C.END} Command Not Found !!", TMexec=int(7))
					await LOGGER(INFO=f"Type {C.FAINT}help{C.END} to get help message.", TMexec=int(6))
			except Exception as rz:
				await LOGGER(INFO=f"ERROR", TMexec=int(5))

async def CNSPR():
	await LOGGER(INFO=f"Starting the {C.BOLD}Mexec{C.END} !", TMexec=int(2))
	await LOGGER(INFO=f"System : {system} {release}", TMexec=int(1))
	await LOGGER(INFO=f"Please wait...", TMexec=int(1))
	await LOGGER(INFO=f"Checking the internet connection !", TMexec=int(1))
	await LOGGER(INFO=f"Connecting...", TMexec=int(1))
	if await CHK_INTERNET():
		await LOGGER(INFO=f"Connected !", TMexec=int(1))
		await LOGGER(INFO=f"Internet connection is good !", TMexec=int(1))
		print ()
		await START_MENU()
		await PORMAPT()
	else:
		await LOGGER(INFO=f"You are offline.", TMexec=int(3))
		await LOGGER(INFO=f"Please check your internet internet connection and try again letter !", TMexec=int(4))
		await LOGGER(INFO=f"Type {C.FAINT}python3 -m Mexec{C.END} to start {C.BOLD}Mexec{C.END} again.", TMexec=int(4))
		await EXIT()

async def main_startup():
	try:
		await LOGO()
		await CNSPR()
	except Exception as e:
		print (e)

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
