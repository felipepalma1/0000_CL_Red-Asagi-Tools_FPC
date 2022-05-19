import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# Metralleta
for x in range(1,100):
    r = requests.get('http://192.168.1.102:8081/api/v1/bikes', verify=False)

print("Red Asagi One\n")

print(f'{r.json()} \n')
