import asyncio
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pickle

from logger import Logger
from util.utility import verify_phone, get_referral_link

logger = Logger.get_instance()


# Save cookies to a file
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


async def signin(environment, browser, user):
    # user = {
    #     'email': 'nikhilnishadatuk+spam@gmail.com',
    #     'password': 'Zxcvbnm#123'
    # }
    # logger.info("Starting sigin: " + user)
    browser.get('https://doordash.com')
    await asyncio.sleep(2)
    load_cookie(browser, user['email'])
    await asyncio.sleep(2)
    browser.get('https://doordash.com')
    await asyncio.sleep(2)
    try:
        acceptAllButton = browser.find_element(By.XPATH, "//button[@id='cassie_accept_all_pre_banner']")
        acceptAllButton.click()
    except:
        logger.info("Cookieee popup not found!")
    await asyncio.sleep(5)
    # Check if element with id "myElement" exists
    elements = browser.find_elements(By.XPATH, '//span[text()="Sign In"]')
    if len(elements) > 0:
        logger.info("Not logged In")

        elements[0].click()
        await asyncio.sleep(3)
        # Wait until the element is present
        iframe = browser.find_element(By.XPATH, "//iframe[@title='Login/Signup']")
        browser.switch_to.frame(iframe)

        await asyncio.sleep(5)

        inputEmail = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentityLoginPageEmailField']")
        for char in user['email']:
            inputEmail.send_keys(char)
            await asyncio.sleep(0.5)

        nextToPassword = browser.find_element(By.XPATH, '//span[text()="Continue to Sign In"]')
        nextToPassword.click()
        await asyncio.sleep(3)

        try:
            buttonToSwitchToPassword = browser.find_element(By.XPATH, '//span[text()="Use password instead"]')
            buttonToSwitchToPassword.click()

        except:
            logger.info("OTP component not found")
        await asyncio.sleep(2)

        inputPassword = browser.find_element(By.XPATH, "//input[@data-anchor-id='IdentityLoginPagePasswordField']")
        for char in user['password']:
            inputPassword.send_keys(char)
            await asyncio.sleep(0.5)

        signin_button = browser.find_element(By.XPATH, '//span[text()="Sign In"]')
        await asyncio.sleep(4)
        signin_button.click()

        time.sleep(5)
        logger.info('Login Success, Ready for the next step..')
        browser.switch_to.default_content()
    else:
        logger.info("Already Logged In")
        time.sleep(2)
    try:
        time.sleep(1)
        browser.find_element(By.XPATH,"//span[text()='Skip']").click()
    except:
        logger.info("Suggestion Popup not found")
    await asyncio.sleep(2)
    save_cookie(browser, user['email'])
    await asyncio.sleep(5)

    # await verify_phone(browser, environment, user)
    await get_referral_link(browser,environment,user)


async def update_profile_bio(browser, user, quote):
    try:
        pass

    except Exception as e:
        logger.info(f"An error occurred: {e}")

    finally:
        browser.quit()

# //span[contains(text(), "Get $") and contains(text(), " in Credits")]
