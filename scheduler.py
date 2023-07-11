import datetime
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import json

from lib.doordash.likePosts import like_post
from lib.doordash.followAccounts import follow_accounts
from lib.doordash.uploadProfilePhoto import update_profile_bio

async def follow_people():
    await follow_accounts()

async def like_posts(follow_people=False):
    await like_post()
    if follow_people:
        await follow_accounts()

async def like_x_posts(count):
    await like_post(count)

async def add_bio():
    await update_profile_bio()

async def perform_action(action, parameters=None):
    if action == "follow_people":
        await follow_people()
    elif action == "like_posts":
        await like_posts(parameters.get("follow_people", False))
    elif action == "like_x_posts":
        await like_x_posts(parameters["count"])
    elif action == "add_bio":
        await add_bio()

def get_current_day():
    current_date = datetime.datetime.now()
    return "day_" + str(current_date.day)

async def run_scheduler():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        
    current_day = get_current_day()
    if current_day in config:
        action = config[current_day].get("action")
        parameters = config[current_day].get("parameters")
        await perform_action(action, parameters)
    else:
        print("No action defined for the current day.")

def update_schedule(config):
    with open("config.json", "w") as config_file:
        json.dump(config, config_file)

# Example usage to update the schedule dynamically
# Update the 'config' dictionary with the desired schedule
config = {
    "day_2": {
        "action": "follow_people"
    },
    "day_3": {
        "action": "like_posts"
    },
    "day_4": {
        "action": "like_posts"
    },
    "day_5": {
        "action": "like_posts",
        "parameters": {
            "follow_people": True
        }
    },
    "day_6": {
        "action": "like_posts",
        "parameters": {
            "follow_people": True
        }
    },
    "day_8": {
        "action": "like_x_posts",
        "parameters": {
            "count": 10
        }
    },
    "day_9": {
        "action": "like_x_posts",
        "parameters": {
            "count": 10
        }
    },
    "day_11": {
        "action": "add_bio"
    }
}

update_schedule(config)

asyncio.run(run_scheduler())
