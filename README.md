# rss-to-discord
An RSS feed to discord proxy

## Usage

Example of command to run it : 
```bash
docker service create -td --name rssfeed -e "RSS_FEED_URL=https://www.codeur.com/projects" -e "DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxx" -e "MESSAGE_TEMPLATE={title} {link}\n {description}" -e "ARRAY_TAG=item" shiishii/kaede-rssfeed
```
