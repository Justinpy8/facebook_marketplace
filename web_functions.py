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

driver = webdriver.Chrome(options=chrome_options)

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

    # """Clicking on the sign in button"""
    # sign_in_button = driver.find_element_by_xpath(
    #     "//*[@id='login_form']//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5']")
    # sign_in_button.click()
    # print("Clicked on the sign in button")
    # time.sleep(2)


def create_new_listing():
    """Select the 'Create New Listing' button"""
    new_listing = driver.find_element_by_xpath(
        "//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[6]/div/span/a/div[1]/div[2]/span/span")
    new_listing.click()
    time.sleep(2)
    print("Click on the 'Create New Listing' button.")


def item_for_sale():
    """Select the 'Item For Sale' option"""
    for_sale_button = driver.find_element_by_xpath("//span[contains(text(),'Item for Sale')]")
    for_sale_button.click()
    time.sleep(2)
    print("Choosing the 'Item for Sale' option.")


def upload_photos(photo_file_name):
    """Upload photo file"""
    upload_xpath = driver.find_element_by_xpath("//input[@class='mkhogb32' and contains(@accept, 'image')]")
    full_path = f"C:/Dev/facebook_marketplace/data/{photo_file_name}"
    upload_xpath.send_keys(full_path)
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
    driver.find_element_by_xpath("//div[@aria-label='Next']//span[contains(text(), 'Next')]").click()
    print("Click on the next button")


def location_box(zipcode):
    """Finding location by zipcode"""
    postal_code = driver.find_element_by_xpath("//input[@aria-label='Enter a city']")
    postal_code.send_keys(Keys.CONTROL, "a")
    postal_code.send_keys(zipcode)
    time.sleep(5)

    """Select the first result by default"""
    first_option_xpath = f"//ul[@class='buofh1pr cbu4d94t j83agx80']//span[contains(text(),'{zipcode}')]"
    first_option_element = driver.find_element_by_xpath(first_option_xpath)
    first_option_element.click()
    print(f"Selected location by ZipCode: {zipcode}")


def publish_button():
    """Click on the publish button to submit the listing"""
    publish = driver.find_element_by_xpath("//div[@aria-label='Publish']//span[contains(text(),'Publish')]")
    publish.click()
    print("Listing has been published")
    time.sleep(20)


def listing_verification_url():
    """Verifying if the listing is created successfully by checking the URL"""
    listing_url = driver.current_url
    assert listing_url == 'https://www.facebook.com/marketplace/you/selling', 'There is a mismatch in the url, please double check the listing.'
    print("The URL matches, listing is successfully executed!!")
    time.sleep(5)


def listing_verification_title(title):
    """Verifying if the listing is created successfully by comparing the title(s) of the active item(s)"""
    active_item1_xpath = f"//div[@class='tvmbv18p']//span[contains(text(),'{title}')]"
    active_item1 = driver.find_element_by_xpath(active_item1_xpath)
    time.sleep(5)
    assert active_item1.is_displayed()
    print("Active listing item title is verified")


def remove_listing():
    """Remove the listing and confirm if the removal is being executed"""
    driver.find_element_by_xpath(
        "//div[@aria-label='More']//i[@class='hu5pjgll lzf7d6o1 sp_SwTRn0N9BuB sx_3f967d']").click()
    time.sleep(2)
    delete_listing_button = driver.find_element_by_xpath("//div[@role='menu']//span[contains(text(),'Delete Listing')]")
    delete_listing_button.click()
    time.sleep(1)
    delete_confirm_button = driver.find_element_by_xpath(
        "//*[@id='mount_0_0']/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span/span")
    delete_confirm_button.click()
    ignore_survey = driver.find_element_by_xpath(
        "//div[@aria-label='Close']//div[@class='s45kfl79 emlxlaya bkmhp75w spb7xbtv i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3']")
    ignore_survey.click()
    print("Listing has been removed!")


def removal_verification_title(title):
    active_item1_xpath = f"//div[@class='tvmbv18p']//span[contains(text(),'{title}')]"
    active_item1 = driver.find_element_by_xpath(active_item1_xpath)
    time.sleep(5)
    assert not active_item1.is_displayed()
    print("Listing removal is verified!!")


def close_browser():
    driver.close()
