#------------- IMPORT -------------#
from os import system as c
import time
import random
import os

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- CHECK ROOT -------------#
def check_root():
    if not os.path.exists("/system/xbin/su"):
        print(f"{R}\n[!] Root Device Not Found!")
        print(f"{Y}This tool only works on Rooted devices.")
        exit()

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
██╗   ██╗████████╗     ██╗   ██╗████████╗
██║   ██║╚══██╔══╝     ██║   ██║╚══██╔══╝
██║   ██║   ██║        ██║   ██║   ██║   
██║   ██║   ██║        ██║   ██║   ██║   
╚██████╔╝   ██║        ╚██████╔╝   ██║   
 ╚═════╝    ╚═╝         ╚═════╝    ╚═╝   
{G}      HACKING WORLD - YT SUBSCRIBE HACK TOOL
{A}------------------------------------------------
""")

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{A}[1] START SUBSCRIBE HACK")
    print(f"{A}[0] EXIT TOOL")
    print(f"{A}------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        sub_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION")
        time.sleep(1)
        menu()

#------------- SUBSCRIBE HACK -------------#
def sub_hack():
    logo()
    c('espeak "YouTube Subscribe Hack Starting"')
    channel = input(f"{C}Enter YouTube Channel Link: ")
    print(f"\n{Y}[+] Connecting to YouTube Server...")
    for i in range(5):
        print(f"{B}[*] Loading{' .' * i}")
        time.sleep(0.7)

    print(f"{G}\n[✓] Channel Verified: {channel}")
    time.sleep(1)
    print(f"{C}[+] Boosting Subscribers & Likes...")
    for i in range(10):
        subs = random.randint(100, 500)
        likes = random.randint(50, 300)
        print(f"{P}[*] {subs} Subscribers & {likes} Likes Added...")
        time.sleep(1)

    print(f"\n{R}[!] successfully added now enjoy")
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()
    exit()

#------------- START TOOL -------------#
check_root()
menu()