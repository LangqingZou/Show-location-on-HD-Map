## importing socket module
import socket
import requests
import json
from requests import get

ip = get('https://api.ipify.org').text
# print(f'My public IP address is: {ip}')
# print(extract_ip())

request_url = 'https://geolocation-db.com/jsonp/' + ip
# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
# Clean the returned string so it just contains the dictionary data for the IP address
result = result.split("(")[1].strip(")")
# Convert this data into a dictionary
result  = json.loads(result)
print(result)

