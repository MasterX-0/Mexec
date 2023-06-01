import os,asyncio,time
from datetime import datetime
from time import sleep
from plugins.colors import C

async def LOGGER(INFO, TMexec):
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
		TxMexec = f"\033[1;41mERROR{C.END}"
	elif TMexec == 6:
		TxMexec = f"\033[1;44mNOTE{C.END}"
	else:
		TxMexec = f"\033[1;45mWARNING{C.END}"
	sleep(0.50)
	print (f"{C.LIGHT_WHITE}[{C.LLIGHT_CYAN}{NOW}{C.LIGHT_WHITE}] - [{C.END}Mexec{C.LIGHT_WHITE}] - [{TxMexec}{C.LIGHT_WHITE}] -{C.END} {INFO}")
