import json
import os
import logging
import io
import pprint
output = io.StringIO()
logging.basicConfig(format='%(asctime)s - %(filename)s [%(levelname)s]: %(message)s',level=logging.DEBUG,filename='last_log.log',filemode='a')
shuju = {}
with open("shuju.json",'r') as f:
    shuju = json.load(f)
    f.close()
print(f'version:{shuju["version"]}')
logging.info(f"[System]: {shuju['version']}")
os.system("pause")
logging.info("pause!")