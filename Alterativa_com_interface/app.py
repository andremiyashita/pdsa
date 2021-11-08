from chatbot import chatbot

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    resposta = bot.get_response(userText)
    if float(resposta.confidence) > 0.5:
       return str(resposta)
    else:
        resposta = 'Hmmm lamento, mas ainda não entendi direito'
        return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
