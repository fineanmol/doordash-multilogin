import asyncio
import random
import string

import aiohttp
from random_address import real_random_address, random_address
from faker import Faker
from selenium.webdriver.common.by import By

from logger import Logger

fake = Faker(['en_US'])
logger = Logger.get_instance()


def generate_random_email():
    domains = ["@gmail.com", "@outlook.com", "@yahoo.com"]
    domain = random.choice(domains)
    email = fake.user_name() + domain
    return email


def generate_us_phone_number():
    phone_number = fake.basic_phone_number()
    return phone_number


def generate_us_city_address(city):
    return random_address.real_random_address_by_state('CA')


def generate_profile():
    return fake.profile()


async def fetch_otp_details(environment, user):
    logger.info(user)
    logger.info(f"{environment['sms_pool_fetch_api']}?orderid={user['orderId']}&key={user['key']}")
    api_status = 1
    while api_status not in [0, 2, 3, 4, 5, 6]:
        try:
            await asyncio.sleep(60)
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        f"{environment['sms_pool_fetch_api']}?orderid={user['orderId']}&key={user['key']}") as response:
                    logger.info(response)
                    if response.status == 200:
                        json_data = await response.json()
                        api_status, message = process_response(json_data)
                        logger.info(str(api_status) + " " + message)
                        await asyncio.sleep(4)
                    else:
                        logger.info(response)
                        logger.info('API status:' + str(response.status))
                        break
        except Exception as e:
            logger.info('An error occurred while checking API status:' + str(e))
    logger.info('[Status of the API is] ' + str(api_status))
    return api_status, message


async def verify_phone(browser, environment, user):
    try:
        open_menu = browser.find_element(By.XPATH, "//button[@aria-label='Open Menu']")
        open_menu.click()
        await asyncio.sleep(5)

        account_btn = browser.find_element(By.XPATH, "//span[text() = 'Account']")
        account_btn.click()

        await asyncio.sleep(3)
        verify_btn = browser.find_element(By.XPATH, "//span[text() = 'Verify']")
        verify_btn.click()
        await asyncio.sleep(5)

        otp_input = browser.find_element(By.XPATH, "//input[@type='number']")

        status, otp_message = await fetch_otp_details(environment, user)
        if status == 3:
            for char in otp_message:
                otp_input.send_keys(char)
                await asyncio.sleep(0.5)
        else:
            logger.info(f"SMS API returned status: {status}")
        await asyncio.sleep(0.5)

        otp_submit_btn = browser.find_element(By.XPATH, "//span[text() = 'Submit']")
        otp_submit_btn.click()
    except:
        logger.info("Verify btn not found")


def process_response(response):
    if "status" in response and "message" in response:
        logger.info(response)
        status = response["status"]
        switch_cases = {
            1: "pending",
            2: "expired",
            4: "resend",
            5: "cancelled",
            6: "refunded"
        }
        message = switch_cases.get(status, "")
        return status, message
    elif "success" in response and response["success"] == 0:
        return response["success"], response["message"]
    elif "status" in response and "sms" in response:
        return response["status"], response["sms"]


def make_email_unique(email):
    username, domain = email.split('@', 1)
    random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    return f"{username}_{random_string}@{domain}"
