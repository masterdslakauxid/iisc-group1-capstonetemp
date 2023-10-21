import os
import yaml

#ak
from pathlib import Path

cfg_path = os.path.join(Path.cwd(), 'config' , "app_config.yml")

def is_error():
    return cfg['debug']['error']

def is_debug():
    return cfg['debug']['debug']

def is_info():
    return cfg['debug']['info']

print("App configuration path -> ", cfg_path)

with open(cfg_path, "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

base_path = Path.cwd()    
content_folder = cfg['folders']['content']
pkl_folder = cfg['folders']['pkl']

def get_app_config():    
    return cfg

def get_base_path():

    if is_debug() == True:
        print("Base path --> ", base_path)

    return base_path

def get_content_folder():

    if is_debug() == True:
        print("content_folder --> ", content_folder)
    return content_folder

def get_content_pkl_path():

    content_pkl_path = os.path.join(base_path, content_folder, pkl_folder)
    if is_debug() == True:
        print("content_pkl_path --> ", content_pkl_path)
 
    return content_pkl_path

def get_classified_lable_file_path():

    classified_label_file = os.path.join(content_folder, 'classified_label.txt')
    if is_debug() == True:
        print("classified_label_file --> ", classified_label_file)
 
    return classified_label_file




def get_content_path():

    content_path = os.path.join(base_path, content_folder)
    if is_debug() == True:
        print("content_path --> ", content_path)

    return content_path
