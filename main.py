## Made by Buck3ts41

import pyMeow as pm 
import os
from colorama import Fore
import time
from render import overlay

def main():
    os.system("cls")
    print('[+] Made by Buck3ts41', '\n')
    print('[+] Loading offsets for 1.3.0.2')
    try:
        from offsets import health, armor, team, pos, fpos, name, player_count, entity_list, local_player, view_matrix
    except:
        print(Fore.RED + '[-] Offsets not found')
        time.sleep(3)
        exit()
    print(Fore.GREEN + '[+] Offsets loaded')
    time.sleep(0.5)
    print(Fore.WHITE + '[+] Checking if game is running')
    
    if not pm.process_exists('ac_client.exe'):
        print(Fore.RED + '[-] Game is not running')
        time.sleep(3)
        exit()
    print(Fore.GREEN + '[+] Found ac_client.exe', '\n')
    
    print(Fore.WHITE + '[+] Getting module base address')
    from memory import AccessGame
    try: 
        proc, base = AccessGame()
    except:
        print(Fore.RED + '[-] Module base address not found')
        time.sleep(3)
        exit()
      
    print(Fore.GREEN + '[+] Module base address:', base)
    print(Fore.WHITE + '[+] Loading overlay', '\n')
    
    overlay()
    
main()
    