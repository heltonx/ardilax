#tested in python 3.11

#OVER GIANT SHOULDERS

'''
some good stuff :
https://datagy.io/python-requests-json/
https://www.geeksforgeeks.org/response-json-python-requests/
https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0
https://github.com/GozOnTheCode/IpLocalisator-Osint/blob/main/main.py
https://stackoverflow.com/questions/9093684/how-to-print-particular-json-value-in-python
https://patorjk.com/software/taag/#p=display&f=Alligator&t=Type%20Something%20
https://ascii.co.uk/art/zebra
'''

#general libraries
import sys

#"gatherer" libraries
import requests
import json

#"portscan" libraries
import socket
import subprocess
import importlib.util

def portScan(host):
    ports = [21,22,23,25,53,80,111,135,139,443,445,3306,8080,9090]

    for port in ports:
        client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((host, port))
        if code == 0:
            try:
                service = socket.getservbyport(port)
                print ("Open port found: ", port, " - ", service)
            except:
                continue

def geoData(host):
    response = requests.get(f'http://ip-api.com/json/{host}')
    resp_dict = response.json()
    print(json.dumps(resp_dict, indent=4, sort_keys=False))

def secData(host):
    response = requests.get(f'https://proxycheck.io/v2/{host}?key=111111-222222-333333-444444&vpn=1&asn=1')
    resp_dict = response.json()
 
    proxy = resp_dict[host]['proxy']
    type = resp_dict[host]['type']
    provider = resp_dict[host]['provider']
    org = resp_dict[host]['organisation']

    printable_values = [
           {
            'PROXY': f'{proxy}',
            'TYPE': f'{type}',
            'PROVIDER': f'{provider}',
            'ORGANISATION': f'{org}'
            },
        ]
    
    print(json.dumps(printable_values, indent=4, sort_keys=False))
    
def netData(host):
    response = requests.get(f'https://proxycheck.io/v2/{host}?key=111111-222222-333333-444444&vpn=1&asn=1')
    resp_dict = response.json()

    range = resp_dict[host]['range']
    asn = resp_dict[host]['asn']
    provider = resp_dict[host]['provider']
    org = resp_dict[host]['organisation']

    printable_values = [
           {
            'RANGE': f'{range}',
            'ASN': f'{asn}',
            'PROVIDER': f'{provider}',
            'ORGANISATION': f'{org}'
            },
        ]
    
    print(json.dumps(printable_values, indent=4, sort_keys=False))

def main():
    
    opcao = input('''
                  
  ___          _ _ _            
 / _ \        | (_) |           
/ /_\ \_ __ __| |_| | __ ___  __
|  _  | '__/ _` | | |/ _` \ \/ /
| | | | | | (_| | | | (_| |>  < 
\_| |_/_|  \__,_|_|_|\__,_/_/\_\                    
                  
    \\/),
   ,'.' /,
  (_)- / /,
     /\_/ |__..--,  *
    (\___/\ \ \ / ).'
     \____/ / (_ //
      \\_ ,'--'\_(
      )_)_/ )_/ )_)
 mrf (_(_.'(_.'(_.'
                              
1) Internal IP port scan          [     IPv4    ]
2) Public IP port scan            [     IPv4    ]
3) IP Geolocation Data            [ IPv4 / IPv6 ]
4) IP check if it is Proxy / VPN  [ IPv4 / IPv6 ]
5) IP Network / Provider data     [ IPv4 / IPv6 ]
6) Exit

        Choose an option: ''')
    
    if opcao == '1':
        host = input("Enter a IP/Host: ")
        try:
            (portScan(host))
        except:
            print("Invalid option!")
	
    elif opcao == '2':
        host = input("Enter a IP/Host: ")
        try:
            portScan(host)
        except:
            print("Invalid option!")

    elif opcao == '3':
        host = input("Enter a IP/Host: ")
        try:
            geoData(host)
        except:
            print("Invalid option!")

    elif opcao == '4':
        host = input("Enter a IP/Host: ")
        try:
            secData(host)
        except:
            print("Invalid option!")

    elif opcao == '5':
        host = input("Enter a IP/Host: ")
        try:
            netData(host)
        except:
            print("Invalid option!")

    elif opcao == '6':
        sys.exit()

if __name__ == "__main__":
    main()
