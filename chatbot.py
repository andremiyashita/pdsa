from chatterbot.trainers import ListTrainer # método responsável por permitir que uma lista de strings seja utilizada no processo de treinamento
from chatterbot import ChatBot # Construtor da classe
import pandas as pd

data = open('treinamento_inicial.txt')
data = data.readlines()
treinamento = []
for item in data:
    treinamento.append(item)

bot = ChatBot('roboTI', logic_adapters=['chatterbot.logic.BestMatch']) #instancia um objeto da classe chatbot

conversa = ListTrainer(bot)
conversa.train(treinamento)
#Cria os itens iniciais de treinamento

# bot.set_trainer(ListTrainer) #Configura para que seja passado como treinamento o array
# bot.train(conversa) # Realiza o treinamento inicial com o array

#Cria um laço para que o bot interaja com o usuário

while True:
    pergunta = input('Usuário: ')
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('RoboTI: ', resposta)
    else:
        print('Hmmm lamento, mas ainda não entendi direito')
