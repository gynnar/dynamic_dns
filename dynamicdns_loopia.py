"""
Auth: David Gunnarsson
Date 2020-02-something

Since my ISP at home gives my router an public IP-address I wrote this script that:
- checks  my routers external IP.
- checks which IP is reported when someone does a DNS-query against my domain name
- If it differs from the routers IP it updates the DNS-record.
- If it's the same the script is happy and exits.

The script is cron-sheduled (daily) in a debian based server in my home network.
Crontab example:
3 16 * * * python3 /*full_path_to_script/dynamicdns_loopia.py
It is adapted to Loopias DNS-service.
The settings-file (config.ini) is placed in the same directory as the script

"""
import socket
import requests
import configparser
import os
import dns.resolver

script_dir = (os.path.dirname(__file__))
config_file = 'config.ini'
config_path = os.path.join(script_dir, config_file)
#print (os.path.isfile(config_path))

if (os.path.exists(config_path)):
    config = configparser.ConfigParser()
    config.read(config_path)
    check_ip_url = config.get('URLS', 'IP_CHECK_URL')
    update_ip_url = config.get('URLS', 'UPDATE_URL')
    username = config.get('USER', 'USERNAME')
    password = config.get('USER', 'PASSWORD')
    hostname = config.get('HOST','HOSTNAME')
#    print (hostname)
else:
    check_ip_url = 'https://www.myexternalip.com/raw'
    update_ip_url = 'https://dyndns.loopia.se'
    username = '#Put your username here#'
    password = '#Put your password here#'
    hostname = '#Put your hostname here#'

# dns_addr = socket.gethostbyname(hostname)           # Check the IP connected to the hostname by the DNS-system
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']
dns_addr = my_resolver.query(hostname)

#############

response = requests.get(check_ip_url)               # Check the external IP seen by the internet.
str_response = str(response.content, 'utf-8')       # Stringifies the response to match the type of the dns-check

if ( dns_addr == str_response ):
    print ("DNS-record matches external IP, no action required")
else :
    str_update_url = ( update_ip_url + "?hostname=" + hostname + "&myip=" + str_response )
    # print (str_update_url)
    response = requests.get(str_update_url, auth=(username, password))
    print ("DNS-record update attempted with response:")
    print (response.content)
