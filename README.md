# ShodanHunter

A tool to quickly identify open ports and potential vulnerabilities through passive OSINT.

This tool will run amass passively against a given target for 10 minutes.

It will then run amass actively against a given target for 10 minutes.

InfraHunter.py will then iterate through all of the collected possible IP address and attempt to identify it's DNS A record.

With the list of valid IP addresses, InfraHunter will then query Shodan to identify open ports and possible CVE details for the identified live IPs.

This tool can be used against a single domain or a list of domains with the amass switch `-df` or `--domainFile`


## Usage
```bash
$ python3 ShodanHunter.py --help  

usage: ShodanHunter.py [-h] [-d DOMAIN] [-df DOMAINFILE]

Passive Shodan Port Scanner (OSINT)

options:

  -h, --help                                show this help message and exit

  -d DOMAIN, --domain DOMAIN                Domain. I.E. example.com

  -df DOMAINFILE, --domainFile DOMAINFILE   File Containing List of Domains
```
