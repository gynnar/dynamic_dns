import socket
import requests
import configparser
import os

script_dir = (os.path.dirname(__file__))
config_file = 'config.ini'
config_path = os.path.join(script_dir, config_file)
print (os.path.isfile(config_path))

if (os.path.exists(config_path)):
    config = configparser.ConfigParser()
    config.read(config_path)
    check_ip_url = config.get('URLS', 'IP_CHECK_URL')
    update_ip_url = config.get('URLS', 'UPDATE_URL')
    username = config.get('USER', 'USERNAME')
    password = config.get('USER', 'PASSWORD')
    hostname = config.get('HOST','HOSTNAME')
    print (hostname)
else:
    check_ip_url = 'https://www.myexternalip.com/raw'
    update_ip_url = 'https://dyndns.loopia.se'
    username = '#Put your username here#'
    password = '#Put your password here#'
    hostname = '#Put your hostname here#'

dns_addr = socket.gethostbyname(hostname)           # Check the IP connected to the hostname by the DNS-system
response = requests.get(check_ip_url)               # Check the external IP seen by the internet.
str_response = str(response.content, 'utf-8')       # Stringifies the response to match the type of the dns-check

if ( dns_addr == str_response ):
    print ("DNS-record matches external IP, no action required")
else :
    str_update_url = ( update_ip_url + "?hostname=" + hostname + "&myip=" + str_response )
    print (str_update_url)
    response = requests.get(str_update_url, auth=(username, password))
    print (response.content)
