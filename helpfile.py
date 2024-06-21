import json
import huancun
import logging
logging.basicConfig(format='%(asctime)s: %(filename)s [%(levelname)s]: %(message)s',level=logging.DEBUG,filename='last_log.log',filemode='a')
lang_list = ['zh_cn.json','en_us.json','zh_ft.json']
with open("shuju.json",'r') as f:
    shuju = json.load(f)
    f.close()
lang_xz = str(lang_list[shuju['lang_xl']])
lang = {}
with open(f'lang/{lang_xz}','r') as f:
    lang = json.load(f)
    f.close()
co_de = huancun.co_de
print(len(co_de))
if len(co_de) == 1:
    print(lang['help_list'])
    logging.info(f'[System]: {lang["help_list"]}')