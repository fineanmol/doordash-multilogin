import os

import configparser

from selenium import webdriver
from faker import Faker
from lib.crawler import start_crawler
from lib.doordash.doordashSignup import signup
from lib.doordash.signin import signin
from lib.pexel_api import download_random_image
from logger import Logger
from constant import services
from httpClient import HttpClient
import undetected_chromedriver as uc

from util.utility import generate_random_email, generate_us_phone_number, generate_us_city_address, generate_profile, \
    make_email_unique

fake = Faker()
service_list = services.ServiceList()
logger = Logger.get_instance()


async def browser_local():
    # logger.info("browser_local")
    # chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
    # return webdriver.Chrome('./chromedriver/chromedriver')
    options = uc.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--no-sandbox')  # Bypass the sandbox mode
    options.add_argument('--disable-dev-shm-usage')  # Disable /dev/shm usage
    options.add_argument('--disable-blink-features=AutomationControlled')  # Disable automation detection

    options.add_argument("--auto-open-devtools-for-tabs")
    driver = uc.Chrome(options)

    # Set the navigator properties to mimic a real browser
    # driver.implicitly_wait(10)
    # driver.execute_cdp_cmd('Network.enable', {})
    # driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
    #     'offline': False,
    #     'downloadThroughput': 750 * 1024,
    #     'uploadThroughput': 250 * 1024,
    #     'latency': 50
    # })
    return driver


# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Determine the environment from the command-line argument
input_environment = os.environ.get('ENVIRONMENT', 'Local')

env = config[input_environment]


async def browser_multilogin(profile_id):
    json_response = await HttpClient("http://127.0.0.1:35000/api/v1/profile") \
        .get(f"/start?automation=true&profileId={profile_id}")
    return webdriver.Remote(command_executor=json_response['value'])


class Automation:
    def __init__(self, profile_id):
        logger.info("Automation instance")
        self.profile_id = profile_id
        self.environment = env

    async def sign_in_to_doordash(self, user):
        logger.info("sign_in_to_doordash")
        browser = await self.get_browser()
        await signin(self.environment, browser, user)
        return browser

    async def doordash_like_posts(self, user, daily_limit):
        browser = await self.sign_in_to_doordash(user)
        await like_post(browser, daily_limit)
        browser.quit()

    async def doordash_upload_profile_photo(self, user, photo_path):
        browser = await self.sign_in_to_doordash(user)

    async def doordash_update_bio(self, user):
        browser = await self.sign_in_to_doordash(user)
        logger.info("Signin browser found")
        quote = fake.sentence(nb_words=10, variable_nb_words=True)
        await update_profile_bio(browser, user, quote)
        browser.quit()

    async def doordash_follow_accounts(self, user, follow_count):
        browser = await self.sign_in_to_doordash(user)
        logger.info("Signin browser found")
        await follow_accounts(browser, follow_count)
        browser.quit()

    async def generate_doordash_account(self):
        CountryId = '1'
        profile = generate_profile()
        user = {'firstName': profile['name'].split(" ")[0], 'lastName': profile['name'].split(" ")[1],
                'email': make_email_unique(profile['mail']),
                'phoneNumber': generate_us_phone_number(), 'password': fake.password(length=12),
                'name': profile['name'], 'address': generate_us_city_address("")}

        print(f'[UserInformation],{user}')

        for element in service_list.get_services():
            if element.name == 'United States':
                CountryId = element.id

        ServiceId = '280'  # Doordash
        jsonData = await HttpClient(self.environment['sms_pool_purchase_api']) \
            .get(f"?key={self.environment['key']}&country={CountryId}&service={ServiceId}")
        phoneNumber = jsonData['phonenumber']
        orderId = jsonData['order_id']
        country = jsonData['country']
        success = jsonData['success']
        countryCode = jsonData['cc']
        message = jsonData['message']

        user['phoneNumber'] = str(phoneNumber)
        user['orderId'] = orderId
        user['key'] = self.environment['key']

        if message.startswith('This country is currently not available for this service'):
            print('[Error Message]', {'jsonData': jsonData})

        browser = await self.get_browser()

        await signup(self.profile_id, self.environment, browser, user)

    async def get_browser(self):
        browser = await browser_multilogin(self.profile_id) \
            if self.environment.getboolean('isProd') \
            else await browser_local()
        return browser

    async def create_browser_history(self):
        browser = await self.get_browser()
        await start_crawler(browser, self.profile_id)

    async def doordash_upload_media_photo(self, user):
        browser = await self.sign_in_to_doordash(user)
        media_path, caption = await download_random_image()
        await upload_media_photo(browser, media_path, caption)
        browser.quit()
