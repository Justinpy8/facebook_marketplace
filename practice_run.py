from web_functions import *

url = data['url']
username = data['username']
password = data['password']
photo_file_path = "C:/Dev/facebook_marketplace/data/Mouse.jpg"
title = 'Broken old computer mouse'
price = '100'


launching_website(url)
sign_in(username, password)
create_new_listing()
item_for_sale()
upload_photos(photo_file_path)
title_box(title)
price_box(price)
