import none as none
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


def create_new_listing():
    new_listing = driver.find_element_by_xpath("//span[contains(text(),'Create New Listing')]")
    new_listing.click()
    time.sleep(2)
    print("Click on the 'Create New Listing' button.")


def item_for_sale():
    for_sale_button = driver.find_element_by_xpath("//span[contains(text(),'Item for Sale')]")
    for_sale_button.click()
    time.sleep(2)
    print("Choosing the 'Item for Sale' option.")


def upload_photos(photo_file_path):
    image_update = driver.find_element_by_xpath("//input[@class='mkhogb32' and contains(@accept, 'image')]")
    image_update.send_keys(photo_file_path)
    time.sleep(3)
    print("Photo file is uploaded.")


def title_box(title):
    title_line = driver.find_element_by_xpath("//label[@aria-label='Title']//input[contains(@id, 'jsc_c_')]")
    title_line.send_keys(title)
    print(f"Entered {title} to the title box")


def price_box(price):
    price_line = driver.find_element_by_xpath("//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]")
    price_line.send_keys(price)
    print(f"Entered {price} to the price box")


def category_list():
    category = driver.find_element_by_xpath("//input[@aria-label='Category']")
    category.click()
    time.sleep(1)
    print("Bringing up the the main category dropdown menu")


def maincat_electronics():
    electronics = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[9]/div/div[1]/div/div[1]/div/div/div/span/span")
    electronics.click()
    time.sleep(1)
    print("Selected 'Electronics' from the category list")


def subcat1_computer():
    computers = driver.find_element_by_link_text("//span[contains(text(),'Computers, Laptops & Tablets')]")
    computers.click()
    time.sleep(1)
    print("Selected 'Computers, Laptops & Tablets' from the subcategory list.")


def subcat2_accessories():
    accessories = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[4]/div/div[1]/div/div[1]/div/div/div/span/span")
    accessories.click()
    time.sleep(1)
    print("Selected 'Computer Peripherals & Accessories' from the subcategory list")


def subcat3_mice():
    mice = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[5]/div/div[1]/div/div[1]/div/div/div[1]/span/span]")
    mice.click()
    time.sleep(1)
    print("Selected 'Mice, Trackballs & Touchpads' from the subcategory list")


def condition_list(condition):
    if condition == "Fair":
        used_fair = driver.find_element_by_xpath("//span[contains(text(),'Used - Fair')]")
        used_fair.click()
        print("Condition:Used - Fair")
    elif condition == "Good":
        used_good = driver.find_element_by_xpath("//span[contains(text(),'Used - Good')]")
        used_good.click()
        print("Condition:Used - Good")
    elif condition == "Like New":
        used_like_new = driver.find_element_by_xpath("//span[contains(text(),'Used - Good')]")
        used_like_new.click()
        print("Condition:Used - Like New")
    # elif condition == "New":
    #     new = driver.find_element_by_xpath("")
