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
    time.sleep(1)
    pw.send_keys(Keys.RETURN)
    print("Password is entered")

    """Clicking on the sign in button"""
    sign_in_button = driver.find_element_by_xpath(
        "//*[@id='login_form']//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']")
    sign_in_button.click()
    print("Clicked on the sign in button")
    time.sleep(2)


def create_new_listing():
    """Select the 'Create New Listing' button"""
    new_listing = driver.find_element_by_xpath("//a[@aria-label='Create New Listing']//span[contains(text(),'Create New Listing')]")
    new_listing.click()
    time.sleep(2)
    print("Click on the 'Create New Listing' button.")


def item_for_sale():
    """Select the 'Item For Sale' option"""
    for_sale_button = driver.find_element_by_xpath("//span[contains(text(),'Item for Sale')]")
    for_sale_button.click()
    time.sleep(2)
    print("Choosing the 'Item for Sale' option.")


def upload_photos(photo_file_path):
    """Upload photo file"""
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
    """Performs the click function to bring up the category dropdown list"""
    category = driver.find_element_by_xpath("//input[@aria-label='Category']")
    category.click()
    time.sleep(1)
    print("Bringing up the the main category dropdown menu")


def maincat_electronics():
    """'maincat' is the first layer on the category list."""
    electronics = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[9]/div/div[1]/div/div[1]/div/div/div/span/span")
    electronics.click()
    time.sleep(2)
    print("Selected 'Electronics' from the category list")


def subcat1_computer():
    """subcat1 is the first layer on the subcategory list"""
    computers = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[6]/div/div[1]/div/div[1]/div/div/div/span/span")
    computers.click()
    time.sleep(1)
    print("Selected 'Computers, Laptops & Tablets' from the subcategory list.")


def subcat2_accessories():
    """subcat2 is the second layer on the subcategory list"""
    accessories = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[4]/div/div[1]/div/div[1]/div/div/div/span/span")
    accessories.click()
    time.sleep(1)
    print("Selected 'Computer Peripherals & Accessories' from the subcategory list")


def subcat3_mice():
    """subcat3 is the third layer on the subcategory list"""
    mice = driver.find_element_by_xpath(
        "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[5]/div/div[1]/div/div[2]/div/div/i")
    mice.click()
    time.sleep(1)
    print("Selected 'Mice, Trackballs & Touchpads' from the subcategory list")


def condition_list(condition):
    condition_button = driver.find_element_by_xpath("//label[@aria-label='Condition']//*[contains(@id,'jsc_c_')]/div")
    condition_button.click()

    if condition == "Fair":
        used_fair = driver.find_element_by_xpath("//span[contains(text(),'Used - Fair')]")
        used_fair.click()
        print("Condition:Used - Fair")
    elif condition == "Good":
        used_good = driver.find_element_by_xpath("//span[contains(text(),'Used - Good')]")
        used_good.click()
        print("Condition:Used - Good")
    elif condition == "Like New":
        used_like_new = driver.find_element_by_xpath("//span[contains(text(),'Used - Like New')]")
        used_like_new.click()
        print("Condition:Used - Like New")
    elif condition == "New":
        new = driver.find_element_by_xpath(
            "//div[@class='rq0escxv l9j0dhe7 du4w35lb']//div[@class='rq0escxv l9j0dhe7 du4w35lb']//div[@class='j34wkznp qp9yad78 pmk7jnqg kr520xx4']//div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']//div[1]//div[1]//div[1]//div[1]//span[1]")
        new.click()
        print("Condition: New")


def next_button():
    driver.find_element_by_link_text(
        "//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5 ojkyduve']").click()
    print("Click on the next button")


def location_box(zipcode):
    """Finding location by zipcode"""
    postal_code = driver.find_element_by_xpath("//input[@aria-label='Enter a city']")
    postal_code.send_keys(zipcode)

    """Choose the first result by zipcode"""
    action = ActionChains(driver)
    action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()


def publish_button():
    """Click on the publish button to submit the listing"""
    publish = driver.find_element_by_xpath(
        "//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5 ojkyduve']")
    publish.click()
