import sys
import tkinter as tk
import json
import os
import logging
#Note that the English language comes from machine translation
lang_list = ['zh_cn.json','en_us.json','zh_ft.json']
logging.basicConfig(format='%(asctime)s: %(filename)s [%(levelname)s]: %(message)s',level=logging.DEBUG,filename='last_log.log',filemode='a')
with open("shuju.json",'r') as f:
    shuju = json.load(f)
    f.close()
lang_list = shuju['lang_list']
lang_xz = str(lang_list[shuju['lang_xl']])
lang = {}
with open(f'lang/{lang_xz}','r') as f:
    lang = json.load(f)
    f.close()

def zy():
    bt.place(x=220,y=100,anchor='w')
    bt_1.place(x=220,y=40,anchor='w')
    re_bt.place(x=220,y=160,anchor='w')
    #up_bt.place(x=220,y=220,anchor='w')
def qcsy():
    bt.place_forget()
    bt_1.place_forget()
    re_bt.place_forget()
    lang_bt.place_forget()
    lang_bt_2.place_forget()
    lang_bt_3.place_forget()
    lang_bt_4.place_forget()
    lang_bt_5.place_forget()
    #lang_bt_6.place_forget()
    lang_back.place_forget()
    #up_bt.place_forget()
    up_lxy_et.place_forget()
    up_bk.place_forget()
def ex_it():
    with open("shuju.json",'w') as f:
        json.dump(shuju,f)
        f.close()
    exit()
def lang_setting():
    num = var.get()
    if num == 0:
        logging.info(f"[setting]: {lang['lang_set_zh_cn']}")
    elif num == 1:
        logging.info(f"[setting]: {lang['lang_set_us']}")
    elif num == 2:
        logging.info(f"[setting]: {lang['lang_set_zh_ft']}")
    elif num == 3:
        logging.info(f"[setting]: {lang['lang_set_fe']}")
    elif num == 4:
        logging.info(f"[setting]: {lang['lang_set_ru']}")
    elif num == 5:
        logging.info(f"[setting]: {lang['lang_set_al']}")
    shuju['lang_xl'] = num
    with open('shuju.json','w') as f:
        json.dump(shuju,f)
        f.close
    qcsy()
    zy()
def lang_set():
    qcsy()
    lang_bt.place(x=100,y=120,anchor='w')
    lang_bt_2.place(x=100,y=80,anchor='w')
    lang_bt_3.place(x=100,y=100,anchor='w')
    lang_bt_4.place(x=100,y=140,anchor='w')
    lang_bt_5.place(x=100,y=60,anchor='w')
    #lang_bt_6.place(x=100,y=160,anchor='w')
    lang_back.place(x=300,y=100,anchor='w')
def reload():
    logging.debug("[setting]: reload!")
    os.execl(sys.executable,sys.executable,*sys.argv)
def up_date():
    qcsy()
    up_lxy_et.place(x=200,y=100,anchor='w')
    up_bk.place(x=350,y=100,anchor='w')
def up_date_sa ():
    qcsy()
    zy()
    shuju['update']['update_URL'] = up_lxy_et.get()
    with open("shuju.json",'w') as f:
        json.dump(shuju,f)
root = tk.Tk()
root.title(lang['title'])
root.geometry("500x500+500+250")
root.resizable(0,0)
var = tk.IntVar()
var_1 = tk.IntVar()

bt = tk.Button(root,text=lang['ex_an_sa'],command=ex_it)
bt_1 = tk.Button(root,text=lang['lang_name'],command=lang_set)
lang_bt = tk.Radiobutton(root,text=lang['lang_cn'],variable=var,value=0)
lang_bt_2 = tk.Radiobutton(root,text=lang['lang_us'],variable=var,value=1)
lang_bt_3 = tk.Radiobutton(root,text=lang['lang_ft'],variable=var,value=2)
lang_bt_4 = tk.Radiobutton(root,text=lang['lang_fe'],variable=var,value=3)
lang_bt_5 = tk.Radiobutton(root,text=lang['lang_ru'],variable=var,value=4)
lang_bt_6 = tk.Radiobutton(root,text=lang['lang_al'],variable=var,value=5)
lang_back = tk.Button(root,text=lang['bk_an_sa'],command=lang_setting)
re_bt = tk.Button(root,text=lang['reload'],command=reload)
#up_bt = tk.Button(root,text=lang['up_set'],command=up_date)
up_lxy_et = tk.Entry(root)
up_bk = tk.Button(root,text=lang['bk_an_sa'],command=up_date_sa)

bt.place(x=220,y=100,anchor='w')
bt_1.place(x=220,y=40,anchor='w')
re_bt.place(x=220,y=160,anchor='w')
#up_bt.place(x=220,y=220,anchor='w')

root.mainloop()