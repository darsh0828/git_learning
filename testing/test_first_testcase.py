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
    driver.start_recording_screen()
    driver.find_element(By.ID, 'com.goibibo:id/icon').click()
    time.sleep(2)
    driver.find_element(By.ID, 'com.goibibo:id/txtPlaceName').click()
    time.sleep(2)
    video_rawdata = driver.stop_recording_screen()
    #video_path = "/videos"

    os.makedirs("videos", exist_ok=True)
    video_path = os.path.join("videos", "test_video.mp4")

    with open(video_path, "wb") as f:
        f.write(base64.b64decode(video_rawdata))

    #allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type="attachmentType.PNG")
    allure.attach.file(video_path, name="Test Execution Video", attachment_type="allure.attachment_type.MP4")
    assert False, "Intentional failure to test screenshot + video"