from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import pandas as pd

arquivo_de_treinamento = 'treinamento_inicial.txt'
bot = ChatBot('roboTI', logic_adapters=['chatterbot.logic.BestMatch'])

def get_lista_treinamento(caminho_arquivo):
    """Esta função define como o bot será treinado a partir de uma dada lista."""
    treinamento = []
    try:
        data = open('treinamento_inicial.txt')
        with open(lista, 'r', encoding='utf8', errors='ignore') as data:
            for item in data.readlines():
                treinamento.append(item)
    except Exception:
        pass

    return treinamento

def treina_bot(lista_treinamento):
    conversa = ListTrainer(bot)
    conversa.train(lista_treinamento)


if __name__ == "__main__":

    lista_treinamento = get_lista_treinamento(arquivo_de_treinamento)
    try:
        treina_bot(lista_treinamento)
    except Exception:
        pass
    while True:
        try:
            pergunta = input('Usuário: ')
        except Exception:
            pass
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.5:
            print('RoboTI: ', resposta)
        else:
            print('Hmmm lamento, mas ainda não entendi direito')
