import json
import logging
import os
import sys


sm={}
logging.basicConfig(format='%(asctime)s: %(filename)s [%(levelname)s]: %(message)s',level=logging.DEBUG,filename='last_log.log',filemode='a')
lang_list = ['zh_cn.json','en_us.json','zh_ft.json']
with open("shuju.json",'r') as f:
    shuju = json.load(f)
    f.close()
    
lang_list = shuju['lang_list']
lang_xz = str(lang_list[shuju['lang_xl']])
lang = {}

with open(f'lang/{lang_xz}','r') as f:
    lang = json.load(f)
    f.close()
    
with open("cache.json",'r') as f:
    sm = json.load(f)
    f.close()
while True:
    print(f"           {lang['title']}")
    print("key                               function")
    print("------------------------------------------")
    print(f"[0]                              {lang['ex_an_sa']}")
    print(f"[1]                              {lang['reload']}")
    print(f"[2]                              {lang['lang_name']}")
    i_v=input()
    if sm['system'] == 'windows':
        os.system('cls')
    elif sm['system'] == 'linux':
        os.system('clear')
    if i_v == '0':
        if shuju != {}:
            with open("shuju.json",'w') as f:
                json.dump(shuju,f)
                f.close()
            exit()
    elif i_v == '1':
        logging.debug("[setting]: reload!")
        os.execl(sys.executable,sys.executable,*sys.argv)
    elif i_v == '2':
        print(f"           {lang['lang_name']}")
        print("key                               function")
        print("------------------------------------------")
        print(f"[0]                              {lang['lang_cn']}")
        print(f"[1]                              {lang['lang_us']}")
        print(f"[2]                              {lang['lang_ft']}")
        print(f"[3]                              {lang['lang_ru']}")
        print(f"[4]                              {lang['lang_fe']}")
        i_v=input()
    if i_v == '0':
        logging.info(f"[setting]: {lang['lang_set_zh_cn']}")
    elif i_v == '1':
        logging.info(f"[setting]: {lang['lang_set_us']}")
    elif i_v == '2':
        logging.info(f"[setting]: {lang['lang_set_zh_ft']}")
    elif i_v == '3':
        logging.info(f"[setting]: {lang['lang_set_fe']}")
    elif i_v == '4':
        logging.info(f"[setting]: {lang['lang_set_ru']}")
    elif i_v == '5':
        logging.info(f"[setting]: {lang['lang_set_al']}")
    if i_v == '0':
        shuju['lang_xl'] = 0
    elif i_v == '1':
        shuju['lang_xl'] = 1
    elif i_v == '2':
        shuju['lang_xl'] = 2
    elif i_v == '3':
        shuju['lang_xl'] = 3
    elif i_v == '4':
        shuju['lang_xl'] = 4
    elif i_v == '5':
        shuju['lang_xl'] = 5
    with open("shuju.json",'w') as f:
        json.dump(shuju,f)
        f.close()
    if sm['system'] == 'windows':
        os.system('cls')
    elif sm['system'] == 'linux':
        os.system('clear')
        os.execl(sys.executable,sys.executable,*sys.argv)