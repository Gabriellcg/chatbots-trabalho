from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

faq_bot = ChatBot('FAQBot', read_only=True)
trainer = ListTrainer(faq_bot)

with open ('base_faq.yml', 'r', encoding='utf-8') as f:
    linhas = f.readline()

    pares = [linha.strip() for linha in linhas if linha.strip()]

    trainer.train(pares)

while True:
    pergunta = input("Você: ")

    resposta = faq_bot.generate_response(pergunta)
    print("Bot>: ", resposta)