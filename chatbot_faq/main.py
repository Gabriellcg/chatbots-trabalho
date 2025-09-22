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