# Importing the required libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Asking for credentials
user_id = input('Enter Facebook User Id: ') 
password = input('Enter your password: ')

print(user_id)
print(password)


# Initializing the Chrome Driver
chrome_driver = 'D:\Bundle Projects\Facebook Bot\chromedriver.exe'

browser = webdriver.Chrome(chrome_driver)
browser.get('https://www.facebook.com/')

user_field = browser.find_element_by_id('email')
user_field.send_keys(user_id)

password_field = browser.find_element_by_id('pass')
password_field.send_keys(password)

login_button = browser.find_element_by_id("u_0_b")
login_button.click()