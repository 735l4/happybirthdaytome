from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



PATH = "/home/tesla//Desktop/projects/python/chromedriver"
driver = webdriver.Chrome(PATH)


driver.get("https://m.facebook.com")
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
email.send_keys("tero email ya hal muji")
password.send_keys("password ya hal")
password.send_keys(Keys.RETURN)

time.sleep(4)

driver.find_element_by_partial_link_text("Not Now").click()

driver.get("tero post link ya hal")
time.sleep(4)
reply = driver.find_elements_by_partial_link_text("Reply")
for x in range(0,len(reply)):
    if reply[x].is_displayed():
        reply[x].click()
time.sleep(3)
cmt = driver.find_elements_by_class_name("_1mf")
for rply in range(0, len(cmt)):
    cmt[rply].send_keys("Thank you")
# driver.quit()