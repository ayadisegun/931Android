import logging
import time
from _ast import Assert

import os

import allure
import bs4.builder
import pytest
from appium.common import helper
from appium.webdriver import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import webdriver
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import KeyInput
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.support import expected_conditions as EC
from Scroll_utils import ScrollUtil
from configparser import ConfigParser


@pytest.fixture(scope='module')
def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = dict(
        deviceName='Rapt',
        platformName='Android',
        browserName='Chrome',
        automationName='UiAutomator2',
        chromedriverExecutable='C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',
    )

    desired_cap = {}
    desired_caps['deviceName'] = 'Android'
    desired_caps['platformName'] = 'Android'
    desired_caps['browserName'] = 'Chrome'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['chromedriverExecutable'] = 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe'
    desired_caps['appPackage'] = 'com.switchto931.mobile'
    desired_caps['appActivity'] = '.MainActivity'
    desired_caps['noReset'] = True

    # capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    driver.implicitly_wait(10)
    touch_actions = ActionChains(driver)
    global wait
    wait = WebDriverWait(driver, 10)
    yield driver
    driver.press_keycode(3)
    driver.quit()
    appium_service.stop()

@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.mark.usefixtures
@pytest.fixture
def log_failure(request, setup_function):
    yield
    item = request.node
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name="Failure_Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

@pytest.fixture
def log():
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)  # Create logs directory if it doesn't exist
    log_file = os.path.join(log_dir, "logfile.log")
    logging.basicConfig(filename=log_file,
                        filemode='a',  # 'a' means append to the file, use 'w' to overwrite
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level='logging.INFO')  # Use logging.DEBUG for more detailed logs)
    loggers = logging.getLogger()
    return loggers


# config = ConfigParser()
# config.read("config.ini") #filename where config is declared
# print(config.get("locatorLogin", "username"))
def readconfig(section, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section, key)












#html report hookwrapper
# @pytest.mark.hookwrapper
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when in ('call', 'setup'):
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.join(os.path.dirname(__file__), 'report')
#             os.makedirs(reports_dir, exist_ok=True)  # Create directory if it doesn't exist
#             file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_").replace("/", "_") + ".png")
#             print("file_name is " + file_name)
#             if _capture_screenshot(file_name):
#                 # Use relative path for HTML report to ensure browser can load the image
#                 relative_file_name = os.path.relpath(file_name, os.path.dirname(item.config.option.htmlpath))
#                 html = f'<div><img src="{relative_file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
#                        f'onclick="window.open(this.src)" align="right"/></div>'
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(file_name):
#     driver.get_screenshot_as_file(file_name)



