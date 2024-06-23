import wget
import json
import logging
import os
import zipfile
import shutil
lj_1 = os.path.abspath(__file__)
lj = os.path.dirname(lj_1)
cache_lj = lj + "\\update the cache"
url = "https://www.github.com/liang_work/easy_lang/shuju.json"
url_jc = "https://raw.githubusercontent.com/liang-work/easy_lang/main/shuju.json"
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
    try:
        os.remove("\\update the cache\\shuju.json")
    except:
        pass
    wget.download(url_jc,out=cache_lj,bar=None)
    #try:
    with open("update the cache/shuju.json",'r') as f:
            up_sj = json.load(f)
            f.close()
    if up_sj['update']['version'] > shuju['update']['version']:
            wget.download(url,lj,bar=None)
            file = zipfile.ZipFile(lj+'\\easy_lang-main.zip')
            file.extractall(lj + '\\update the cache\\easy_lang-main.zip')
            file.close()
            #os.remove(lj)
            print("ok!")
            logging.info("[update]: upgrade ok")
    else:
            os.remove(lj + "\\update the cache\\shuju.json")
    #except FileNotFoundError:
    print("[update]: Don't update!")
    logging.warning("[System]: Don't update!")
def update():
    wget.download(url_jc,cache_lj + '\\shuju.json',bar=None)
    try:
        with open(lj+"\\update the cache\\shuju.json",'r') as f:
            up_sj = json.load(f)
            f.close()
        if up_sj['update']['version'] > shuju['update']['version']:
            wget.download(url,lj,bar=None)
            file = zipfile.ZipFile(lj+'\\easy_lang-main.zip')
            file.extractall(lj+'\\update the cache')
            file.close()
            #os.remove(lj)
            print("ok!")
            print("注意：目前不支持主动将文件替换，需要手动操作")
            logging.info("[update]: upgrade ok")
        else:
            os.remove(lj +"\\update the cache\\shuju.json")
            print("no update")
            logging.info("[update]: no update")
    except FileNotFoundError:
        print("[System]: Don't update!")
        logging.warning("[System]: Don't update!")
    except:
        print("未知错误！")
    