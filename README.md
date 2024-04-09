# CartomanteTarot_Bot - English

![CartomanteTarot_Bot](https://github.com/parrelladev/CartomanteTarot_Bot/assets/126002318/96500a0d-92fb-4d46-923c-f8ddda593e48)

## About

The CartomanteTarot_Bot is a Telegram chatbot assistant that uses the Llama2 API to interpret Tarot. It allows users to ask questions and receive readings based on randomly selected Tarot cards, providing insights and guidance on personal, professional, and spiritual matters.

## Features

- **Card Reading**: Users can initiate a Tarot card reading by answering a question, which will be interpreted based on the selected cards.
- **Translation**: Responses are translated from English to Portuguese, ensuring clear and understandable communication. Change this line to change the translation: `translation = GoogleTranslator(source="en", target="pt").translate(text)`
- **Interaction**: The bot offers a friendly interface, with options to understand the bot's functionality, learn about Tarot, and perform card readings.

## How to Use

1. **Start the Bot**: To start using the CartomanteTarot_Bot, send the `/start` command to the bot on Telegram.
2. **Select Option**: Choose one of the available options in the menu to understand the bot's functionality, learn about Tarot, or perform a card reading.
3. **Perform Reading**: If you choose to perform a card reading, the bot will ask you to type your question. After that, it will draw three random cards from the deck and provide a reading based on those cards.

## Requirements

- Python 3.6 or higher
- Python Libraries: `telebot`, `requests`, `json`, `deep_translator`
- Telegram Bot API Token
- Llama2 installed on the machine `https://ollama.com/`

## Installation

1. Clone the repository or download the source code.
2. Install the necessary dependencies with the command `pip install telebot requests deep_translator`.
3. Configure the Telegram bot token and the Llama2 API URL in the `APIs.py` file.
4. Run the Python script to start the bot.

## Contribution

Contributions are welcome! If you find bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
