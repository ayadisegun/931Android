import time

from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from appium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from selenium.webdriver.common.actions.input_device import InputDevice
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.support.wait import WebDriverWait


class ScrollUtil:
    # def setup_function1(self):
    #     global appium_service
    #     appium_service = AppiumService()
    #     appium_service.start()
    #
    #     desired_caps = dict(
    #         deviceName='Rapt',
    #         platformName='Android',
    #         browserName='Chrome',
    #         automationName='UiAutomator2',
    #         chromedriverExecutable='C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',
    #     )
    #
    #     desired_cap = {}
    #     desired_caps['deviceName'] = 'Android'
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['browserName'] = 'Chrome'
    #     desired_caps['automationName'] = 'UiAutomator2'
    #     desired_caps['chromedriverExecutable'] = 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe'
    #     desired_caps['appPackage'] = 'com.androidsample.generalstore'
    #     desired_caps['appActivity'] = 'com.androidsample.generalstore.SplashActivity'
    #     desired_caps['noReset'] = True
    #
    #     # capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    #     capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
    #     global driver
    #     driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    #     driver.implicitly_wait(10)
    #     touch_actions = ActionChains(driver)
    #     global wait
    #     wait = WebDriverWait(driver, 10)

    def setup_function(self):
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

    def teardown(self):
        driver.quit()
        appium_service.stop()



    @staticmethod
    def draganddrop(source, drop):
        ActionChains.drag_and_drop(source, drop).perform()

    @staticmethod
    def longPress(element):
        ActionChains.click_and_hold(element).perform()

    @staticmethod
    def scrollToTextByUIAutomatorclick(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
                            "UiSelector().textContains(\"" + text + "\").instance(0))").click()

    # @staticmethod
    # def scrollToTextByAccessibilityIdclick(text, driver):
    #     driver.find_element(AppiumBy.ACCESSIBILITY_ID,
    #                         "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
    #                         "UiSelector().text(\"" + text + "\").instance(0))").click()

    @staticmethod
    def scrollintoViewText(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"" + text + "\"))")

    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().className("android.widget.ImageView").description("200GB 2-Month Plan ₦50,000.00 valid for 60 Days"))'

    @staticmethod
    def scrollToTextByUIAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
                            "UiSelector().textContains(\"" + text + "\").instance(0))")

    # Scroll into view using JavaScript - for mobile web
    @staticmethod
    def scrollIntoView(element, driver):
        driver.execute_script("arguments[0].scrollIntoView();", element)


    @staticmethod
    def swipe(element, direction, driver):
        driver.execute_script("mobile: swipeGesture", {
            "elementId": element,
            "direction": direction,
            "percent": 0.75
        })


    @staticmethod
    def scrollDown(numberOfswipes, driver):
        for i in range(1, numberOfswipes+1):
            driver.swipe(325, 941, 325, 436, 1000)

    @staticmethod
    def scrollUp(numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(325, 436, 325, 941, 1000)

    @staticmethod
    def swipeRightCordinate(x1, y1, x2, y2, numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(x1, y1, x2, y2, 1000)

    @staticmethod
    def swipeLeftCordinate(x1, y1, x2, y2, numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(x1, y1, x2, y2, 500)


    @staticmethod
    def swipeLeftAirtimeCustomAmount(numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(484, 576, 88, 576, 1000)

    @staticmethod
    def swipeRightAirtimeCustomAmount(numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(88, 576, 484, 576, 1000)

    @staticmethod
    def click_at_coordinates(x, y, driver):
        # Create a touch pointer
        actions = ActionChains(driver)
        pointer_input = PointerInput("touch", "finger")
        actions.w3c_actions = ActionBuilder(driver, mouse=pointer_input)

        # Define touch actions
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pointer_up()

        # Perform the actions
        actions.perform()

    @staticmethod
    def swipeUpawaiting(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 200)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeDownawaitingc(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 500)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 800)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeLefta(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeRighta(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def inputText(text, driver):
        keycodes = {
            # Uppercase and lowercase letters
            'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36,
            'I': 37, 'J': 38, 'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44,
            'Q': 45, 'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50, 'W': 51, 'X': 52,
            'Y': 53, 'Z': 54,
            'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36,
            'i': 37, 'j': 38, 'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44,
            'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50, 'w': 51, 'x': 52,
            'y': 53, 'z': 54,
            # Numbers
            '0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
            # Special characters
            ' ': 62, '!': 8, '#': 18, '$': 19, '%': 20, '^': 21, '&': 22,
            '*': 23, '(': 24, ')': 25, '@': 77, '-': 69, '_': 69, '=': 70, '+': 70, '[': 71,
            '{': 71, ']': 72, '}': 72, "\\": 73, '|': 73, ';': 74, ':': 74, "'": 75,
            '"': 75, ',': 55, '<': 55, '.': 56, '>': 56, '/': 76, '?': 76, '`': 68,
            '~': 68
        }
        for char in text:
            if char in keycodes:
                # Handle Shift key for uppercase letters and symbols
                if char.isupper() or char in {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '{', '}', '|',
                                              ':', '"', '<', '>', '?', '~'}:
                    driver.press_keycode(59, 1)
                    driver.press_keycode(keycodes[char], 1)
                    driver.press_keycode(59, 1)
                elif char.islower():
                    driver.press_keycode(keycodes[char])
                elif char in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                    driver.press_keycode(keycodes[char])
            else:
                raise ValueError(f"Invalid alphabet: {text}. Please provide a valid alphabet or number A-Z, 0-9.")

    @staticmethod
    def back(driver):
        driver.press_keycode(4)

    @staticmethod
    def TearDown(driver):
        driver.close()
        driver.quit()


# Android Keycodes
# 0 - 7
# 1 - 8
# 2 - 9
# 3 - 10
# 4 - 11
# 5 - 12
# 6 - 13
# 7 - 14
# 8 - 15
# 9 -16
# 10 -
# 11 - 227
# 12 - 228
# Shift - 59
# back - 4
# home - 3
# recent app - 187
# driver.launch_app()  # Reopen the app
# driver.background_app(5)  # Minimize the app for 5 seconds
# power key 26
# volume up 24
# volume down 25
#delete - 67

