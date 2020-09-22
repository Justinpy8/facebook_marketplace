# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
# import time
import yaml
from os.path import dirname, abspath

# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.maximize_window()


ROOT_DIR = dirname(abspath(__file__))


def load_yaml(filepath):
    with open(filepath, 'r') as info:
        document = yaml.safe_load(info)
    return document


data = load_yaml(f'{ROOT_DIR}/data/credentials.yml')

url = data['url']
print(url)
