import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.google.android.dialer',
    appActivity='com.android.dialer.main.impl.MainActivity'

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element(By.ID, 'com.google.android.dialer:id/dialpad_fab').click()

driver.find_element(By.ID, 'com.google.android.dialer:id/nine').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/eight').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/six').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/five').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/two').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/nine').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/one').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/one').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/zero').click()
driver.find_element(By.ID, 'com.google.android.dialer:id/four').click()

driver.find_element(By.ID, 'com.google.android.dialer:id/dialpad_voice_call_button').click()

time.sleep(5)
driver.quit()

