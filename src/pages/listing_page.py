from src.all_imports import *
from selenium.webdriver.support.select import Select
from src.pages.base_page import *

logs = utils.create_logger()


class LoginPage(BasePage):
    def sign_in(self, username, password):
        """Entering the email address"""
        email_address = self.driver.find_element_by_xpath("//input[@placeholder='Email or Phone']")
        email_address.clear()
        email_address.send_keys(username)
        logs.info("Email is being entered as the user name")


class ListingCreationPage(BasePage):
    def launching_website(self, url):
        self.driver.get(url)
        logs.info(f"{url} is loading")

    def sign_in(self, username, password):
        """Entering the email address"""
        email_address = self.driver.find_element_by_xpath("//input[@placeholder='Email or Phone']")
        email_address.clear()
        email_address.send_keys(username)
        logs.info("Email is being entered as the user name")

        """Entering the password"""
        pw = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
        pw.clear()
        pw.send_keys(password)
        time.sleep(1)
        pw.send_keys(Keys.RETURN)
        logs.info("Password is entered")

    def create_new_listing(self):
        """Select the 'Create New Listing' button"""
        new_listing = self.driver.find_element_by_xpath(
            "//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[6]/div/span/a/div[1]/div[2]/span/span")
        new_listing.click()
        time.sleep(2)
        logs.info("Click on the 'Create New Listing' button.")

    def item_for_sale(self):
        """Select the 'Item For Sale' option"""
        for_sale_button = self.driver.find_element_by_xpath("//span[contains(text(),'Item for Sale')]")
        for_sale_button.click()
        time.sleep(2)
        logs.info("Choosing the 'Item for Sale' option.")

    def upload_photos(self, photo_file_name):
        """Upload photo file"""
        upload_xpath = self.driver.find_element_by_xpath("//input[@class='mkhogb32' and contains(@accept, 'image')]")
        full_path = f"C:/Dev/facebook_marketplace/data/{photo_file_name}"
        upload_xpath.send_keys(full_path)
        time.sleep(3)
        logs.info("Photo file is uploaded.")

    def title_box(self, title):
        title_line = self.driver.find_element_by_xpath("//label[@aria-label='Title']//input[contains(@id, 'jsc_c_')]")
        title_line.send_keys(title)
        logs.info(f"Entered {title} to the title box")

    def price_box(self, price):
        price_line = self.driver.find_element_by_xpath("//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]")
        price_line.send_keys(price)
        logs.info(f"Entered {price} to the price box")

    def category_list(self):
        """Performs the click function to bring up the category dropdown list"""
        category = self.driver.find_element_by_xpath("//input[@aria-label='Category']")
        category.click()
        time.sleep(1)
        logs.info("Bringing up the the main category dropdown menu")

    def maincat_electronics(self):
        """'maincat' is the first layer on the category list."""
        electronics = self.driver.find_element_by_xpath(
            "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[9]/div/div[1]/div/div[1]/div/div/div/span/span")
        electronics.click()
        time.sleep(2)
        logs.info("Selected 'Electronics' from the category list")

    def subcat1_computer(self):
        """subcat1 is the first layer on the subcategory list"""
        computers = self.driver.find_element_by_xpath(
            "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[6]/div/div[1]/div/div[1]/div/div/div/span/span")
        computers.click()
        time.sleep(1)
        logs.info("Selected 'Computers, Laptops & Tablets' from the subcategory list.")

    def subcat2_accessories(self):
        """subcat2 is the second layer on the subcategory list"""
        accessories = self.driver.find_element_by_xpath(
            "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[4]/div/div[1]/div/div[1]/div/div/div/span/span")
        accessories.click()
        time.sleep(1)
        logs.info("Selected 'Computer Peripherals & Accessories' from the subcategory list")

    def subcat3_mice(self):
        """subcat3 is the third layer on the subcategory list"""
        mice = self.driver.find_element_by_xpath(
            "//*[contains(@id,'jsc_c_')]/div/div/div/div/div/span/div/div[5]/div/div[1]/div/div[2]/div/div/i")
        mice.click()
        time.sleep(1)
        logs.info("Selected 'Mice, Trackballs & Touchpads' from the subcategory list")

    def condition_list(self, condition):
        condition_button = self.driver.find_element_by_xpath(
            "//label[@aria-label='Condition']//*[contains(@id,'jsc_c_')]/div")
        condition_button.click()

        if condition == "Fair":
            used_fair = self.driver.find_element_by_xpath("//span[contains(text(),'Used - Fair')]")
            used_fair.click()
            logs.info("Condition:Used - Fair")
        elif condition == "Good":
            used_good = self.driver.find_element_by_xpath("//span[contains(text(),'Used - Good')]")
            used_good.click()
            logs.info("Condition:Used - Good")
        elif condition == "Like New":
            used_like_new = self.driver.find_element_by_xpath("//span[contains(text(),'Used - Like New')]")
            used_like_new.click()
            logs.info("Condition:Used - Like New")
        elif condition == "New":
            new = self.driver.find_element_by_xpath(
                "//div[@class='rq0escxv l9j0dhe7 du4w35lb']//div[@class='rq0escxv l9j0dhe7 du4w35lb']//div[@class='j34wkznp qp9yad78 pmk7jnqg kr520xx4']//div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']//div[1]//div[1]//div[1]//div[1]//span[1]")
            new.click()
            logs.info("Condition: New")

    def next_button(self):
        self.driver.find_element_by_xpath("//div[@aria-label='Next']//span[contains(text(), 'Next')]").click()
        logs.info("Click on the next button")

    def location_box(self, zipcode):
        """Finding location by zipcode"""
        postal_code = self.driver.find_element_by_xpath("//input[@aria-label='Enter a city']")
        postal_code.send_keys(Keys.CONTROL, "a")
        postal_code.send_keys(zipcode)
        time.sleep(5)

        """Select the first result by default"""
        first_option_xpath = f"//ul[@class='buofh1pr cbu4d94t j83agx80']//span[contains(text(),'{zipcode}')]"
        first_option_element = self.driver.find_element_by_xpath(first_option_xpath)
        first_option_element.click()
        logs.info(f"Selected location by ZipCode: {zipcode}")

    def publish_button(self):
        """Click on the publish button to submit the listing"""
        publish = self.driver.find_element_by_xpath("//div[@aria-label='Publish']//span[contains(text(),'Publish')]")
        publish.click()
        time.sleep(10)
        self.screen_shots("Listing_Confirmation")
        logs.info("Listing has been published and a screen shot is being saved")

    def listing_verification_url(self):
        """Verifying if the listing is created successfully by checking the URL"""
        listing_url = self.driver.current_url
        assert listing_url == 'https://www.facebook.com/marketplace/you/selling', 'There is a mismatch in the url, please double check the listing.'
        logs.info("The URL matches, listing is successfully executed!!")
        time.sleep(5)

    def listing_verification_title(self, title):
        """Verifying if the listing is created successfully by comparing the title(s) of the active item(s)"""
        active_item1_xpath = f"//div[@class='tvmbv18p']//span[contains(text(),'{title}')]"
        active_item1 = self.driver.find_element_by_xpath(active_item1_xpath)
        time.sleep(5)
        assert active_item1.is_displayed()
        logs.info("Active listing item title is verified")

    def remove_listing(self):
        """Remove the listing and confirm if the removal is being executed"""
        self.driver.find_element_by_xpath(
            "//div[@aria-label='More']/div/div/i").click()
        time.sleep(2)
        delete_listing_button = self.driver.find_element_by_xpath(
            "//div[@role='menu']//span[contains(text(),'Delete Listing')]")
        delete_listing_button.click()
        time.sleep(1)
        delete_confirm_button = self.driver.find_element_by_xpath("//div[@aria-label='Delete']/div/div/span/span")
        delete_confirm_button.click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        logs.info("Listing has been removed!")

    def removal_verification_title(self, title):
        try:
            active_item1_xpath = f"//div[@class='tvmbv18p']//span[contains(text(),'{title}')]"
            active_item1 = self.driver.find_element_by_xpath(active_item1_xpath)
            assert not active_item1.is_displayed(), logs.error(
                'Listing removal failed, listing web element is still being found!')
            time.sleep(5)
        except NoSuchElementException as err:
            logs.info("Listing removal was a success!")
            logs.info("Listing item xpath no longer being found with the following error message:")
