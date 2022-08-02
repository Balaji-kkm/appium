import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.google.android.contacts',
    appActivity='com.google.android.apps.contacts.activities.PeopleActivity'

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.find_element(By.ID, 'com.google.android.contacts:id/floating_action_button').click()

driver.find_element(By.XPATH, "//*[contains(@text, 'First name')]").send_keys("Test")
driver.find_element(By.XPATH, "//*[contains(@text, 'Phone')]").send_keys("9865291103")
driver.find_element(By.XPATH, "//*[contains(@text, 'Email')]").send_keys("test@gmail.com")

driver.hide_keyboard()

driver.find_element(By.ID, 'com.google.android.contacts:id/toolbar_button').click()


time.sleep(5)
driver.quit()

