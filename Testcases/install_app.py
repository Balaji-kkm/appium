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
desired_caps['app'] = str(Path().absolute().parent) + '\\apps\\Apna Mart.apk'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# phone_number = driver.find_element(By.ID, 'com.apnamart.apnaconsumer:id/phoneInputEditText')
# phone_number.click()
# driver.find_element(By.ID, 'com.google.android.gms:id/cancel').click()
#
# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'android.widget.ImageView')))
#
# driver.find_element(By.CLASS_NAME, 'android.widget.ImageView').click()
#
# phone_number.send_keys("9865291104")

time.sleep(2)


# driver.find_element(By.CLASS_NAME, 'android.widget.ImageView').click()
# time.sleep(2)
# for switching apps
# driver.start_activity('com.google.android.apps.messaging', '.launcher.Launcher')


time.sleep(2)
driver.quit()
