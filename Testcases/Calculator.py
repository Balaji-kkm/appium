import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

desired_caps = {}
desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['appPackage'] = 'com.miui.calculator'
desired_caps['appActivity'] = '.cal.CalculatorActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

el1 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout")
el2.click()

el1 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_7_s")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_8_s")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="minus")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_1_s")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_5_s")
el6.click()
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
el7.click()
el8 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_1_s")
el8.click()
el9 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_0_s")
el9.click()
el9.click()
el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="multiply")
el10.click()
el11 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_6_s")
el11.click()
el11.click()

time.sleep(5)
driver.quit()