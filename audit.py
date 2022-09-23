from array import array
from ast import Constant
from asyncio.windows_events import NULL
import os
import platform
from subprocess import PIPE, run

############### FUNCTIONS #################
def cmd(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

################ OS/ARCHITECTURE DETECTION ################
opsys = platform.system()
print("Operating System:", opsys)
archsys = platform.processor()
print("Processor Family:", archsys)
if (opsys == "Windows"):
    ip = cmd("ipconfig | findstr \"IPv4\"")
    nm = cmd("ipconfig | findstr \"Subnet\"")
else:
    ip = cmd("ip a | grep \"inet\"")
    nm = cmd("ip a | grep \"netmask\"")
################ IP RANGE FINDER ###############
iptemp = ip.splitlines()

def ipformat(strarray):
     x = range(3)
     for i in x:
        temp = strarray[i].split(":")
        temp1 = temp[1].strip()
        return temp1
            
iplist = ipformat(iptemp)
print(iplist)

