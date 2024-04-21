import json
import random
import requests
from deep_translator import GoogleTranslator
import telebot
from APIs import BOT_TOKEN, LLM_API_URL

# Inicializando o bot com o token fornecido
bot = telebot.TeleBot(BOT_TOKEN)

# Definindo o teclado de resposta rápida
markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
item1 = telebot.types.KeyboardButton("Entender o funcionamento do bot")
item2 = telebot.types.KeyboardButton("Aprender sobre Tarot e horóscopos")
item3 = telebot.types.KeyboardButton("Realizar leitura de Tarot")
item4 = telebot.types.KeyboardButton("Consultar meu horóscopo")
markup.add(item1, item2, item3, item4)

# Definindo o teclado de resposta rápida para os signos do zodíaco
zodiac_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
zodiac_signs = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
for sign in zodiac_signs:
    zodiac_markup.add(telebot.types.KeyboardButton(sign))

# Função para traduzir texto do inglês para o português
def translate_text(text):
    translation = GoogleTranslator(source="en", target="pt").translate(text)
    return translation

# Função para gerar cartas aleatórias do Tarot
def generate_cards():
    cards = [
        "O Louco", "O Mago", "A Sacerdotisa", "A Imperatriz", "O Imperador",
        "O Hierofante", "Os Amantes", "A Carruagem", "A Justiça", "O Eremita",
        "A Roda da Fortuna", "A Força", "O Enforcado", "A Morte", "A Temperança",
        "O Diabo", "A Torre", "A Estrela", "A Lua", "O Sol", "O Julgamento", "O Mundo"
    ]
    return random.sample(cards, 3)

# Função para processar a seleção do signo do usuário
def process_zodiac_sign(message):
    # Obtendo o signo do usuário
    user_sign = message.text
    # Gerando a resposta baseada no signo do usuário
    response = generate_response_horoscope(user_sign)
    # Traduzindo a resposta para o português
    translation = translate_text(response)
    # Enviando a resposta traduzida
    bot.send_message(message.chat.id, translation)
    # Enviando a mensagem de encerramento com o teclado de resposta rápida
    bot.send_message(message.chat.id, "Espero que tenha gostado da consulta! 😉\n\nSelecione o que você deseja fazer agora:", reply_markup=markup)

# Função para gerar uma resposta baseada na pergunta do usuário e nas cartas do Tarot
def generate_response(user_question, cards_message):
    payload = {
        "role": "assistant",
        "model": "llama3",
        "prompt": "From now on you will take on the role of tarot interpreter. Your task is to help the user uncover the symbolic messages of the tarot and apply them to the specific situation the user will share. Please remember that the interpretations of the tarot cards are subjective and aim to promote reflection and self-knowledge. Be respectful and sensitive when dealing with personal issues. Don't respond with questions. Respond with direct and objective language, providing insights and short guidance, with a maximum of 600 characters, based on the cards indicated below:\n\n" + cards_message + "\n\n" + user_question,
    }

    try:
        response = requests.post(LLM_API_URL, json=payload)
        response_lines = response.text.strip().split('\n')
        concatenated_response = "".join([json.loads(line)["response"] for line in response_lines if "response" in json.loads(line)])
        return concatenated_response

    except Exception as e:
        return f"Error: {str(e)}"

# Função para gerar uma resposta baseada no signo do usuário
def generate_response_horoscope(user_sign):
    payload = {
        "role": "user",
        "model": "llama3",
        "prompt": user_sign + " It's my zodiac sign! What is my horoscope for the day? Don't respond with questions. Respond with direct and objective language, providing insights and short guidance, with a maximum of 200 characters",
    }

    try:
        response = requests.post(LLM_API_URL, json=payload)
        response_lines = response.text.strip().split('\n')
        concatenated_response = "".join([json.loads(line)["response"] for line in response_lines if "response" in json.loads(line)])
        return concatenated_response

    except Exception as e:
        return f"Error: {str(e)}"

# Função para iniciar a leitura das cartas do Tarot
def interpret_tarot(message):
    sent = bot.reply_to(message, "🗯️ Por favor, digite a pergunta que você deseja fazer ao Tarot e espere eu fazer a leitura das cartas.")
    bot.register_next_step_handler(sent, process_question)

# Função para iniciar a leitura do horóscopo
def interpret_horoscope(message):
    bot.send_message(message.chat.id, "Por favor, escolha um signo do zodíaco abaixo:", reply_markup=zodiac_markup)
    bot.register_next_step_handler(message, process_question_horoscope)

# Função para processar a pergunta do usuário e gerar a resposta
def process_question(message):
    if message.text == "Realizar leitura de Tarot":
        interpret_tarot(message)
    elif message.text == "Entender o funcionamento do bot":
        bot.send_message(message.chat.id, "Eu sou um bot que oferece leituras de tarô e horóscopo. Utilizando a API Llama3, meu objetivo é oferecer insights e orientações sobre questões pessoais, profissionais e espirituais por meio de uma interação misticas e milenares.")
    elif message.text == "Aprender sobre Tarot e horóscopos":
        bot.send_message(message.chat.id, "O Tarot é um sistema de leitura de cartas que utiliza imagens e símbolos para fornecer insights e orientações sobre questões pessoais, profissionais e espirituais.\n\nJá a leitura de horóscopos é uma forma de adivinhação que utiliza a posição dos astros no momento do nascimento de uma pessoa para prever aspectos da sua personalidade e eventos da sua vida.")
    else:
        user_question = message.text
        drawn_cards = generate_cards()
        cards_message = "\n".join([f"{i+1}. {card}" for i, card in enumerate(drawn_cards)])
        response = (
            f"🧙‍♀️ Acabei de tirar do baralho algumas cartas aleatórias para você. Elas são:\n\n"
            f"{cards_message}\n\n"
        )
        bot.send_message(message.chat.id, response)
        sent_message = bot.send_message(message.chat.id, "🔮 Estou fazendo a leitura. Me dê uns segundinhos...")
        message_id = sent_message.message_id
        response = generate_response(user_question, cards_message)
        translation = translate_text(response)
        bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=translation)
        bot.send_message(message.chat.id, "Espero que tenha gostado da consulta! 😉\n\nSelecione o que você deseja fazer agora:", reply_markup=markup)

# Função para processar a pergunta do usuário e gerar a resposta do horóscopo
def process_question_horoscope(message):
    user_sign = message.text
    if user_sign in zodiac_signs: # Verifica se o texto da mensagem é um signo válido
        sent_message = bot.send_message(message.chat.id, "🔮 Estou consultando as estrelas. Me dê uns segundinhos...")
        message_id = sent_message.message_id
        response = generate_response_horoscope(user_sign)
        translation = translate_text(response)
        bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=translation)
        bot.send_message(message.chat.id, "Espero que tenha gostado da consulta! 😉\n\nSelecione o que você deseja fazer agora:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Por favor, escolha um signo do zodíaco válido.", reply_markup=zodiac_markup)

# Manipuladores de Mensagens
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🧙‍♀️ Olá! Eu sou o consultor MystiBot.\n\nSelecione uma das opções abaixo para começar:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Realizar leitura de Tarot":
        interpret_tarot(message)
    elif message.text == "Entender o funcionamento do bot":
        bot.send_message(message.chat.id, "Eu sou um bot que oferece leituras de tarô e horóscopo. Utilizando a API Llama3, meu objetivo é oferecer insights e orientações sobre questões pessoais, profissionais e espirituais por meio de uma interação misticas e milenares.")
    elif message.text == "Aprender sobre Tarot e horóscopos":
        bot.send_message(message.chat.id, "O Tarot é um sistema de leitura de cartas que utiliza imagens e símbolos para fornecer insights e orientações sobre questões pessoais, profissionais e espirituais.\n\nJá a leitura de horóscopos é uma forma de adivinhação que utiliza a posição dos astros no momento do nascimento de uma pessoa para prever aspectos da sua personalidade e eventos da sua vida.")
    elif message.text == "Consultar meu horóscopo":
        interpret_horoscope(message)
    else:
        bot.send_message(message.chat.id, "🫠 Desculpe, não consegui entender sua escolha. Por favor, selecione uma das opções no menu:", reply_markup=markup)

# Iniciando o bot
bot.polling()
