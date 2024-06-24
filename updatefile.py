import pip
try:
    import wget
except ImportError:
    if input("wget module not found, do you want to install it?[y/n]") == 'y':
        pip.main(['install','wget'])
        import wget
    else:
        print("wget module not found, please install it manually")
        exit()
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
if not shuju['update']['auto_update']:
    try:
        os.makedirs("update the cache")
    except:
        pass
    try:
        os.remove("update the cache/shuju.json")
    except:
        pass
    wget.download(url_jc,out=cache_lj,bar=None)
    try:
        with open("update the cache/shuju.json",'r') as f:
                up_sj = json.load(f)
                f.close()
        if up_sj['update']['version'] > shuju['update']['version']:
                wget.download(url,lj+"/update the cache",bar=None)
                file = zipfile.ZipFile(lj+'\\update the cache\\easy_lang-main.zip')
                file.extractall(lj + '\\update the cache\\easy_lang-main')
                file.close()
                get_files = os.listdir(lj+"\\update the cache\\easy_lang-main\\easy_lang-main\\")
                base_dir = lj + '\\update the cache\\easy_lang-main\\easy_lang-main\\'
                shutil.rmtree(lj + "\\lang\\")
                shutil.move(lj + "\\update the cache\\easy_lang-main\\easy_lang-main\\lang\\",lj)
                files = [os.path.join(base_dir,file) for file in os.listdir(base_dir)]
                for g in files:
                    print(g)
                    shutil.copy2(g,lj + "\\")
                get_files = os.listdir(lj + "\\update the cache\\")
                for dirname in get_files:
                    dirname = lj + "\\update the cache" + "\\" + dirname
                    if os.path.isfile(dirname):
                        os.remove(dirname)
                    elif os.path.isdir(dirname):
                        dellist =os.listdir(dirname)
                        for f in dellist:
                            file_path = os.path.join(dirname,f)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                print("ok!")
                logging.info("[update]: upgrade ok")
        else:
                os.remove(lj + "\\update the cache\\shuju.json")
                print("no update")
    except FileNotFoundError:
        print("[update]: Don't update!")
        logging.warning("[System]: Don't update!")
def update():
    try:
        os.makedirs("update the cache")
    except:
        pass
    try:
        os.remove("update the cache/shuju.json")
    except:
        pass
    wget.download(url_jc,out=cache_lj,bar=None)
    try:
        with open("update the cache/shuju.json",'r') as f:
                up_sj = json.load(f)
                f.close()
        if up_sj['update']['version'] > shuju['update']['version']:
                wget.download(url,lj+"/update the cache",bar=None)
                file = zipfile.ZipFile(lj+'\\update the cache\\easy_lang-main.zip')
                file.extractall(lj + '\\update the cache\\easy_lang-main')
                file.close()
                get_files = os.listdir(lj+"\\update the cache\\easy_lang-main\\easy_lang-main\\")
                base_dir = lj + '\\update the cache\\easy_lang-main\\easy_lang-main\\'
                shutil.rmtree(lj + "\\lang\\")
                shutil.move(lj + "\\update the cache\\easy_lang-main\\easy_lang-main\\lang\\",lj)
                files = [os.path.join(base_dir,file) for file in os.listdir(base_dir)]
                for g in files:
                    print(g)
                    shutil.copy2(g,lj + "\\")
                get_files = os.listdir(lj + "\\update the cache\\")
                for dirname in get_files:
                    dirname = lj + "\\update the cache" + "\\" + dirname
                    if os.path.isfile(dirname):
                        os.remove(dirname)
                    elif os.path.isdir(dirname):
                        dellist =os.listdir(dirname)
                        for f in dellist:
                            file_path = os.path.join(dirname,f)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                print("ok!")
                logging.info("[update]: upgrade ok")
        else:
                os.remove(lj + "\\update the cache\\shuju.json")
                print("no update")
    except FileNotFoundError:
        print("[update]: Don't update!")
        logging.warning("[System]: Don't update!")