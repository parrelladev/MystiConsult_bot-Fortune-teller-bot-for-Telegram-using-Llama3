# MystiConsult_bot - Telegram Bot

![CartomanteTarot_Bot](https://github.com/parrelladev/CartomanteTarot_Bot/assets/126002318/96500a0d-92fb-4d46-923c-f8ddda593e48)

## About

MystiConsult_bot is a Telegram bot that offers Tarot and horoscope readings. Using the Llama3 API, the bot provides insights and guidance on personal, professional and spiritual issues through a simple and direct interaction.

## Features

- **Card Reading**: Users can initiate a Tarot card reading by answering a question, which will be interpreted based on the selected cards.
- **Horoscope**:  Offers daily insights based on the user's chosen zodiac sign.
- **Translation**: Responses are translated from English to Portuguese, ensuring clear and understandable communication. Change this line to change the translation: `translation = GoogleTranslator(source="en", target="pt").translate(text)`
- **Interaction**: The bot offers a friendly interface, with options to understand the bot's functionality, learn about Tarot, and perform card readings.

## How to Use

1. **Start the Bot**: Send the /start command to the bot on Telegram to get started.
2. **Select Option**: Choose between "Perform tarot reading", "Understand how the bot works", "Learn about Tarot" or "Consult my horoscope" to start the interaction.
3. **Tarot Reading**: If you choose a Tarot reading, enter your question and wait for the answer.
4. **Horoscope**: To consult your horoscope, select "Consult my horoscope" and choose your zodiac sign.

## Requirements

- Python 3.6 or higher
- Python Libraries: `telebot`, `requests`, `json`, `deep_translator`
- Telegram Bot API Token
- Llama3 installed on the machine `https://ollama.com/`

## Installation

1. Clone the repository or download the source code.
2. Install the necessary dependencies with the command `pip install telebot requests deep_translator`.
3. Configure the Telegram bot token and the Llama3 API URL in the `APIs.py` file.
4. Run the Python script to start the bot.