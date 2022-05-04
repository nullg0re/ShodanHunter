#!/usr/bin/python3
import os
import json
import signal
import subprocess
from time import sleep
from colorama import Fore, Style

def passive(args):
    subdomains = []
    if args.domain:
        # run amass by domain
        subprocess.Popen(['amass','enum','--passive','-norecursive', '-d',args.domain,'-o','passive.txt'])
        sleep(600)
        subprocess.Popen(['killall', 'amass'])
        sleep(15)
    elif args.domainFile:
        # run amass by domain file
        subprocess.Popen(['amass','enum','--passive','-norecursive', '-df', args.domainFile,'-o','passive.txt'])
        sleep(600) 
        subprocess.Popen(["killall", 'amass'])
        sleep(15)
    else:
        print (f"{Fore.RED}[!] Must use '-d' or '-df'.  Check Help Menu (-h).{Style.RESET_ALL}")
        exit()

    with open('passive.txt', 'r') as amass_txt:
        for line in amass_txt:
            subdomains.append(line.strip())
    print (f"{Fore.CYAN}[*] Total Passive Subdomains: {str(len(subdomains))}{Style.RESET_ALL}")
    return subdomains

def active(args):
    subdomains = []
    if args.domain:
        # run amass by domain
        subprocess.Popen(['amass','enum','-active','-norecursive','-d',args.domain,'-json','active.json'])
        sleep(600) 
        subprocess.Popen(['killall', 'amass'])
        sleep(15)
    elif args.domainFile:
        # run amass by domain file
        subprocess.Popen(['amass','enum','-active','-norecursive','-df',args.domainFile,'-json','active.json'])
        sleep(600) 
        subprocess.Popen(['killall', 'amass'])
        sleep(15)
    else:
        print (f"{Fore.RED}[!] Must use '-d' or '-df'. Check Help Menu (-h).{Style.RESET_ALL}")
        exit()

    with open("active.json", 'r') as amass_json:
        for line in amass_json:
            entry = json.loads(line.strip())
            subdomains.append(entry.get("name"))
    print (f"{Fore.CYAN}[*] Total Active Subdomains: {str(len(subdomains))}{Style.RESET_ALL}") 
    return subdomains
