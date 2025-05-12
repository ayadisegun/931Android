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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import openpyxl
from Utility import read_excel_data, setCellData_path_in_script, get_Excel_data_path_in_script


@pytest.fixture(scope='module')
def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = {
        'deviceName': 'Android',
        'platformName': 'Android',
        # 'browserName': 'Chrome',
        'automationName': 'UiAutomator2',
        'chromedriverExecutable': 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',
        # 'chromedriverExecutable': get_chromedriver_path(),  # Use a function for portability
        'appPackage': 'com.switchto931.mobile',
        'appActivity': '.MainActivity',
        'noReset': True
    }
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
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


def get_chromedriver_path():
    """Return the chromedriver path based on environment or configuration."""
    # Example: Use environment variable or config file for portability
    return os.getenv('CHROMEDRIVER_PATH', 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe')


@pytest.fixture(params=["device1", "device2"], scope="module")
def setup_function_parallel(request):
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    global driver
    if request.param == "device1":
        desired_caps = {
            'deviceName': 'Android',
            'platformName': 'Android',
            'udid': '076452521J102102',
            'browserName': 'Chrome',
            'automationName': 'UiAutomator2',
            # 'chromedriverExecutable': 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',
            'chromedriverExecutable': get_chromedriver_path(),  # Use a function for portability
            # 'appPackage': 'com.switchto931.mobile',
            # 'appActivity': '.MainActivity',
            'noReset': True, }
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    if request.param == "device2":
        desired_caps = {
                'deviceName': 'Android',
                'platformName': 'Android',
                'udid': 'emulator-5554',
                'browserName': 'Chrome',
                'automationName': 'UiAutomator2',
                # 'chromedriverExecutable': 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',
                'chromedriverExecutable': get_chromedriver_path(),  # Use a function for portability
                # 'appPackage': 'com.switchto931.mobile',
                # 'appActivity': '.MainActivity',
                'noReset': True, }
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4724', options=capabilities_options)
    driver.implicitly_wait(10)
    touch_actions = ActionChains(driver)
    global wait
    wait = WebDriverWait(driver, 10)
    yield driver
    driver.press_keycode(3)
    driver.quit()
    appium_service.stop()


# DEVICE_CONFIGS = {
#     "device1": {
#         "udid": "076452521J102102",
#         "port": 4723,
#         "deviceName": "Android",
#     },
#     "device2": {
#         "udid": "074972524K000075",
#         "port": 4724,
#         "deviceName": "Android",
#     }
# }


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
    # log failure for allure reporting
    yield
    item = request.node
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name="Failure_Screenshot",
            attachment_type=allure.attachment_type.PNG
        )


def readconfig(section, key):
    # script for reading data from config.ini for test data
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section, key)


def send_mail(sender_address, sender_pass, receiver_address, subject, mail_content, attach_file_name,
              ):
    # sender_pass = 'Selenium@234'

    # setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def pytest_addoption(parser):
    parser.addoption(
        "--excel-file",
        action="store",
        default="C:\\Users\\Segun\\PycharmProjects\\Android931\\testScripts\\ExcelFile.xlsx",
        help="Path to the Excel file"
    )
    parser.addoption(
        "--sheet-name",
        action="store",
        default="details",
        help="Name of the sheet to read"
    )


def pytest_generate_tests(metafunc):
    import pytest

    global excel_file
    global sheet_name
    excel_file = metafunc.config.getoption("excel_file")
    sheet_name = metafunc.config.getoption("sheet_name")

    if excel_file and sheet_name:
        headers, data_rows = read_excel_data(excel_file, sheet_name)

        # Get all function parameters
        func_params = metafunc.function.__code__.co_varnames[:metafunc.function.__code__.co_argcount]

        # Detect only real fixtures (not just argument names)
        actual_fixtures = {
            name for name in func_params
            if name in metafunc._arg2fixturedefs
        }

        # print(f"Function parameters: {func_params}")
        # print(f"Actual fixtures: {actual_fixtures}")
        # print(f"Excel headers: {headers}")

        # Excel-driven parameters are those not in actual fixtures
        excel_params = [param for param in func_params if param not in actual_fixtures]
        print(f"Excel-driven parameters: {excel_params}")

        # Find missing test params in Excel headers
        missing_params = [param for param in excel_params if param not in headers]
        if missing_params:
            pytest.fail(f"The following test parameters are missing in the Excel header row: {missing_params}")

        # Use only matching headers in correct order
        matched_headers = [h for h in headers if h in excel_params]
        print(f"Matched headers: {matched_headers}")
        matched_headers = [h for h in headers if h in excel_params]
        print(f"Matched headers: {matched_headers}")
        if not matched_headers:
            # No parameters to parametrize for this test function
            return  # Safe to skip without failing

        # Prepare data
        filtered_data = [
            tuple(row[headers.index(h)] for h in matched_headers)
            for row in data_rows
        ]

        metafunc.parametrize(matched_headers, filtered_data, indirect=False)


# def pytest_generate_tests(metafunc):
#     # read_excel data function
#     global excel_file
#     global sheet_name
#     excel_file = metafunc.config.getoption("excel_file")
#     sheet_name = metafunc.config.getoption("sheet_name")
#
#     if excel_file and sheet_name:
#         headers, data_rows = read_excel_data(excel_file, sheet_name)
#
#         # Define known fixture parameters to exclude
#         known_fixtures = {
#             'request', 'setup_function', 'setup_function_parallel', 'log', 'log_failure'
#         }
#
#         # Get only the actual function parameters (not local variables)
#         func_params = metafunc.function.__code__.co_varnames[:metafunc.function.__code__.co_argcount]
#
#         # Filter out known fixtures to get Excel-driven parameters
#         excel_params = [param for param in func_params if param not in known_fixtures]
#
#         # Find missing test params in Excel headers
#         missing_params = [param for param in excel_params if param not in headers]
#         if missing_params:
#             pytest.fail(f"The following test parameters are missing in the Excel header row: {missing_params}")
#
#         # Use only matching headers in correct order
#         matched_headers = [h for h in headers if h in excel_params]
#         filtered_data = [
#             tuple(row[headers.index(h)] for h in matched_headers)
#             for row in data_rows
#         ]
#
#         metafunc.parametrize(tuple(matched_headers), filtered_data)

# @pytest.fixture(params=["device1", "device2"], scope="module")
# def setup_function_parallel(request):
#     device = request.param
#     config = DEVICE_CONFIGS[device]
#
#     # Start Appium service for the specific device
#     appium_service = AppiumService()
#     appium_service.start(
#         args=['--address', '127.0.0.1', '--port', str(config['port']), '--base-path', '/']
#     )
#
#     # Common desired capabilities
#     desired_caps = {
#         'deviceName': config['deviceName'],
#         'platformName': 'Android',
#         'udid': config['udid'],
#         'automationName': 'UiAutomator2',
#         'chromedriverExecutable': get_chromedriver_path(),
#         'appPackage': 'com.switchto931.mobile',
#         'appActivity': '.MainActivity',
#         'noReset': True,
#     }
#
#     # Load capabilities and initialize driver
#     capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
#     global driver
#     driver = webdriver.Remote(f'http://127.0.0.1:{config["port"]}', options=capabilities_options)
#     driver.implicitly_wait(10)
#     touch_actions = ActionChains(driver)
#     global wait
#     wait = WebDriverWait(driver, 10)
#     yield driver
#     driver.press_keycode(3)
#     driver.quit()
#     appium_service.stop()


def setCellData(rowNum, colNum, data):
    excelfile = excel_file
    sheetName = sheet_name
    workbook = openpyxl.load_workbook(excelfile)
    sheet = workbook[sheetName]
    sheet.cell(row=rowNum, column=colNum).value=data
    workbook.save(excelfile)


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


# # script successfully generating html error screenshot but not attaching to the report, debug later
# html report hookwrapper
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

