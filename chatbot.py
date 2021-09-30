from chatterbot.trainers import ListTrainer # método responsável por permitir que uma lista de strings seja utilizada no processo de treinamento
from chatterbot import ChatBot # Construtor da classe

bot = ChatBot('roboTI', logic_adapters=['chatterbot.logic.BestMatch']) #instancia um objeto da classe chatbot

conversa = ListTrainer(bot)
conversa.train(['Oi', 'Olá eu sou o RoboTI o seu assistente em problemas de TI', 'Tudo bem?',
            'Tudo ótimo, ficara melhor se eu puder lhe ajudar', 'Estou com problemas', 'Descreva melhor o que ocorre',
                'Impressora', 'Sua impressora está com problemas... Ja verificou os cabos de energia e dados?'])
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
