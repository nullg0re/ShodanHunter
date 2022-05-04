#!/usr/bin/python3
import argparse
from colorama import Fore,Style
from core.amass import passive
from core.amass import active
from core.dns import resolve
from core.helpers import cleanup
from core.helpers import combine_lists
from core.shodanapi import scanner

def get_args():
    p = argparse.ArgumentParser(description="Passive Shodan Port Scanner (OSINT)")
    p.add_argument('-d','--domain',type=str,help="Domain. I.E. example.com")
    p.add_argument('-df','--domainFile', type=str, help="File Containing List of Domains")

    return p.parse_args()

def main():
    args = get_args()

    print (f"{Fore.YELLOW}[*] Passively Collecting Subdomains Now...{Style.RESET_ALL}")
    passive_list = passive(args)

    print (f"{Fore.YELLOW}[*] Actively Collecting Subdomains Now...{Style.RESET_ALL}")
    active_list = active(args)

    print (f"{Fore.YELLOW}[*] Combining Subdomain List and Unique'ing...{Style.RESET_ALL}")
    combined = combine_lists(passive_list, active_list)

    print (f"{Fore.YELLOW}[*] Finding Live Hosts by Resolving Subdomains Now...{Style.RESET_ALL}")
    live = resolve(combined)

    print (f"{Fore.YELLOW}[*] Running Live IPs Against Shodan...{Style.RESET_ALL}")
    scanner(live)

    print (f"{Fore.YELLOW}[*] Cleaning up collected files...{Style.RESET_ALL}")
    cleanup()
if __name__ == '__main__':
    main()


