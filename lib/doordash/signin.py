import asyncio
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pickle

from logger import Logger

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
        logger.info("An unexpected error occurred:"+ str(e))


async def signin(browser,user):
    # user = {
    #     'email': 'jasonford468',
    #     'password': ')7Y9sxfJJ&4Q'
    # }
    # logger.info("Starting sigin: "+user)
    browser.get('https://doordash.com')
    await asyncio.sleep(2)
    load_cookie(browser, user['username'])
    await asyncio.sleep(2)
    browser.get('https://doordash.com')
    await asyncio.sleep(2)
    try:
        logger.info("Clinking accept cookies")
        accept_cookies_button = browser.find_element_by_xpath('//button[text()="Allow all cookies"]')
        accept_cookies_button.click()
    except Exception as e:
        logger.info("Accept cookie button not found!")
    await asyncio.sleep(5)
    # Check if element with id "myElement" exists
    elements = browser.find_elements_by_xpath('//div[text()="Log in"]')
    if len(elements) > 0:
        logger.info("Not logged In")
        # Wait until the elements are present
        wait = WebDriverWait(browser, 30)  # Maximum wait time of 30 seconds
        input_email_or_phone = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=username]")))
        input_email_or_phone.send_keys(user.get('username'))

        password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=password]")))
        password.send_keys(user.get('password'))

        signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Log in")]')))
        await asyncio.sleep(4)
        signin_button.click()

        time.sleep(5)
        logger.info('Login Success, Ready for the next step..')
        try:
            save_your_login_info_button = browser.find_element_by_xpath('//button[@type="button"]')
            save_your_login_info_button.click()
        except:
            logger.info("Save Login Details Popup not available")
    else:
        logger.info("Already Logged In")
        time.sleep(2)
    try:
        button_notification = browser.find_element_by_xpath('//button[text()="Not Now"]')
        button_notification.click()
    except:
        logger.info("Turn On Notification popup not found")
    await asyncio.sleep(2)
    save_cookie(browser, user['username'])
    await asyncio.sleep(5)


async def update_profile_bio(browser,user, quote):
    try:
       pass

    except Exception as e:
        logger.info(f"An error occurred: {e}")

    finally:
        browser.quit()
