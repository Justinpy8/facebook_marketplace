from src.all_imports import *
from src.utilities import *

data = utils.load_yaml("C:/Dev/facebook_marketplace/data/credentials.yml")
logs = utils.create_logger()

# Parameters:

url = data['url']
username = data['username']
password = data['password']
photo_file_name = 'Mouse.jpg'
title = 'Broken old computer mouse'
price = '100'
condition = 'New'
zipcode = "10003"


@pytest.mark.listing_creation
@pytest.mark.listing_creation_positive
def test_listing_creation_case1(driver):
    logs.info("Starting listing creation positive case test #1!")
    listing = ListingCreationPage(driver)
    listing.launching_website(url)
    listing.sign_in(username, password)
    listing.create_new_listing()
    listing.item_for_sale()
    listing.upload_photos(photo_file_name)
    listing.title_box(title)
    listing.price_box(price)
    listing.category_list()
    listing.maincat_electronics()
    listing.subcat1_computer()
    listing.subcat2_accessories()
    listing.subcat3_mice()
    listing.condition_list(condition)
    listing.next_button()
    listing.location_box(zipcode)
    listing.publish_button()
    listing.listing_verification_url()
    listing.listing_verification_title(title)
    listing.remove_listing()
    listing.removal_verification_title(title)
