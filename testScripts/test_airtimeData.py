import time
from _ast import Assert

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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import KeyInput
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.support import expected_conditions as EC
from Scroll_utils import ScrollUtil
# from testScripts.conftest import setup_function


@pytest.mark.usefixtures
def airtime(setup_function):
    global driver
    driver = setup_function
    # mtn airtime
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Airtime").click()
    topupLabel = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Mobile Top Up").get_attribute("content-desc")
    Assert(topupLabel == "Mobile Top Up"), "label is not 'Mobile Top Up'."
    driver.find_element(By.XPATH, "//android.widget.ImageView[@index='0']").click()
    mtnLabel = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "MTN AIRTIME").get_attribute("content-desc")
    Assert(mtnLabel == "MTN AIRTIME")
    phnbox = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter Your Phone Number']")
    phnbox.click()
    phnbox.send_keys("08164627646")
    amountbox = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter amount between ₦50 and ₦20000']")
    amountbox.click()
    amountbox.send_keys("100")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "₦500.00").click()
    amountFilled = driver.find_element(By.XPATH, "//android.widget.EditText[@index='4']").text
    Assert(amountFilled=="500")
    # scrollToEndAction()
    ScrollUtil.scrollDown(2, driver)
    driver.press_keycode(4)      # Key(new KeyEvent(AndroidKey.BACK))
    driver.find_element(By.XPATH, "//android.widget.Button[@index='6']").click()
    pinbox = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
    pinbox.click()
    # clickAtCoordinates(driver, 164, 1328)
    pinbox.send_keys("1234")
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.find_element(By.XPATH, "//android.widget.Button[@index='0']").click()


    # airtel airtime
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Airtime").click()
    topupLabelairteltest = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Mobile Top Up").get_attribute("content-desc")
    Assert(topupLabelairteltest=="Mobile Top Up")
    driver.find_element(By.XPATH, "//android.widget.ImageView[@index='1']").click()
    airtelLabel = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "AIRTEL AIRTIME").get_attribute("content-desc")
    Assert(airtelLabel=="AIRTEL AIRTIME")
    phnboxairtel = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter Your Phone Number']")
    phnboxairtel.click()
    phnboxairtel.send_keys("09041694018")
    amountboxairtel = driver.find_element(By.XPATH, "//android.widget.EditText[@hint='Enter amount between ₦50 and ₦20000']")
    amountboxairtel.click()
    amountboxairtel.send_keys("100")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "₦5,000.00").click()
    driver.press_keycode(4)
    changeamount = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "₦2,000.00")
    changeamount.click()
    # swipeAction(changeamount, "left")
    ScrollUtil.swipeLeftAirtimeCustomAmount(1, driver)
    # scrollToEndAction()
    ScrollUtil.scrollDown(2, driver)
    driver.find_element(By.XPATH, "//android.widget.Button[@index='6']").click()
    pinboxairr = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
    pinboxairr.click()
    pinboxair = ScrollUtil.click_at_coordinates(164, 1343, driver)
    driver.press_keycode(8)
    driver.press_keycode(8)
    driver.press_keycode(8)
    driver.press_keycode(8)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Pay").click()
    errortxt = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Incorrect pin. Please try again.").get_attribute("content-desc")
    Assert(errortxt == "Incorrect pin. Please try again."), "error message not accurate"
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK").click()
    driver.press_keycode(4)
    driver.press_keycode(4)
    print("finished Airtime test")

    print("Started Data vending")
    # mtn Data
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Data").click()
    # datalabel = driver.find_element(By.XPATH, "//android.view.View[@content-desc='Data Purchase']").get_attribute("content-desc")
    # assert datalabel == "Data Purchase"
    # driver.find_element(By.XPATH, "//android.widget.ImageView[@index='0']").click()
    # time.sleep(1)
    # tab3 = driver.find_element(By.XPATH, "//android.view.View[@index='2']")
    # tab3.click()
    # assert((driver.find_element(By.XPATH, "//android.view.View[@index='0']").get_attribute("focusable")) == "false")
    # tablabel = driver.find_element(By.XPATH, "//android.view.View[@index='2']").get_attribute("content-desc")
    # print(tablabel)
    # time.sleep(2)
    # monthlyTab = driver.find_element(By.XPATH, "//android.view.View[@index=2]")
    # monthlyTab.click()
    # ScrollUtil.swipe(monthlyTab, "left", driver)
    # tabsocial = driver.find_element(By.XPATH, "//android.view.View[@index=3]")
    # tabsocial.click()
    # twomnth = driver.find_element(By.XPATH, "//android.view.View[@index=2]")
    # twomnth.click()


    # ScrollUtil.swipeRightCordinate(60, 959, 646, 959, 1, driver)
    # # ScrollUtil.scrollintoViewText("200GB", driver)  #works for scrolling remain location
    # driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, '150MB Facebook')]").click()
    #
    # # ScrollUtil.scrollUp(3, driver)
    #
    # # prods = driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView")
    # # prodslen = len(prods)
    # # for i in range(prodslen):
    # #     product_name = prods[i].get_attribute("content-desc")
    # #     if product_name == "200GB 2-Month Plan ₦50,000.00 valid for 60 Days":
    # #         prodclick = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, '200GB 2-Month Plan')]")
    # #         prodclick.click()
    # #     break
    #
    # # plan = driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='200GB 2-Month Plan ₦50,000.00 valid for 60 Days']").click()
    # # plan = driver.find_element(By.XPATH, "//android.widget.ImageView[@index='6']")
    # # scrollTohere((driver.find_element(By.XPATH, "//android.widget.ImageView[@index='3']")), "down")
    # # nextplan1 = driver.find_element(By.XPATH, "//android.widget.ImageView[@index='3']")
    # # nextplan1.click()
    # amountcheck = driver.find_element(By.XPATH, "//android.view.View[contains(@content-desc, '₦')]").get_attribute("content-desc")
    # assert amountcheck == "₦150.00", "amount returned is not accurate"
    # driver.find_element(By.XPATH, "//android.widget.Button[@index='5']").click()
    # print("here")
    # driver.find_element(By.XPATH, "//android.widget.Button[contains(@content-desc, 'Buy for Others')]").click()
    # print("1")

    textbox = driver.find_element(By.XPATH, "//android.widget.EditText[contains(@hint, 'Enter Phone Number')]")
    textbox.click()
    textbox.send_keys("111")
    ScrollUtil.back(driver)
    tabs1 = driver.find_element(By.XPATH, "//android.view.View[contains(@content-desc, 'Phone Number')]")
    tabs1.click()
    # swipeAction(tabs1, "left")
    tabs2 = driver.find_element(By.XPATH, "//android.view.View[@index='1' or contains(@content-desc, 'Beneficiaries Tab')]")
    tabs2.click()
    tabAttribute = tabs1.get_attribute("selected")
    assert tabAttribute == "false", "wrong tab still selected"
    benesearch = driver.find_element(By.XPATH, "//android.widget.EditText")
    benesearch.click()
    benesearch.send_keys("111")
    ScrollUtil.swipe((driver.find_element(By.XPATH, "//android.view.View[@index='1' or contains(@content-desc, 'Beneficiaries Tab')]")), "right", driver)
    tabs1 = driver.find_element(By.XPATH, "//android.view.View[contains(@content-desc, 'Phone Number')]")
    tabs1.click()
    # contactIcon = driver.find_element(By.XPATH, "//android.view.View[@index='0']")
    # contactIcon.click()
    # dismissPermission = driver.find_element(By.XPATH, "//android.widget.Button[contains(@content-desc, 'No thanks']")
    # dismissPermission.click()
    textbox1 = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
    textbox1.click(), textbox1.clear()
    textbox1.send_keys("111")
    ScrollUtil.back(driver)
    # driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='OK']").click()  # dismiss permission not granted notification
    # driver.press_keycode(4)  # driver.pressKey(new KeyEvent(AndroidKey.BACK))
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Buy for others']").click()
    pinboxmtnData = ScrollUtil.click_at_coordinates(164, 1343, driver)
    driver.press_keycode(8)
    driver.press_keycode(8)
    driver.press_keycode(8)
    driver.press_keycode(8)
    ScrollUtil.back(driver)
    ScrollUtil.back(driver)
    ScrollUtil.back(driver)
    driver.quit()
    # driver.press_keycode(4)
    # driver.press_keycode(4)
    # driver.press_keycode(4)


    # Glo Data
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Data").click()
    datalabel = driver.find_element(By.XPATH, "//android.view.View[@content-desc='Data Purchase']").get_attribute("content-desc")
    assert datalabel=="Data Purchase"
    driver.find_element(By.XPATH, "//android.widget.ImageView[@index='2']").click()
    time.sleep(3)
    tab3 = driver.find_element(By.XPATH, "//android.view.View[@index='2']")
    tab3.click()
    assert (driver.find_element(By.XPATH, "//android.view.View[@index='0']")).get_attribute("focusable") == "false"
    tablabel = driver.find_element(By.XPATH, "//android.view.View[@index='2']").get_attribute("content-desc")
    print(tablabel)
    tab2month = driver.find_element(By.XPATH, "//android.view.View[@index='2']")
    tab2month.click()
    nextplan1 = driver.find_element(By.XPATH, "//android.widget.ImageView[@index='4']")
    nextplan1.click()
    amountcheck = driver.find_element(By.XPATH, "//android.view.View[@index='7']").get_attribute("content-desc")
    assert amountcheck == "₦100,000.00"
    driver.find_element(By.XPATH, "//android.widget.Button[@index='5']").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Buy for Others").click()
    textbox = driver.find_element(By.CLASS_NAME, "android.widget.EditText")
    textbox.click()
    textbox.send_keys("08164627646")
    driver.press_keycode(4)
    tabs1 = driver.find_element(By.XPATH, "//android.view.View[@index='0']")
    tabs1.click()
    tabs2.click()
    assert tabs1.get_attribute("selected") == "false"
    benesearch = driver.find_element(By.XPATH, "//android.widget.EditText[@index='0']")
    benesearch.click()
    benesearch.send_keys("08164627646")
    time.sleep(1)
    benesearch.clear()
    time.sleep(1)
    driver.press_keycode(4)
    savedBene = driver.find_element(By.XPATH, "//android.view.View[@index='0']")
    assert savedBene.get_attribute("content-desc") == "MY my glodata 07052038428"
    savedBene.click()
    tabs3 = driver.find_element(By.CLASS_NAME, "android.view.View")
    tabs3.click()
    # textbox1 = driver.find_element(By.CLASS_NAME("android.widget.EditText"))
    # textbox1.click()
    # textbox1.clear()
    # textbox1.send_keys("081646276467")
    # driver.press_keycode(4)
    # driver.find_element(By.XPATH("//android.widget.Button[@index='2']")).click()
    driver.find_element(By.XPATH, "//android.widget.Button[@index='9']").click()
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.find_element(By.XPATH, "//android.widget.Button[@index='0']").click()

    #teardown
    ScrollUtil.TearDown(driver)

