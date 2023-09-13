# Aiogram bot
This bot created as example of my code. I use "Aiogram" to connect telegram API,
Redis as cashed database and containerized with docker. 

## Getting Started

1. Clone this repository to your local machine: `git clone https://github.com/Plat01/ya_bot.git
cd your-telegram-bot`

2. Create a .env file in the project directory and add the following environment 
variables, _replacing the placeholders with your bot token and Redis configuration_:

`TOKEN=your_bot_token_here
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=5`

3. Build and run the bot and Redis services using Docker Compose: `docker-compose up -d`


Open the Telegram app, search for your bot by its username (e.g., `@YourBotUsername`), and start a chat to interact with your bot.