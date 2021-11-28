import os
from paramiko import SSHClient, AutoAddPolicy
import datetime
from download_file import download
from bs4 import BeautifulSoup as BS
from pars_to_txt import GOM_txt, GOM_old_txt
from GOM_lists import GOM_lists, GOM_new,GOM_old
from tg_bot import telega_bot_error, telega_bot_result
import libapi

try:
    download()
    telega_bot_result('Файл скачал, ща поработаю')

    with open('list.xml', encoding='utf-8') as file:
        src = file.readlines()
        src = ''.join(src)
        content = BS(src, 'lxml')
    date_new = content.find('resources').get('date')

    with open('list_old.xml', encoding='utf-8') as file:
        src = file.readlines()
        src = ''.join(src)
        content = BS(src, 'lxml')
    date_old = content.find('resources').get('date')
    if date_new == date_old:
        telega_bot_result('Ну, ничего нового не добавили, так что я сворачиваюсь на сегодня')
        os.remove('list_old.xml')
        exit()
    else:
        telega_bot_result('Так, там че то добавили - работаю дальше')
        GOM_txt()
        GOM_old_txt()
        telega_bot_result('Файлы для GOM сформировал, еду дальше')

        GOM_lists()
        telega_bot_result('Списки для GOM сформировал, приступаю к сравнению')

        add_host = []
        delete_host = []
        x,y = 0,0
        for i in GOM_new:
            if i not in GOM_old and i not in add_host:
                add_host.append(i)
                x += 1
        telega_bot_result(f'В общем надо бы добавить {x} сайтов')
        for i in GOM_old:
            if i not in GOM_new and i not in delete_host:
                delete_host.append(i)
                y += 1
        telega_bot_result(f'И удалить надо {y} сайтов')

        host = 'host_ip'
        password = 'password'
        if x > 0:
            x1 = 0
            s = libapi.socketOpen(host)
            dev_api = libapi.ApiRos(s)
            dev_api.login(username=username, pwd=password)
            for i in add_host:
                command = ['/ip/firewall/address-list/add', '=list=GIEs', f'=address={i}']
                dev_api.writeSentence(command)
                res = libapi.readResponse(dev_api)
                x1 += 1
            libapi.socketClose(s)
            telega_bot_result(f'Добавил {x1} сайтов')
        if y > 0:
            # y1 = 0
            # ssh = SSHClient()
            # ssh.set_missing_host_key_policy(AutoAddPolicy())
            # ssh.connect('host_ip', username=username, password=password, allow_agent=False, look_for_keys=False)
            # for i in delete_host:
            #     remove_host = f'/ip firewall address-list remove [find address={i} list=GIEs]'
            #     ssh.exec_command(remove_host)
            #     y1 += 1
            # ssh.close()
            telega_bot_result(f'Надо удалить след. сайты: {delete_host}')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        os.rename('GOM.txt', f'GOM_{today}.txt')
        os.rename('GOM_old.txt', f'GOM_old_{today}.txt')
        os.remove('list_old.xml')
        telega_bot_result(f'И также поудалял ненужные файлы, на сегодня всё - я сворачиваюсь')
except Exception as error:
    telega_bot_error(error)