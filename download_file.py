import requests
import os

def download():
    os.rename('list.xml', "list_old.xml")
    file = open('list.xml', 'wb')
    link = link
    data = {
        'name': login,
        'pass': password
    }
    responce = requests.post(url=link, data=data, verify='/home/horn313/GIEs_auto/belgie-by-chain.pem').content
    file.write(responce)
    file.close()

