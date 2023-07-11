import subprocess
import threading

import schedule
import time

def schedule_jobs():
    # Run your main script using subprocess
    subprocess.run(['python', 'warmup_script.py'], check=True)


# Schedule the job to run every day at 00:00
schedule.every().day.at("00:30:00").do(schedule_jobs)


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
