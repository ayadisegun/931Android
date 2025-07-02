import time
from _ast import Assert

import allure
import bs4.builder
import openpyxl
import pytest
import requests
from appium.common import helper
from appium.webdriver import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import webdriver
from appium.options.android import UiAutomator2Options
from appium import webdriver
from pytest_assume.plugin import assume
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import KeyInput
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.support import expected_conditions as EC, wait
from Scroll_utils import ScrollUtil
from conftest import readconfig, setCellData
from conftest import log
from typing import List, Tuple, Any
from Utility import setCellData_path_in_script, get_Excel_data_path_in_script


@pytest.mark.starters
# @pytest.mark.usefixtures("log", "log_failure")
# @pytest.mark.parametrize("FName, LName, UName, Eml, PWord, Email, Pd", get_Excel_data_path_in_script())
def test_chrome(setup_function_parallel):
    global driver
    global wait
    driver = setup_function_parallel
    driver.get("http://google.com")
    driver.find_element(By.XPATH, readconfig("locatorChrome", "searchbox")).send_keys("facebook.com")
    driver.press_keycode(66)
    time.sleep(5)


@pytest.mark.starters
# @pytest.mark.usefixtures("log", "log_failure")
# @pytest.mark.parametrize("FName, LName, UName, Eml, PWord, Email, Pd", get_Excel_data_path_in_script())
def test_logosCheck(setup_function_parallel, log, log_failure, FName, LName, UName, Eml, PWord, Email, Pd):
    global driver
    global wait
    driver = setup_function_parallel
    # driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Login']").click()
    loginIcons = driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView")
    pytest.assume(loginIcons[0].get_attribute("displayed") == "true"), "931 logo is not displayed"
    pytest.assume(loginIcons[1].get_attribute("displayed") == "true"), "Instagram logo is not displayed"
    pytest.assume(loginIcons[2].is_displayed), "FB logo is not displayed"
    pytest.assume(loginIcons[3].is_displayed), "X logo is not displayed"
    pytest.assume(driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").is_displayed), "poweredBy is not displayed"
    appVersion = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").get_attribute("content-desc")
    print("931 application version is: " + appVersion)
    setCellData(1,8,"consoles")
    setCellData(2, 8, appVersion)
    # emailfield = wait.until(EC.presence_of_element_located((By.XPATH, readconfig("locatorLogin", "login_emailbox"))))
    emailfield = driver.find_element(By.XPATH, readconfig("locatorLogin", "login_emailbox"))
    # pwdfield = wait.until(EC.presence_of_element_located((By.XPATH, readconfig("locatorLogin", "login_passbox"))))
    pwdfield = driver.find_element(By.XPATH, readconfig("locatorLogin", "login_passbox"))
    cont_button = driver.find_element(By.XPATH, readconfig("locatorLogin", "continue"))
    # driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter Password']")
    emailfield.click(),emailfield.clear(), emailfield.send_keys(Eml)
    pwdfield.click(), pwdfield.clear(), pwdfield.send_keys(Pd)
    cont_button.click()
    invalidbutton = driver.find_element(By.XPATH, readconfig("locatorLogin", "invalid_credentials"))
    invalidcred_error = invalidbutton.get_attribute("hint")
    setCellData(1, 9, "Errors")
    setCellData(2, 9, "invalid Credentials")
    invalidbutton.click()
    log.error("log message")


# @pytest.mark.starters
# @pytest.mark.usefixtures("log", "log_failure")
# @pytest.mark.parametrize("FName, LName, UName, Eml, PWord, Email, Pd", get_Excel_data_path_in_script())
def test_signUp(setup_function, log, log_failure, FName, LName, UName, Eml, PWord, Email, Pd):
    # sign up
    # driver = setup_function
    driver.find_element(By.XPATH, "//android.view.View[@content-desc='Don’t have an account?  Sign Up']").click()
    # fields = driver.find_elements(By.XPATH, "//android.widget.EditText")
    # FNfield = fields[0]
    FNfield = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter your First Name']")
    LNfield = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter your Last Name']")
    UN = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Username']")
    Email = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter your Email Address']")
    Phn = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter your Phone Number']")
    Pwd = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter your Password']")
    CnfEmail = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Confirm your Password']")
    ScrollUtil.scrollDown(2, driver)
    referal = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter Referral Code']")
    pytest.assume(referal.get_attribute("enabled") == "true"), "referal txtbox not clickable"
    driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Terms of Service']").click()
    driver.press_keycode(4)
    driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='privacy policy.']").click()
    driver.press_keycode(4)
    driver.find_element(By.XPATH, "//android.widget.CheckBox").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//android.widget.CheckBox").click()
    driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Continue']").click()
    ScrollUtil.scrollUp(2, driver)
    fNError = driver.find_element(By.XPATH, "//android.view.View[@content-desc='First Name cannot be empty']").text
    # lNError = driver.find_element(By.XPATH, "//android.view.View[@content-desc='Last Name cannot be empty']").get_attribute("content-desc")
    print(fNError)
    # print(lNError)
    FNfield.click(), FNfield.send_keys(FName)
    LNfield.click(), LNfield.send_keys(LName)
    UN.click(), UN.send_keys(UName)
    Email.click(), Email.send_keys(Eml)
    driver.press_keycode(4)
    ScrollUtil.scrollUp(1, driver)
    Pwd.click(), Pwd.send_keys(PWord)
    CnfEmail.click(), CnfEmail.send_keys(PWord)
    driver.press_keycode(4)
    ScrollUtil.scrollDown(2, driver)
    driver.find_element(By.XPATH, "//android.view.View[@content-desc='Already have an account ? Login']").click()
    time.sleep(1)
    # allure.attach(driver.get_screenshot_as_png(), name="Landing page", attachment_type="PNG")


def test_login_page_checkbox(setup_function, log_failure):
    # global driver
    # driver = setup_function
    # Login
    pytest.assume((driver.find_element(By.XPATH, "//android.view.View[@content-desc='Remember me']")).get_attribute("content-desc") == "Remember me")
    pytest.assume((driver.find_element(By.XPATH, "//android.widget.CheckBox")).get_attribute("enabled") == "true"), "remember me checkbox is not checkable"
    driver.find_element(By.XPATH, "//android.widget.CheckBox").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//android.widget.CheckBox").click()


@pytest.mark.usefixtures
# @pytest.mark.parametrize("FName, LName,UName, Eml, PWord, Email, Pd", get_data())
def test_forgot_password(setup_function,log_failure, FName, LName, UName, Eml, PWord, Email, Pd):
    # forgot password
    # driver = setup_function
    assert (driver.find_element(By.XPATH, "//android.view.View[@content-desc='Forgot Password']")).is_enabled(), "F-pswd not displayed"
    driver.find_element(By.XPATH, "//android.view.View[@content-desc='Forgot Password']").click()
    em = ScrollUtil.click_at_coordinates(120, 1352, driver)
    time.sleep(3)
    # em.send_keys("aya02@gmailcom")
    ScrollUtil.inputText(Eml, driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Continue']").click()
    assert(driver.find_element(By.XPATH, "//android.view.View[@content-desc='Enter a valid email Address']")).is_displayed(), "Enter a valid email Address Error expected"
    driver.press_keycode(4)
    driver.press_keycode(4)
    #eye_button
    pytest.assume((driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[2]/android.view.View")).get_attribute(
        "enabled") == "true"), "eye button is not enabled"
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[2]/android.view.View").click()


@pytest.mark.usefixtures
# @pytest.mark.parametrize("FName, LName, UName, Eml, PWord, Email, Pd", get_data())
def test_login(setup_function, log_failure,FName, LName, UName, Eml, PWord, Email, Pd):
    # global driver
    # driver = setup_function
    emailfield = driver.find_element(By.XPATH, "//android.widget.EditText")
    emailfield.click()
    emailfield.clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "//android.view.View[@content-desc='Continue']").click()
    assert (driver.find_element(By.XPATH, "//android.view.View[@content-desc='Email address/Phone Number cannot be empty']")).get_attribute("displayed") == "true", "empty email/phone number error not returned"
    # pytest.assume((driver.find_element(By.XPATH, "//android.view.View[@content-desc='Password cannot be empty']")).get_attribute("enabled") == "true"), "empty password error not returned"
    emailfield.click()
    emailfield.send_keys(Email)
    pwdfield = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter Password']")
    pwdfield.click()
    pwdfield.send_keys(Pd)
    driver.find_element(By.XPATH, "//android.view.View[@content-desc='Continue']").click()
    pytest.assume(driver.find_element(By.XPATH, "//android.view.View[@content-desc = 'Invalid Credentials']").get_attribute("displayed") == "true", "invalid credential expected")
    # assert(driver.find_element(By.XPATH, "//android.view.View[@content-desc = 'Invalid Credentials']").is_displayed())
    # driver.find_element(By.XPATH, "//android.view.View[@content-desc='Continue']").click()
    allure.attach(driver.get_screenshot_as_png(), name="Landing page", attachment_type="PNG")
    time.sleep(2)

