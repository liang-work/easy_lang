##!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Winston.Wang
#main file
#This file is the main file of the easy lang.
#It is used to run the program.
#The program is divided into several modules, including:
#dayin.py: This module is used to read the code entered by the user and execute it.
#huancun.py: This module is used to compile the code entered by the user.
#updatefile.py: This module is used to update the program.
#helpfile.py: This module is used to display the help information.
#setting.py: This module is used to set the language and other settings.
import json
import os
import logging
#import dayin Temporarily useless
import huancun
import updatefile
import sys
import platform
lj = os.path.abspath(__file__)
logging.basicConfig(format='%(asctime)s: %(filename)s [%(levelname)s]: %(message)s',level=logging.DEBUG,filename='last_log.log',filemode='w')
#Note that the English language comes from machine translation
sm = {}
at_dt = {}
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
    
with open("lang/agreement.json",'r') as f:
    agree = json.load(f)
    f.close()
if not shuju['agree']:
    print(agree[lang_xz])
    if input() == 'y':
        shuju['agree'] = True
        with open("shuju.json",'w') as f:
            json.dump(shuju,f)
            f.close()
        pass
    else:
        exit()
try:
    with open("cache.json",'r') as f:
        sm = json.load(f)
        f.close()
except:
    if os.name == 'nt':
        sm['system'] = 'windows'
    elif os.name == 'posix':
        sm['system'] = 'linux'
    else:
        sm['system'] = 'unknown'
    sm['python_version'] = platform.python_version()
    sm["stm"] = platform.platform()
    sm['s_b'] = platform.architecture()[0]
    with open("cache.json",'w') as f:
        json.dump(sm,f)
        f.close()
logging.info(f'[System]: {sm["system"]}')
logging.info(f"{lang['eyl_version']}:{shuju['version']}")
logging.info(lang['load_value'])
logging.info("start!")
print("system:",sm['system']+ str(sm['s_b'])+f" python version:{sm['python_version']}"+" easy lang version:"+shuju['version'])
#logging.info("system:",sm['system']+ str(sm['s_b'])+f" python version:{sm['python_version']}"+" easy lang version:"+shuju['version'])
try:
    while True:
        i_v = ''
        i_v = input(f"{lj} >>>")
        logging.info(f"[user]: {i_v}")
        code = i_v.split()
        #print(code)
        huancun.co_de = code
        if code:
            if code[0] == 'version' or code[0] == '-V':
                os.system("python version.py")
            if code[0] == 'exit' or code[0] == 'exit()':
                logging.info("stopping!")
                logging.info("exit code : 0,it's normal exit")
                exit()
            if code[0] == 'setting':
                try:
                    import tkinter
                    
                    logging.info(f"[System]: setting start!")
                    os.system("python setting.py")
                    logging.info(f"[System]: setting stop!")
                except ImportError:
                    input_str = input(f"{lang['set_run_error']}[y/n]")
                    logging.error(f"[System] :{lang['set_run_error']}")
                    if input_str == 'y':
                        os.system("python setting_2.py")
                    else:
                        pass
            if code[0] == 'help':
                os.system("python helpfile.py")
            if code[0] == 'clear' or code[0] == 'cls':
                if  not len(code) >1:
                    os.system("cls")
                    logging.info("[System]: clear cmd!")
            if code[0] == 'update' or code[0] == 'upgrade':
                updatefile.update()
            if code[0] == 'clear_cache':
                print(lang['clear_cache'])
                logging.info(f"[System]: {lang['clear_cache']}")
                with open("cache.json",'w') as f:
                    json.dump(at_dt,f)
                    f.close()
            #if len(code) >=1:
                #dy = dayin.bl_dy
            
        else:
            continue
except KeyError:
    print(lang['keyerror'])
    logging.warning(f'[System]: {lang["keyerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except ValueError:
    print(lang['valueerror'])
    logging.warning(f'[System]: {lang["valueerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except SyntaxError:
    print(lang['syntaxerror'])
    logging.warning(f'[System]: {lang["syntaxerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except TypeError:
    print(lang['typeerror'])
    logging.warning(f'[System]: {lang["typeerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except IndexError:
    print(lang['indexerror'])
    logging.warning(f'[System]: {lang["indexerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except AttributeError:
    print(lang['attributeerror'])
    logging.warning(f'[System]: {lang["attributeerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except NameError:
    print(lang['nameerror'])
    logging.warning(f'[System]: {lang["nameerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except FileNotFoundError:
    print(lang['filenotfounderror'])
    logging.warning(f'[System]: {lang["filenotfounderror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except StopIteration:
    print(lang['stopiteration'])
    logging.warning(f'[System]: {lang["stopiteration"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except AssertionError:
    print(lang['assertionerror'])
    logging.warning(f'[System]: {lang["assertionerror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except EOFError:
    print(lang['eoferror'])
    logging.warning(f'[System]: {lang["eoferror"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")
except KeyboardInterrupt:
    print(lang['keyboardinterrupt'])
    logging.warning(f'[System]: {lang["keyboardinterrupt"]}')
    logging.info("stopping!")
    logging.info("exit code : -1,it's abnormal exit.")