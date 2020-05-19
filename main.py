#!/usr/bin/env python3
import requests
import click
import json


def get_token(user, passwd, tower_api_url):
    creds = (user, passwd)
    response = requests.post(f'{tower_api_url}/tokens/', auth=creds, verify=False)
    response.raise_for_status()
    token_json = response.json()
    token = token_json["token"]
    return token

def get_inventories(token,  page_size=200):
    headers = {'Authorization': 'Bearer ' + token}
    url = f'{tower_api_url}/inventories?&page_size={page_size}'
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def cleanup_hosts(token, page_size=200):
    inventories_list = get_inventories(token=token, page_size=page_size)
    counter = inventories_list["count"]
    if (inventories_list["count"] == 0):
        print("Inventory count is zero so no more inventories left for deletion")
        exit(1)
    while counter > 0:
        for inventory in inventories_list["results"]: 
            print(inventory["name"])
        counter -= 1
    return counter
   
user="bbdjshbhjb"
passwd="vdjvjd"
tower_api_url=" "
token = get_token(user, passwd, tower_api_url)
page_size=200
inventories = cleanup_hosts(token=token, page_size=page_size)
print(inventories)