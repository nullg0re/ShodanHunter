#!/usr/bin/python3
import concurrent.futures
import dns.resolver
from colorama import Fore,Style

def resolve_ips(sub):
    try:
        answers = dns.resolver.query(sub, 'A')
        for record in answers:
            return (record.to_text())
    except Exception as e:
        return None

def resolve(subs):
    live_hosts = []
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
        future_to_ip = {executor.submit(resolve_ips, sub): sub for sub in subs}
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                results.append(future.result())
            except Exception as e:
                print (f"{Fore.RED}[ ! ] Executor Error: {str(e)}{Style.RESET_ALL}")
    for result in results:
        if result is not None and result not in live_hosts:
            live_hosts.append(result)
        else:
            continue
    print (f"\r\n{Fore.GREEN}[+] Total number of \"live\" hosts: {str(len(live_hosts))}{Style.RESET_ALL}")
    return live_hosts
