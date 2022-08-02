import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)


# appium_service = AppiumService()
# appium_service.start()

driver = webdriver.Remote('http://127.0.0.1:5000/wd/hub', desired_caps)

driver.get("https://www.wikipedia.org/")
print(driver.title)

select_element = driver.find_element(By.CSS_SELECTOR, 'select')
select_object = Select(select_element)


select_object.select_by_value("es")


options = driver.find_elements(By.TAG_NAME, 'option')

for option in options:
    print("Text is :", option.text, "Lang is:", option.get_attribute('Lang'))

print(len(options))


time.sleep(5)
driver.quit()
# appium_service.stop()
