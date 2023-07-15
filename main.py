import asyncio
import os

from aioconsole import ainput

from httpClient import HttpClient
from lib.automation import Automation
from logger import Logger

logger = Logger.get_instance()


async def main():
    await sign_in_doordash_account()
    actions = {
        '1': create_multilogin_profile,
        '2': create_doordash_account,
        '3': crawl,
        '4': exit_program,

    }

    while True:
        print('\n' +
              'Enter action to perform.\n' +
              '1. Create Multilogin Profile\n' +
              '2. Create Doordash Account\n' +
              '3. Crawl \n' +
              '4. Exit\n' +
              '\n')

        user_input = input("Please enter your input: ")

        # Perform actions based on user input
        action = actions.get(user_input)
        if action:
            await action()
        else:
            # Handle invalid input
            print("Invalid input. Please try again.\n")


async def create_multilogin_profile():
    profile_count = await ainput("Input number of profiles to be created: ")
    jsonData = await HttpClient("http://localhost:3001").post(f"/profile/generate/{profile_count}")
    logger.info(jsonData)
    # Your code for creating a Multi-login profile goes here


async def create_doordash_account():
    print("Creating Dordash Account...")
    # jsonData = await HttpClient("http://localhost:3001").get("/profile/unused")
    # for profile in jsonData['profiles']:
    #     logger.info(profile['uuid'])
    bot = Automation('uuid')
    await bot.generate_doordash_account()


async def sign_in_doordash_account():
    bot = Automation('dummyUUid')
    await bot.sign_in_to_doordash({})


def exit_program():
    print("Exiting...")
    raise SystemExit


async def crawl():
    #jsonData = await HttpClient("http://localhost:3001").get("/profile/unused")
    # for profile in jsonData['profiles']:
    #     logger.info(profile['uuid'])
    #     bot = Automation(profile['uuid'])
    #     await bot.create_browser_history()
    bot = Automation("profile['uuid']")
    await bot.create_browser_history()
    await create_doordash_account()

async def upload_profile_photo():
    bot = Automation("")
    await bot.doordash_upload_profile_photo("/Users/nikhil_nishad/Develop/python/multilogin-python/LinkedIn_icon.png")


async def upload_media():
    bot = Automation("")
    await bot.doordash_upload_media_photo({"username": "jasonford468", "password": ")7Y9sxfJJ&4Q"})


asyncio.run(main())
