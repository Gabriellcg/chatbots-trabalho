from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import yaml

# Cria o chatbot
chatbot = ChatBot("FAQ_TI")

# Carrega o arquivo YAML
with open("base_faq.yml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

# Treina com os pares de conversa
trainer = ListTrainer(chatbot)
for conversation in data["conversations"]:
    trainer.train(conversation)

# Loop de interação
while True:
    pergunta = input("Você: ").strip().lower()
    if pergunta in ["sair", "exit","parar"]:
        print("Bot: Até mais! Encerrando o chatbot.")
        break
    resposta = chatbot.get_response(pergunta)
    print("Bot:", resposta)


#from chatterbot.trainers import ListTrainer
#from chatterbot import ChatBot

#faq_bot = ChatBot('FAQBot', read_only=True)
#trainer = ListTrainer(faq_bot)

#with open ('base_faq.yml', 'r', encoding='utf-8') as f:
#    linhas = f.readline()

#    pares = [linha.strip() for linha in linhas if linha.strip()]

#    trainer.train(pares)

#while True:
#    pergunta = input("Você: ")

#    resposta = faq_bot.generate_response(pergunta)
#    print("Bot>: ", resposta)