from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Panther", storage_adapter="chatterbot.storage.mysql")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
listtrainer = ListTrainer(bot)
listtrainer.train([
    "Who is your creator", "Panther was developed by Arav Tyagi, deployed by Arav Tyagi, and maintained by the FHS "
                           "Computer Club "
])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
