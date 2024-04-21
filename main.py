# Importando bibliotecas necessárias
import random
import telebot
import requests
import json
from APIs import BOT_TOKEN, LLM_API_URL
from deep_translator import GoogleTranslator

# Inicializando o bot com o token fornecido
bot = telebot.TeleBot(BOT_TOKEN)

# Função para traduzir texto do inglês para o português
def translate_text(text):
    translation = GoogleTranslator(source="en", target="pt").translate(text)
    return translation

# Função para gerar uma resposta baseada na pergunta do usuário e nas cartas do Tarot
def generate_response(user_question, cards_message):
    payload = {
        "role": "assistant",
        "model": "llama3",
        "prompt": "From now on you will take on the role of tarot interpreter. Your task is to help the user uncover the symbolic messages of the tarot and apply them to the specific situation the user will share. Please remember that the interpretations of the tarot cards are subjective and aim to promote reflection and self-knowledge. Be respectful and sensitive when dealing with personal issues. Don't respond with questions. Respond with direct and objective language, providing insights and short guidance (maximum 500 tokens) based on the cards indicated below:\n\n" + cards_message + "\n\n" + user_question,
        "max_new_tokens": 500,
        "min_new_tokens": -1
    }

    try:
        # Fazendo a requisição à API
        response = requests.post(LLM_API_URL, json=payload)
        # Processando a resposta
        response_lines = response.text.strip().split('\n')
        concatenated_response = "".join([json.loads(line)["response"] for line in response_lines if "response" in json.loads(line)])
        return concatenated_response

    except Exception as e:
        # Caso ocorra um erro, retorna a mensagem de erro
        return f"Error: {str(e)}"

# Função para iniciar a leitura das cartas do Tarot
def interpret_tarot(message):
    # Enviando uma mensagem pedindo ao usuário para digitar a pergunta
    sent = bot.reply_to(message, "🗯️ Por favor, digite a pergunta que você deseja fazer ao Tarot e espere eu fazer a leitura das cartas.")
    # Registrando o próximo passo para processar a pergunta do usuário
    bot.register_next_step_handler(sent, process_question)

# Função para processar a pergunta do usuário e gerar a resposta
def process_question(message):
    # Obtendo a pergunta do usuário
    user_question = message.text
    # Gerando as cartas do Tarot
    drawn_cards = generate_cards()
    # Montando a mensagem com as cartas
    cards_message = "\n".join([f"{i+1}. {card}" for i, card in enumerate(drawn_cards)])
    # Enviando a mensagem com as cartas para o usuário
    response = (
        f"🧙‍♀️ Acabei de tirar do baralho algumas cartas aleatórias para você. Elas são:\n\n"
        f"{cards_message}\n\n"
    )
    bot.send_message(message.chat.id, response)
    # Enviando uma mensagem informando que a leitura está sendo feita
    sent_message = bot.send_message(message.chat.id, "🔮 Estou fazendo a leitura. Me dê uns segundinhos...")
    # Obtendo o ID da mensagem enviada
    message_id = sent_message.message_id
    # Gerando a resposta baseada na pergunta e nas cartas
    response = generate_response(user_question, cards_message)
    # Traduzindo a resposta para o português
    translation = translate_text(response)
    # Editando a mensagem anterior com a resposta traduzida
    bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=translation)
    # Enviando a mensagem de encerramento
    bot.send_message(message.chat.id, "Espero que tenha gostado da consulta! 😉 Selecione o que você deseja fazer agora.")

# Função para gerar cartas aleatórias do Tarot
def generate_cards():
    cards = [
        "O Louco", "O Mago", "A Sacerdotisa", "A Imperatriz", "O Imperador",
        "O Hierofante", "Os Amantes", "A Carruagem", "A Justiça", "O Eremita",
        "A Roda da Fortuna", "A Força", "O Enforcado", "A Morte", "A Temperança",
        "O Diabo", "A Torre", "A Estrela", "A Lua", "O Sol", "O Julgamento", "O Mundo"
    ]
    return random.sample(cards, 3)

# Função para enviar uma mensagem de boas-vindas ao usuário
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Entender o funcionamento do bot")
    item2 = telebot.types.KeyboardButton("Aprender sobre Tarot")
    item3 = telebot.types.KeyboardButton("Realizar leitura de cartas")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "🧙‍♀️ Olá! Eu sou o CartomanteTarot_Bot.\n\nSelecione uma das opções abaixo para começar:", reply_markup=markup)

# Função para lidar com mensagens do usuário
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Realizar leitura de cartas":
        interpret_tarot(message)
    elif message.text == "Entender o funcionamento do bot":
        bot.send_message(message.chat.id, "Eu sou um bot que utiliza a API do Llama3 para interpretar o Tarot. Você pode fazer uma pergunta e eu fornecerei uma leitura baseada nas cartas do Tarot.")
    elif message.text == "Aprender sobre Tarot":
        bot.send_message(message.chat.id, "O Tarot é um sistema de leitura de cartas que utiliza imagens e símbolos para fornecer insights e orientações sobre questões pessoais, profissionais e espirituais.")
    else:
        bot.send_message(message.chat.id, "Desculpe, não consegui entender sua escolha. Por favor, selecione uma das opções no menu.", reply_markup=markup)

# Iniciando o bot
bot.polling()
