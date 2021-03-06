from dotenv import dotenv_values
from telethon.sync import TelegramClient

config = dotenv_values(".env")
api_id = config['API_ID']
api_hash = config['API_HASH']

spam_group_list = None

with TelegramClient('name', api_id, api_hash) as client:

    with open('spam_groups.txt', 'r') as f:
        spam_group_list = f.readlines()

    def send_multiple_message():

        for spam_group in spam_group_list:
            try:
                client.send_message(spam_group, 'https://t.me/cashin_guadagni_passivi')
            except:
                print("An exception occurred")
        exit()
        # await asyncio.sleep(60*3)

    send_multiple_message()

    client.run_until_disconnected()