# rss-to-discord
An RSS feed to discord proxy

## How to build

Simply run this command : 
```bash
dofigen dofigen.yml && docker build -t rssfeed .
```

## Usage

Example of command to run it : 
```bash
docker service create -td --name rssfeed -e "RSS_FEED_URL=https://www.codeur.com/projects" -e "DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxx" -e "MESSAGE_TEMPLATE={title} {link}\n {description}" -e "ARRAY_TAG=item" rssfeed
```
