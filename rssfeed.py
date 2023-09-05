import os
import requests
import re
from bs4 import BeautifulSoup
import time

# RSS feed URL
RSS_FEED_URL = os.environ.get('RSS_FEED_URL')
# https://www.codeur.com/projects?budgets%5B%5D=750&budgets%5B%5D=4500&budgets%5B%5D=15000&format=rss&order=most_recent&states%5B%5D=published&user_id=192062

# Discord webhook URL
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')
# https://discord.com/api/webhooks/1139562394587238594/9KsUubk3_VPOIZmB6vpW3ULDmC6ojt_JEVixhGWH5pUcGmBl0_JLII-NG7fI-dYMrg8H

# Check if the environment variables are present
if not RSS_FEED_URL or not DISCORD_WEBHOOK_URL:
    print("Error: Missing environment variables. Ensure RSS_FEED_URL and DISCORD_WEBHOOK_URL are set.")
    exit(1)


ARRAY_TAG = os.environ.get('ARRAY_TAG')
MESSAGE_TEMPLATE = os.environ.get('MESSAGE_TEMPLATE')

if not ARRAY_TAG or not MESSAGE_TEMPLATE:
    print("Error: Missing environment variables. Ensure ARRAY_TAG and MESSAGE_TEMPLATE are set.")
    exit(1)

tags = re.findall(r'{(.*?)}', MESSAGE_TEMPLATE)

# Store the titles of posted items
posted_items = []

def post_to_discord(item):
    data = {
        "content": MESSAGE_TEMPLATE.format(**item)
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)

print('Starting...')

while True:
    print('Fetching new posts...')
    response = requests.get(RSS_FEED_URL)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all(ARRAY_TAG)
    
    new_items = []
    for item in items:
        current_item = {}
        for tag in tags:
            if item[tag].get('type') == 'html':
                current_item[tag] = BeautifulSoup(item[tag].text, 'lxml').get_text()
            else:
                current_item[tag] = item[tag].text
        if current_item not in posted_items:
            new_items.append(current_item)
        else:
            break

    # If bot just started, post only the latest item
    if not posted_items:
        print('First post found')
        post_to_discord(new_item[0])
        posted_items.append(new_item[0])
    else:
        print('Seen {} new posts'.format(len(new_items)))
        # Post all new items
        for item in reversed(new_items):
            post_to_discord(item)
            posted_items.append(item)

    # Check the RSS feed every 10 minutes
    time.sleep(600)
