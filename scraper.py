from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email_input = input("Enter your email: ")
password_input = input("Enter your password: ")
post_url = input("Enter your post url: ")


PATH = "/home/tesla//Desktop/projects/python/chromedriver"
driver = webdriver.Chrome(PATH)


driver.get("https://m.facebook.com")
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
email.send_keys(email_input)
password.send_keys(password_input)
password.send_keys(Keys.RETURN)

time.sleep(4)

driver.find_element_by_partial_link_text("Not Now").click()

driver.get(post_url)
time.sleep(4)
reply = driver.find_elements_by_partial_link_text("Reply")
for x in range(0,len(reply)):
    if reply[x].is_displayed():
        reply[x].click()
time.sleep(3)
cmt = driver.find_elements_by_class_name("_1mf")
for rply in range(0, len(cmt)):
    cmt[rply].send_keys("Thank you")
    cmt[rply].send_keys(Keys.RETURN)
# driver.quit()