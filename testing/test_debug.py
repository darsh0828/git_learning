import os

import allure
import pytest
import appium
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time
import base64
import allure
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.goibibo',
    appActivity='com.goibibo.common.HomeActivity',
    noReset=True,
    fullReset=False

)

capabilities_option = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_option)
time.sleep(2)


def test_search():
    driver.find_element(By.ID, 'com.goibibo:id/icon').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="hotel_landing_searched_text"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="edtSearch"]').send_keys("delhi")
    time.sleep(2)
    driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.Button').click()
    time.sleep(2)


def test_flight_search():
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                        value="new UiSelector().resourceId(\"com.goibibo:id/icon\").instance(1)").click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"ROUNDTRIP\")").click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                        value="new UiSelector().className(\"android.widget.RelativeLayout\").instance(4)").click()
    time.sleep(2)
    driver.find_element(By.ID, "com.goibibo:id/arrival_city_input").send_keys("chennai")
    time.sleep(2)
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Chennai\")").click()
    time.sleep(2)
    driver.find_element(By.ID, "com.goibibo:id/search_button_flat").click()
    time.sleep(2)
