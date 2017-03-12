__author__ = 'Dmitriy Luzanovsky'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from time import sleep
import logging

license = open("license.txt", "r")
read_license = license.read()
print(read_license)
license.close()
print("Starting program ............")
sleep(3)
print("OK")
sleep(1)
chrome_Options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_Options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_Options)

driver.get("https://facebook.com")
sleep(2)
email = input("Введите свой email ... ")
driver.find_element_by_id("email").send_keys(email)
print("Введен email ... ")
sleep(1)
pwd = driver.find_element_by_id("pass")
enter_pwd = input("А теперь пароль ... ")
pwd.send_keys(enter_pwd)
print("Пароль принят ... ")
pwd.send_keys(Keys.ENTER)
sleep(2)
print("Логин успешен!")




def posting():
    filename = input("Укажите имя файла базы груп и сообществ...  ")
    filename = 'settings/'+filename+'.txt'
    a = 0
    fb_base = open(filename, 'r')
    while 1:
        blog_url = fb_base.readline()
        if not blog_url: break
        print("Blog url: " + blog_url)
        driver.get(blog_url)
        sleep(5)
        e = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        act = ActionChains(driver)
        act.move_to_element(e).perform()
        act = ActionChains(driver)
        act.click(e).perform()
        sleep(3)
        post = open("settings/post.txt", "r")
        post_text = post.read()
        print("Загрузка поста... ")
        sleep(1)
        act = ActionChains(driver)
        act.send_keys(post_text).perform()
        sleep(1)
        post.close()

        e = driver.find_element_by_xpath("//button[@type='submit'][@value='1']/span")
        act = ActionChains(driver)
        act.move_to_element(e).perform()
        sleep(1)
        act = ActionChains(driver)
        act.click(e).perform()
        print("Sucessfull!")
        sleep(3)
    fb_base.close()
posting()