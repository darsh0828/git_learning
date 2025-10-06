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


def driver(request):
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




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot only if test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            allure.attach(driver.get_screenshot_as_png(),
                          name=f"Failure_{item.name}",
                          attachment_type=allure.attachment_type.PNG)


