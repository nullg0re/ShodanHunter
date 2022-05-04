#!/usr/bin/python3
import subprocess
from colorama import Fore,Style

def combine_lists(_list1, _list2):
    final_subs = []
    for x in _list1:
        if x not in final_subs:
            final_subs.append(x)
    for x in _list2:
        if x not in final_subs:
            final_subs.append(x)
    print (f"{Fore.CYAN}[*] Total Combined Unique Subdomains: {str(len(final_subs))}{Style.RESET_ALL}")
    return final_subs

def save_to_disk(filename, _list):
    f = open(filename, 'w')
    for x in _list:
        f.write(x + "\n")
    f.close()
    print (f"{Fore.YELLOW}[*] Final Hostnames Saved To: ./{filename}{Style.RESET_ALL}")

def cleanup():
    cmd = "rm passive.txt active.json"
    subprocess.call(cmd.split())
