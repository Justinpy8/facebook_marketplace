from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
import time
import yaml
from os.path import dirname, abspath

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(20)
driver.maximize_window()

ROOT_DIR = dirname(abspath(__file__))


def load_yaml(filepath):
    """Initiating safe loading the yaml file from dir path"""
    with open(filepath, 'r') as info:
        document = yaml.safe_load(info)
    return document


data = load_yaml(f'{ROOT_DIR}/data/credentials.yml')


def launching_website(url):
    driver.get(url)
    print(f"{url} is loading")


def sign_in(username, password):
    """Entering the email address"""
    email_address = driver.find_element_by_xpath("//input[@placeholder='Email or Phone']")
    email_address.clear()
    email_address.send_keys(username)
    print("Email is being entered as the user name")

    """Entering the password"""
    pw = driver.find_element_by_xpath("//input[@placeholder='Password']")
    pw.clear()
    pw.send_keys(password)
    print("Password is entered")

    """Clicking on the sing in button"""
    sign_in_button = driver.find_element_by_xpath(
        "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p bwm1u5wc']")
    sign_in_button.click()
    print("Clicked on the sign in button")
    time.sleep(2)
