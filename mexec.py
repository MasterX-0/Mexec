import os
import sys
from os import system as mexec_sys

class C(object):
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[1;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    LIGHT_YELLOW = "\033[0;33m"
    LLIGHT_GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LLIGHT_CYAN = "\033[0;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

class MEXECFIG(object):
	REQ_NOTFOUND = """

"""
	REQ_FILE = "req.py"

def INSTALL_REQ():
	print (MEXECFIG.REQ_NOTFOUND)
	if os.path.isfile(f"{MEXECFIG.REQ_FILE}"):
		mexec_sys(f"python3 {MEXECFIG.REQ_FILE}")
	else:
		return

try:
	import requests
	import time
	import base64
	import pyrogram
	from pyrogram import *
	from pyrogram.types import *
	import asyncio
	from asyncio import *
	from time import sleep
	import datetime
	from datetime import datetime
except ModuleNotFoundError:
	INSTALL_REQ()

class MEXEC_LOGOs(object):
	MEXEC_SLOGO = f"""
{C.RED} ___ ___{C.LIGHT_BLUE}
{C.RED}|   Y   .{C.LIGHT_BLUE}-----.--.--.-----.----.
{C.RED}|.      |{C.LIGHT_BLUE}  -__|_   _|  -__|  __|
{C.RED}|. \_/  |{C.LIGHT_CYAN}_____|__.__|_____|____|
{C.YELLOW}|:  |   |
{C.YELLOW}|::.|:. |{C.LIGHT_WHITE}                   {C.BOLD}v1.1
{C.YELLOW}`--- ---'{C.END}
"""

def LOGGER(INFO, TMexec):
	NOW = datetime.now().strftime("%H:%M:%S")
	if TMexec == 1:
		TxMexec = f"{C.LLIGHT_GREEN}INFO{C.END}"
	elif TMexec == 2:
		TxMexec = f"{C.GREEN}INFO{C.END}"
	elif TMexec == 3:
		TxMexec = f"{C.YELLOW}WARNING{C.END}"
	elif TMexec == 4:
		TxMexec = f"{C.LIGHT_YELLOW}WARNING{C.END}"
	elif TMexec == 5:
		TxMexec = f"\033[1;40mERROR{C.END}"
	else:
		TxMexec = f"\033[1;46mWARNING{C.END}"
	print (f"{C.LIGHT_WHITE}[{C.LLIGHT_CYAN}{NOW}{C.LIGHT_WHITE}] [{TxMexec}{C.LIGHT_WHITE}]{C.END} {INFO}")

