from web_functions import *

url = data['url']
username = data['username']
password = data['password']
photo_file_path = "C:/Dev/facebook_marketplace/data/Mouse.jpg"
title = 'Broken old computer mouse'
price = '100'
condition = 'New'
zipcode = "10032"




launching_website(url)
sign_in(username, password)
create_new_listing()
item_for_sale()
upload_photos(photo_file_path)
title_box(title)
price_box(price)
category_list()
maincat_electronics()
subcat1_computer()
subcat2_accessories()
subcat3_mice()
condition_list(condition)
next_button()
location_box(zipcode)
