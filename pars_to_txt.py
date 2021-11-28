import os
import datetime
from bs4 import BeautifulSoup as BS

def GOM_txt():
    with open('list.xml', encoding='utf-8') as file:
        src = file.readlines()
        src = ''.join(src)
        content = BS(src, 'lxml')
    info = content.find_all('resource')
    list_for_GOM = []
    social = [
                'vk.com',
                'youtube.com',
                'youtube.com.chanell',
                't.me',
                'instagram.com',
                'ok.ru',
                'facebook.com',
                'www.vk.com',
                'www.youtube.com',
                'www.t.me',
                'www.instagram.com',
                'www.ok.ru',
                'www.facebook.com',
            ]
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    for i in info:
        with open(f'citadel{today}.txt', 'a', encoding='utf-8') as f:
            url = i.find('url')
            if url.text == '-':
                dns = i.find('dns')
                if dns.text == '-':
                    ip = i.find('ip')
                    list_for_GOM.append(ip.text)
                    print(ip.text, file=f)
                else:
                    list_for_GOM.append(dns.text)
                    print(dns.text, file=f)
            else:
                list_for_GOM.append(url.text)
                print(url.text, file=f)
    with open('GOM.txt', 'a') as file:
        for i in list_for_GOM:
            i = i.replace('https://', '')
            i = i.replace('http://', '')
            i = i.replace('\n', '')
            i = i.split('/')
            i = i[0]
            if i not in social:
                print(i,file=file)

def GOM_old_txt():
    with open('list_old.xml', encoding='utf-8') as file:
        src = file.readlines()
        src = ''.join(src)
        content = BS(src, 'lxml')
    info = content.find_all('resource')
    list_for_GOM = []
    for i in info:
        url = i.find('url')
        if url.text == '-':
            dns = i.find('dns')
            if dns.text == '-':
                ip = i.find('ip')
                list_for_GOM.append(ip.text)
            else:
                list_for_GOM.append(dns.text)
        else:
            list_for_GOM.append(url.text)
    social = [
                'vk.com',
                'youtube.com',
                'youtube.com.chanell',
                't.me',
                'instagram.com',
                'ok.ru',
                'facebook.com',
                'www.vk.com',
                'www.youtube.com',
                'www.t.me',
                'www.instagram.com',
                'www.ok.ru',
                'www.facebook.com',
            ]

    with open('GOM_old.txt', 'a') as file:
        for i in list_for_GOM:
            i = i.replace('https://', '')
            i = i.replace('http://', '')
            i = i.replace('\n', '')
            i = i.split('/')
            i = i[0]
            if i not in social :
                print(i,file=file)


