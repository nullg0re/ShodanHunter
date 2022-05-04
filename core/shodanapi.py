#!/usr/bin/python3
from shodan import Shodan
from tabulate import tabulate
api = Shodan("<SHODAN-API-KEY-HERE>")

def scanner(ips):
    resources = []
    for ip in ips:
        try:
            ipinfo = api.host(ip)
            hostname = ipinfo["hostnames"]
            ports = ipinfo["ports"]
            for item in ipinfo["data"]:
                try:
                    product = item["product"]
                except Exception as e:
                    product = "Service Product Could Not Be Identified"
            resources.append([hostname, product, ports])
        except Exception as e:
            continue

    print (tabulate(resources, headers=["Hostnames", "Product", "Open Ports"], tablefmt="github"))
