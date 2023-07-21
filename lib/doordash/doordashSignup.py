import asyncio
import os
import pickle

import aiohttp
import random

from logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from httpClient import HttpClient
from util.utility import fetch_otp_details, verify_phone

logger = Logger.get_instance()


def save_cookie(browser, filename):
    cookies = browser.get_cookies()
    os.makedirs(os.path.dirname(f'cookies/{filename}-cookies.pkl'),
                exist_ok=True)  # Create directory if not present
    with open(f'cookies/{filename}-cookies.pkl', 'wb') as file:
        pickle.dump(cookies, file)


def load_cookie(browser, filename):
    try:
        with open(f'cookies/{filename}-cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            # Add the cookies to the WebDriver
            for cookie in cookies:
                browser.add_cookie(cookie)
    except FileNotFoundError:
        logger.info("Cookie not found")
    except IOError:
        logger.info("An error occurred while reading cookies file")
    except Exception as e:
        logger.info("An unexpected error occurred:" + str(e))


async def add_account_data_to_profile(profile_id, user):
    await asyncio.sleep(4)
    url = "http://localhost:3001"
    account_details = {
        "parentEmail": user['email'],
        "parentPassword": user['password'],
        "parentPhone": user['phoneNumber'],
        "parentAddress": user['address'],
        "orderId": user['orderId'],
        "key": user['key']
    }

    logger.info(account_details)
    json_response = await HttpClient(url).post(f"/profile/{profile_id}/family/parent", account_details)
    logger.info(json_response)


async def signup(profile_id, environment, browser, user):
    # browser.execute_script("window.devtools.open()")
    browser.get('https://doordash.com')
    await asyncio.sleep(2)
    load_cookie(browser, "doordash")
    await asyncio.sleep(2)
    browser.get('https://doordash.com')
    await asyncio.sleep(2)

    try:
        acceptAllButton = browser.find_element(By.XPATH, "//button[@id='cassie_accept_all_pre_banner']")
        acceptAllButton.click()
    except:
        logger.info("Cookieee popup not found!")

    await asyncio.sleep(4)
    save_cookie(browser, user['email'])

    try:
        signUpButton = browser.find_element(By.XPATH, '//span[text()="Sign Up"]')
        signUpButton.click()
    except:
        logger.info("signup button not found")
    await asyncio.sleep(5)
    # Wait until the element is present
    iframe = browser.find_element(By.XPATH, "//iframe[@title='Login/Signup']")
    browser.switch_to.frame(iframe)
    try:
        inputFirstName = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentitySignupFirstNameField']")
        for char in user['firstName']:
            inputFirstName.send_keys(char)
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.3)
        inputLastName = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentitySignupLastNameField']")
        for char in user['lastName']:
            inputLastName.send_keys(char)
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.3)

        inputEmail = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentitySignupEmailField']")
        await asyncio.sleep(0.3)
        for char in user['email']:
            inputEmail.send_keys(char)
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.5)
        inputPhone = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentitySignupPhoneField']")
        await asyncio.sleep(0.3)
        for char in user['phoneNumber']:
            inputPhone.send_keys(char)
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.5)
        inputPassword = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentitySignupPasswordField']")
        for char in user['password']:
            inputPassword.send_keys(char)
            await asyncio.sleep(0.5)
    except:
        logger.info("Error while inputting signup form values")

    await asyncio.sleep(0.7)
    signupButton = browser.find_element(By.XPATH, '//span[text()="Sign Up"]')
    signupButton.click()
    await asyncio.sleep(4)

    #

    #
    # await asyncio.sleep(5)
    #
    # def get_random_integer(min_val, max_val):
    #     return str(random.randint(min_val, max_val))
    #
    # select_month = browser.find_element_by_css_selector('select[title="Month:"]')
    # select = Select(select_month)
    # select.select_by_value(get_random_integer(1, 12))
    #
    # select_day = browser.find_element_by_css_selector('select[title="Day:"]')
    # select = Select(select_day)
    # select.select_by_value(get_random_integer(1, 29))
    #
    # select_year = browser.find_element_by_css_selector('select[title="Year:"]')
    # select = Select(select_year)
    # select.select_by_value(get_random_integer(1965, 2000))
    #
    # await asyncio.sleep(5)
    #
    # next_buttons = browser.find_element_by_xpath('//button[text()="Next"]')
    # next_buttons.click()
    #
    # await asyncio.sleep(10)
    #
    # status, otp_message = await fetch_otp_details()
    # inputConfirmationCode = wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=confirmationCode]")))
    # await asyncio.sleep(5)
    # if status != 1:
    #     for char in otp_message:
    #         inputConfirmationCode.send_keys(char)
    #         await asyncio.sleep(0.5)
    #     await asyncio.sleep(5)
    #     confirmation_signup_button = browser.find_element_by_xpath('//button[text()="Confirm"]')
    #     confirmation_signup_button.click()
    #     # await add_account_data_to_profile()

    await asyncio.sleep(2)

    await asyncio.sleep(5)

    await add_account_data_to_profile(profile_id, user)

    # browser.close()
    browser.switch_to.default_content()

    delivery_city = browser.find_element(By.ID, "HomeAddressAutocomplete")
    for char in "New york":
        delivery_city.send_keys(char)
        await asyncio.sleep(0.5)

    await asyncio.sleep(5)

    find_restro_btn = browser.find_element(By.XPATH, "//button[@aria-label='Find Restaurants']")
    find_restro_btn.click()

    await asyncio.sleep(15)

    try:
        browser.find_elements(By.XPATH,"//span[text()='Skip']")[0].click()
    except:
        logger.info("Suggestion Popup not found")

    await asyncio.sleep(10)

    await verify_phone(browser, environment, user)

    await asyncio.sleep(50)