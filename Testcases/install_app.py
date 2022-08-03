import time
from pathlib import Path
from telnetlib import EC

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
# desired_caps['appPackage'] = 'com.apnamart.apnaconsumer'
# desired_caps['appActivity'] = '.presentation.activities.dashboard.DashBoardActivity'
desired_caps['app'] = str(Path().absolute().parent) + '\\apps\\Amazon.apk'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# android automator

driver.find_element(By.android_uiautomator)



time.sleep(2)


# for switching apps
# driver.start_activity('com.google.android.apps.messaging', '.launcher.Launcher')


time.sleep(2)
driver.quit()
