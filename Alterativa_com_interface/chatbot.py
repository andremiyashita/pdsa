from chatterbot import ChatBot

#Inicializando o objeto do bot
chatbot = ChatBot(
    'RoboTI',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

from chatterbot.trainers import ListTrainer

#Carregando arquivos de treinamento
caminho_arquivo = 'treinamento_inicial.txt'
treinamento = []
try:
    with open(caminho_arquivo, 'r', encoding='utf8', errors='ignore') as data:
        for item in data.readlines():
            treinamento.append(item)
except Exception:
    pass

#Realizando o treinamento
trainer = ListTrainer(chatbot)

training_data = treinamento

trainer.train(training_data)


