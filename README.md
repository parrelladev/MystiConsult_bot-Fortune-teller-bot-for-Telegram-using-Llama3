# CartomanteTarot_Bot - English

## About

The CartomanteTarot_Bot is a chatbot assistant that uses the Llama2 API to interpret Tarot. It allows users to ask questions and receive readings based on randomly selected Tarot cards, providing insights and guidance on personal, professional, and spiritual matters.

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

# CartomanteTarot_Bot - Português

## Sobre

O CartomanteTarot_Bot é um assistente de chatbot que utiliza a API do Llama2 para interpretar o Tarot. Ele permite que os usuários façam perguntas e recebam leituras baseadas nas cartas do Tarot, fornecendo insights e orientações sobre questões pessoais, profissionais e espirituais.

## Funcionalidades

- **Leitura de Cartas**: Os usuários podem iniciar uma leitura de cartas do Tarot, respondendo a uma pergunta que será interpretada com base nas cartas selecionadas aleatoriamente.
- **Tradução**: As respostas são traduzidas do inglês para o português, garantindo uma comunicação clara e compreensível. Mude esta linha para mudar a tradução: `translation = GoogleTranslator(source="en", target="pt").translate(text)`
- **Interação**: O bot oferece uma interface amigável, com opções para entender o funcionamento do bot, aprender sobre o Tarot e realizar leituras de cartas.

## Como Usar

1. **Iniciar o Bot**: Para começar a usar o CartomanteTarot_Bot, envie o comando `/start` para o bot no Telegram.
2. **Selecionar Opção**: Escolha uma das opções disponíveis no menu para entender o funcionamento do bot, aprender sobre o Tarot ou realizar uma leitura de cartas.
3. **Realizar Leitura**: Se escolher realizar uma leitura de cartas, o bot pedirá que você digite sua pergunta. Após isso, ele tirará três cartas aleatórias do baralho e fornecerá uma leitura baseada nessas cartas.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python: `telebot`, `requests`, `json`, `deep_translator`
- API Token de Bot do Telegram
- Llama2 instalado na máquina `https://ollama.com/`

## Instalação

1. Clone o repositório ou baixe o código-fonte.
2. Instale as dependências necessárias com o comando `pip install telebot requests deep_translator`.
3. Configure o token do bot do Telegram e a URL da API do Llama2 no arquivo `APIs.py`.
4. Execute o script Python para iniciar o bot.

## Contribuição

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.