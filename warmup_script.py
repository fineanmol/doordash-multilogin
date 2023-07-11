import asyncio
import concurrent.futures
import os
from datetime import datetime, timedelta
import random
import schedule
import threading
import time

from httpClient import HttpClient
from lib.automation import Automation
from logger import Logger
from model.account import ActionType

logger = Logger.get_instance()


async def perform_action(profile_name, user, account_id, current_day, action_type, count, session_id):
    logger.info("perform_action")
    # Perform the action delay times
    action_delay = random.uniform(0.5, 1)
    time.sleep(action_delay)

    # Perform the action
    if action_type == ActionType.LIKE:
        bot = Automation(profile_name)
        await bot.doordash_like_posts(user, count)
        logger.info(f"[Profile: {profile_name}] Session: {session_id} - [{action_type}] Like {1}/{count}")
    elif action_type == ActionType.FOLLOW:
        bot = Automation(profile_name)
        await bot.doordash_follow_accounts(user, count)
        logger.info(f"[Profile: {profile_name}] Session: {session_id} - [{action_type}] Follow {1}/{count}")
    elif action_type == ActionType.BIO_UPDATE:
        logger.info(action_type)
        bot = Automation(profile_name)
        logger.info("next to action")
        await bot.doordash_update_bio(user)
        logger.info(f"[Profile: {profile_name}] Session: {session_id} - [{action_type}] Bio Update {1}/{count}")
    elif action_type == ActionType.MEDIA_UPLOAD:
        bot = Automation(profile_name)
        logger.info("Next to action")
        await bot.doordash_upload_media_photo(user)
        logger.info(f"[Profile: {profile_name}] Session: {session_id} - [{action_type}] Media Upload {1}/{count}")
    elif action_type == ActionType.BLOCK:
        logger.info(f"[Profile: {profile_name}] Session: {session_id} - [{action_type}] Block {1}/{count}")
    response = await HttpClient("http://127.0.0.1:3001/profile").put(
        f"/{profile_name}/accounts/{account_id}/warmup_configuration/{current_day}/actions/{action_type}/sessions/{session_id}/completed")
    logger.info(response)


def schedule_task(profile_name, user, account_id, current_day, action_type, count, session_id):
    # Run the task immediately
    asyncio.run(perform_action(profile_name, user, account_id, current_day, action_type, count, session_id))


def schedule_and_execute_tasks(profiles):
    # Get the current weekday
    current_day = datetime.now().strftime("%A")

    # Retrieve the actions and their configurations for the current weekday from the warmup configuration
    actions = None
    for profile in profiles:
        for account in profile['accounts']:
            for config in account['warmup_configuration']:
                if config['day_of_week'] == current_day:
                    actions = config['actions']
                    break
            if actions:
                break
        if actions:
            break

    if not actions:
        logger.info(f"No action scheduled for {current_day}")
        return

    # Create a thread pool executor
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(profiles) * len(actions))

    # Schedule the tasks for each profile, account, and action
    for profile in profiles:
        for account in profile['accounts']:
            profile_name = profile['uuid']
            user = {
                'username': account['username'],
                'password': account['password']
            }
            for action in actions:
                action_type = action['action_type']
                sessions = action['sessions']

                for session in sessions:
                    session_id = session['session_id']
                    count = session['count']
                    start_time = datetime.strptime(session['start_time'], "%H:%M:%S").time()
                    end_time = session['end_time']
                    current_time = datetime.now().time()

                    if start_time > current_time:
                        # schedule.every().day.at((datetime.now() + timedelta(seconds=2)).strftime('%H:%M:%S')).do()
                        # Schedule the task at the start time using the schedule library
                        schedule.every().day.at(session['start_time']).do(
                            executor.submit,
                            schedule_task,
                            profile_name, user,
                            account['_id'],
                            current_day,
                            action_type,
                            count, session_id)
                        logger.info(
                            f"Scheduled task for [Profile: {profile_name}] Session: {session_id} - [{action_type}]")

    # Run the schedule in a separate thread
    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Start the schedule thread
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)


async def main():
    profiles = await HttpClient("http://127.0.0.1:3001/profile") \
        .get("/warmup/list")
    # profiles = [{"_id": {"$oid": "64a70171d82d4458c1dec8c8"}, "name": "c3f561ed-620e-4cfa-8045-ad8327dddd26",
    #              "accounts": [{"_id": "abc",
    #                            "warmup_phase": True, "warmup_configuration": [
    #                      {"day_of_week": "Monday", "isAllActionsCompleted": True, "actions": [
    #                          {"action_type": "LIKE", "isActionCompleted": True, "sessions": [
    #                              {"session_id": "session1", "count": {"$numberInt": "1"}, "start_time": "04:08:30",
    #                               "end_time": "08:30:45", "isSessionCompleted": True,
    #                               "_id": {"$oid": "64a7026e1fe88a2c83276874"}},
    #                              {"session_id": "session2", "count": {"$numberInt": "3"}, "start_time": "08:59:52",
    #                               "end_time": "11:39:37", "isSessionCompleted": True,
    #                               "_id": {"$oid": "64a7026e1fe88a2c83276875"}}],
    #                           "_id": {"$oid": "64a7026e1fe88a2c83276873"}}],
    #                       "_id": {"$oid": "64a7026e1fe88a2c83276872"}},
    #                      {"day_of_week": "Tuesday", "isAllActionsCompleted": False, "actions": [
    #                          {"action_type": "MEDIA_UPLOAD", "isActionCompleted": True, "sessions": [
    #                              {"session_id": "session1", "count": {"$numberInt": "4"}, "start_time": "18:36:23",
    #                               "end_time": "21:17:02", "isSessionCompleted": False,
    #                               "_id": {"$oid": "64a7026e1fe88a2c83276878"}}],
    #                           "_id": {"$oid": "64a7026e1fe88a2c83276877"}},
    #                          {"action_type": "BIO_UPDATE", "isActionCompleted": False, "sessions": [
    #                              {"session_id": "session1", "count": {"$numberInt": "9"}, "start_time": "23:46:04",
    #                               "end_time": "05:35:08", "isSessionCompleted": False,
    #                               "_id": {"$oid": "64a7026e1fe88a2c8327687a"}},
    #                              {"session_id": "session2", "count": {"$numberInt": "8"}, "start_time": "10:24:24",
    #                               "end_time": "16:57:01", "isSessionCompleted": False,
    #                               "_id": {"$oid": "64a7026e1fe88a2c8327687b"}}],
    #                           "_id": {"$oid": "64a7026e1fe88a2c83276879"}}],
    #                       "_id": {"$oid": "64a7026e1fe88a2c83276876"}},
    #                      {"day_of_week": "Wednesday", "isAllActionsCompleted": False, "actions": [
    #                          {"action_type": "LIKE", "isActionCompleted": False, "sessions": [
    #                              {"session_id": "session1", "count": {"$numberInt": "3"}, "start_time": "02:23:41",
    #                               "end_time": "07:08:42", "isSessionCompleted": True,
    #                               "_id": {"$oid": "64a7026e1fe88a2c8327687e"}}],
    #                           "_id": {"$oid": "64a7026e1fe88a2c8327687d"}}],
    #                       "_id": {"$oid": "64a7026e1fe88a2c8327687c"}},
    #                      {"day_of_week": "Thursday", "isAllActionsCompleted": False, "actions": [],
    #                       "_id": {"$oid": "64a7026e1fe88a2c8327687f"}},
    #                      {"day_of_week": "Friday", "isAllActionsCompleted": False,
    #                       "actions": [{"action_type": "FOLLOW",
    #                                    "isActionCompleted": False, "sessions": [
    #                               {"session_id": "session1",
    #                                "count": {"$numberInt": "6"},
    #                                "start_time": "01:45:30",
    #                                "end_time": "20:28:18",
    #                                "isSessionCompleted": False,
    #                                "_id": {"$oid": "64a7026e1fe88a2c83276882"}}],
    #                                    "_id": {
    #                                        "$oid": "64a7026e1fe88a2c83276881"}},
    #                                   {"action_type": "BIO_UPDATE",
    #                                    "isActionCompleted": False, "sessions": [
    #                                       {"session_id": "session1",
    #                                        "count": {"$numberInt": "2"},
    #                                        "start_time": "01:46:00",
    #                                        "end_time": "13:52:23",
    #                                        "isSessionCompleted": False, "_id": {
    #                                           "$oid": "64a7026e1fe88a2c83276884"}},
    #                                       {"session_id": "session2",
    #                                        "count": {"$numberInt": "6"},
    #                                        "start_time": "00:45:50",
    #                                        "end_time": "07:47:38",
    #                                        "isSessionCompleted": False, "_id": {
    #                                           "$oid": "64a7026e1fe88a2c83276885"}},
    #                                       {"session_id": "session3",
    #                                        "count": {"$numberInt": "9"},
    #                                        "start_time": "00:46:02",
    #                                        "end_time": "04:35:33",
    #                                        "isSessionCompleted": False, "_id": {
    #                                           "$oid": "64a7026e1fe88a2c83276886"}}],
    #                                    "_id": {
    #                                        "$oid": "64a7026e1fe88a2c83276883"}}],
    #                       "_id": {"$oid": "64a7026e1fe88a2c83276880"}},
    #                      {"day_of_week": "Saturday", "isAllActionsCompleted": False, "actions": [
    #                          {"action_type": "LIKE", "isActionCompleted": False, "sessions": [
    #                              {"session_id": "session1", "count": {"$numberInt": "8"}, "start_time": "01:30:30",
    #                               "end_time": "04:18:11", "isSessionCompleted": False,
    #                               "_id": {"$oid": "64a7026e1fe88a2c83276889"}},
    #                              {"session_id": "session2", "count": {"$numberInt": "1"}, "start_time": "20:43:30",
    #                               "end_time": "01:35:11", "isSessionCompleted": False,
    #                               "_id": {"$oid": "64a7026e1fe88a2c8327688a"}}],
    #                           "_id": {"$oid": "64a7026e1fe88a2c83276888"}}],
    #                       "_id": {"$oid": "64a7026e1fe88a2c83276887"}},
    #                      {"day_of_week": "Sunday", "isAllActionsCompleted": False,
    #                       "actions": [{"action_type": "BIO_UPDATE",
    #                                    "isActionCompleted": False, "sessions": [
    #                               {"session_id": "session1",
    #                                "count": {"$numberInt": "8"},
    #                                "start_time": "08:14:29",
    #                                "end_time": "14:25:53",
    #                                "isSessionCompleted": False,
    #                                "_id": {"$oid": "64a7026e1fe88a2c8327688d"}},
    #                               {"session_id": "session2",
    #                                "count": {"$numberInt": "5"},
    #                                "start_time": "21:23:49",
    #                                "end_time": "22:18:36",
    #                                "isSessionCompleted": False,
    #                                "_id": {"$oid": "64a7026e1fe88a2c8327688e"}}],
    #                                    "_id": {
    #                                        "$oid": "64a7026e1fe88a2c8327688c"}},
    #                                   {"action_type": "MEDIA_UPLOAD",
    #                                    "isActionCompleted": False, "sessions": [
    #                                       {"session_id": "session1",
    #                                        "count": {"$numberInt": "6"},
    #                                        "start_time": "03:45:21",
    #                                        "end_time": "09:43:17",
    #                                        "isSessionCompleted": True, "_id": {
    #                                           "$oid": "64a7026e1fe88a2c83276890"}},
    #                                       {"session_id": "session2",
    #                                        "count": {"$numberInt": "5"},
    #                                        "start_time": "23:03:17",
    #                                        "end_time": "01:41:22",
    #                                        "isSessionCompleted": False, "_id": {
    #                                           "$oid": "64a7026e1fe88a2c83276891"}}],
    #                                    "_id": {
    #                                        "$oid": "64a7026e1fe88a2c8327688f"}}],
    #                       "_id": {"$oid": "64a7026e1fe88a2c8327688b"}}],
    #                            "daily_actions": []}],
    #              "uuid": "2888c04a-b06f-4c2a-b143-07d65484185c"}]

    schedule_and_execute_tasks(profiles)


if __name__ == '__main__':
    asyncio.run(main())
