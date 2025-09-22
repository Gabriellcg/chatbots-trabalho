from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datasets import load_dataset
import spacy
import logging
import os

logging.basicConfig(level=logging.INFO)

try:
    nlp = spacy.load('pt_core_news_sm')
except:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "pt_core_news_sm"])
    nlp = spacy.load('pt_core_news_sm')

print("Carregando o dataset 'daily_dialog' do Hugging Face...")
dataset = load_dataset("daily_dialog", trust_remote_code=True)

dialogos = dataset['train']['dialog']

training_data = []
limite_de_dialogos = 5000 

print(f"Processando {limite_de_dialogos} diálogos para o treinamento...")
for dialogo in dialogos[:limite_de_dialogos]:
    training_data.extend(dialogo)

print(f"Total de {len(training_data)} frases carregadas.")


db_path = "daily_dialog_bot.sqlite3"
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Banco de dados antigo '{db_path}' removido.")

chatbot = ChatBot(
    'Daily Dialog Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=f'sqlite:///{db_path}',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(chatbot)
trainer.train(training_data)

print("\nHello! I am a bot trained on daily dialogues. (type 'exit' to end)")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        bot_response = chatbot.get_response(user_input)
        print(f"Bot: {bot_response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break