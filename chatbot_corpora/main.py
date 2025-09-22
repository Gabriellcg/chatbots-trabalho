from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("CorporaBot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")

while True:
    pergunta = input("Você: ").strip().lower()
    if pergunta in ["sair", "exit", "parar", "tchau"]:
        print("Bot: Até mais! Encerrando o chatbot.")
        break
    resposta = chatbot.get_response(pergunta)
    print("Bot:", resposta)