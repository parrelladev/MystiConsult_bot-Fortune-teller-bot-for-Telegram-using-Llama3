import telebot
from telebot import types

from config.settings import TELEGRAM_TOKEN
from services.tarot_service import generate_cards, generate_response
from services.horoscope_service import generate_response_horoscope
from config.messages import BOT_MESSAGES

# Inicializa o bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Dicionário para armazenar o estado do usuário
user_states = {}


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """
    Comando /start: mostra o menu principal.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tarot_btn = types.KeyboardButton("Tarot")
    horoscope_btn = types.KeyboardButton("Horoscopo")
    info_btn = types.KeyboardButton("Sobre o Bot")
    markup.add(tarot_btn, horoscope_btn, info_btn)

    bot.send_message(message.chat.id, BOT_MESSAGES["welcome"], reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    """
    Handler principal de mensagens de texto.
    """
    chat_id = message.chat.id
    text = message.text

    # Usuário está digitando a pergunta para o Tarot
    if user_states.get(chat_id) == "waiting_tarot_question":
        user_states[chat_id] = None


        # Gera as cartas e a interpretação
        cards = generate_cards()  # retorna uma lista de strings (ver TAROT_CARDS)
        cards_message = "\n".join([f"- {card}" for card in cards])

        # Mostra as cartas sorteadas para o usuário
        bot.send_message(
            chat_id,
            f"As cartas sorteadas foram:\n{cards_message}",
            parse_mode="Markdown",
        )

        bot.send_message(chat_id, BOT_MESSAGES["reading_cards"])

        response = generate_response(text, cards_message)

        # Envia a resposta
        bot.send_message(chat_id, response, parse_mode="Markdown")
        bot.send_message(chat_id, BOT_MESSAGES["end_consultation"])
        return

    # Usuário está escolhendo um signo
    if user_states.get(chat_id) == "waiting_zodiac_sign":
        valid_signs = [
            "Áries",
            "Touro",
            "Gêmeos",
            "Câncer",
            "Leão",
            "Virgem",
            "Libra",
            "Escorpião",
            "Sagitário",
            "Capricórnio",
            "Aquário",
            "Peixes",
        ]

        if text not in valid_signs:
            bot.send_message(chat_id, BOT_MESSAGES["invalid_zodiac"])
            return

        user_states[chat_id] = None
        bot.send_message(chat_id, BOT_MESSAGES["consulting_stars"])

        # Gera o horóscopo
        response = generate_response_horoscope(text)

        # Envia a resposta
        bot.send_message(chat_id, response, parse_mode="Markdown")
        bot.send_message(chat_id, BOT_MESSAGES["end_consultation"])
        return

    # Handler para os botões do menu
    if text == "Tarot":
        user_states[chat_id] = "waiting_tarot_question"
        bot.send_message(chat_id, BOT_MESSAGES["tarot_question"])

    elif text == "Horoscopo":
        user_states[chat_id] = "waiting_zodiac_sign"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        signs = [
            "Áries",
            "Touro",
            "Gêmeos",
            "Câncer",
            "Leão",
            "Virgem",
            "Libra",
            "Escorpião",
            "Sagitário",
            "Capricórnio",
            "Aquário",
            "Peixes",
        ]
        markup.add(*[types.KeyboardButton(sign) for sign in signs])
        bot.send_message(chat_id, BOT_MESSAGES["horoscope_choice"], reply_markup=markup)

    elif text == "Sobre o Bot":
        bot.send_message(chat_id, BOT_MESSAGES["bot_info"])
        bot.send_message(chat_id, BOT_MESSAGES["about_tarot"])

    else:
        bot.send_message(chat_id, BOT_MESSAGES["invalid_choice"])


if __name__ == "__main__":
    print("Bot iniciado!")
    bot.polling(none_stop=True)
