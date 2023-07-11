import aiohttp
import asyncio
import random
import os
from faker import Faker

fake = Faker()


async def download_random_image():
    file_path = 'random_image.jpg'
    api_key = 'SL8nlay8reg0i4xtuhw8cP54BvoVbIVpHVgv8ZHX5yCjqFolQP30IeOV'

    headers = {"Authorization": api_key}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get("https://api.pexels.com/v1/search?query=nature&per_page=80") as response:
            if response.status == 200:
                json_response = await response.json()
                photos = json_response["photos"]
                random_photo = random.choice(photos)
                download_url = random_photo["src"]["original"]
                async with session.get(download_url) as image_response:
                    if image_response.status == 200:
                        with open(file_path, 'wb') as file:
                            while True:
                                chunk = await image_response.content.read(1024)
                                if not chunk:
                                    break
                                file.write(chunk)
                        print(f"Random image downloaded successfully and saved as {file_path}")
                        return os.path.abspath(file_path),\
                            fake.sentence(nb_words=10, variable_nb_words=True)
                    else:
                        print("Failed to download random image")
            else:
                print("Failed to get random image URL")


# Example usage:
# loop = asyncio.get_event_loop()
# absolute_file_path = loop.run_until_complete(download_random_image(api_key, file_name))
# if absolute_file_path:
#     print(f"Absolute file path: {absolute_file_path}")
