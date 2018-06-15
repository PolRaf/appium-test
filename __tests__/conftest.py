import pytest
import os
from appium import webdriver


@pytest.fixture(scope="function")
def driver():
    #driver = webdriver.Remote(
        #command_executor='http://127.0.0.1:4723/wd/hub',
        #desired_capabilities={
            #'app': '/Users/vood/dev/appium-test/ios/build/Build/Products/Debug-iphonesimulator/myTestProject.app',
            #'platformName': 'iOS',
            #'platformVersion': '11.4',
            #'deviceName': 'iPhone Simulator'
        #})
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': os.path.expanduser(
                '/Users/raffaellapolistena/dev/myTestProject/android/app/build/outputs/apk/app-debug.apk'),
            'platformName': 'Android',
            'deviceName': 'Android Emulator'
        })

    yield driver
   #driver.quit()







# import os
# import time
# from appium import webdriver

# driver = webdriver.Remote(
#     command_executor='http://127.0.0.1:4723/wd/hub',
#     desired_capabilities={
#         "platformName": "iOS",
#         "platformVersion": "11.4",
#         "deviceName": "iPhone Simulator",
#         "app": "/Users/raffaellapolistena/dev/myTestProject/ios/build/Build/Products/Debug-iphonesimulator/myTestProject.app"
#     })

# # wait for app to load
# time.sleep(3)

# # find the link with the text "Click here" and click on it
# # link = driver.find_element_by_xpath('//XCUIElementTypeOther[@name="ciao"]')
# link = driver.find_elements_by_accessibility_id("ciao")
# print(dir(link))
# link.click()

# # wait for the next screen to load
# time.sleep(10)

# # make sure the correct "Success" result is on the page
# driver.find_element_by_xpath('//*[@text="clicked"]')

# # important; you will not be able to launch again if this does not happen
# driver.quit()
