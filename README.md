# dynamic_dns
My ISP does not offer static IP addresses, so I wrote a small python script to check if my external IP matches the DNS record of my domain name. My DNS service provider is Loopia. If my router has been assigned a new DHCP-address the script sends a request to Loopia to update the DNS-record with the new IP.

### Prereqs:
- A python 3 installation.
- requests module installed in python (using python-pip: pip install requests)
- configparser module installed in python (pip install configparser)

### Settings:

The script needs a few settings:
- The domain name to be monitored/updated
- Username to the DNS Service Provider account
- The password to the account
- An url to check the external IP of your system
- An url to the DNS Service Providers update mechanism.

These settings can either be set in a config.ini file or be set in the else-clause of the script. You pick...
Look at config.ini_example if you want to use it. 

### How to use it:
#### Linux
Download it and place it in a folder you think is good. 
Edit the config file with your info.
Make a record in your crontab to execute as often as you'd like. 
- crontab -e
- #EXAMPLE LINE#


I know there are fancier and much more competent clients out there, but I just wanted to code a little myself.
