import wget
import json
import logging
import os
import zipfile
lj_1 = os.path.abspath(__file__)
lj = os.path.dirname(lj_1) + '\\cache\\shuju.json'
cache_lj = lj
url = "https://www.github.com/liang_work/easy_lang/shuju.json"
url_jc = "https://www.github.com/liang_work/easy_lang/shuju.json"
logging.basicConfig(format='%(asctime)s: %(filename)s [%(levelname)s]: %(message)s',level=logging.DEBUG,filename='last_log.log',filemode='w')
#Note that the English language comes from machine translation
lang_list = ['zh_cn.json','en_us.json']
with open("shuju.json",'r') as f:
    shuju = json.load(f)
    f.close()
lang_xz = str(lang_list[shuju['lang_xl']])
lang = {}
with open(f'lang/{lang_xz}','r') as f:
    lang = json.load(f)
    f.close()
url = shuju['update']['update_URL']
if shuju['update']['auto_update']:
    wget.download(url,cache_lj,bar=None)
    try:
        with open("cache/shuju.json",'r') as f:
            up_sj = json.load(f)
            f.close()
        if up_sj['update']['version'] > shuju['update']['version']:
            wget.download(url,lj,bar=None)
            file = zipfile.ZipFile(lj+'\\easy_lang-main.zip')
            file.extractall(lj_1)
            file.close()
            os.remove(lj)
            print("ok!")
            logging.info("[update]: upgrade ok")
        else:
            os.remove(lj)
    except FileNotFoundError:
        print("[update]: Don't update!")
        logging.warning("[System]: Don't update!")
def update():
    wget.download(url,cache_lj,bar=None)
    try:
        with open("cache/shuju.json",'r') as f:
            up_sj = json.load(f)
            f.close()
        if up_sj['update']['version'] > shuju['update']['version']:
            wget.download(url,lj,bar=None)
            file = zipfile.ZipFile(lj+'\\easy_lang-main.zip')
            file.extractall(lj_1)
            file.close()
            os.remove(lj)
            print("ok!")
            logging.info("[update]: upgrade ok")
        else:
            os.remove(lj)
            print("no update")
            logging.info("[update]: no update")
    except FileNotFoundError:
        print("[System]: Don't update!")
        logging.warning("[System]: Don't update!")
    