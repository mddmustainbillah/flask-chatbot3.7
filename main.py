from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

app = Flask(__name__)

data = json.loads(open('data/greetings.json', 'r').read())

train = []

for k, row in enumerate(data):
    train.append(row['patterns'])
    train.append(row['responses'])

train_data = str(train)
print(train_data)

chatbot = ChatBot("TALK")

trainer = ListTrainer(chatbot)
trainer.train(train)
#
# trainer.train([
#     "Hi there", "How are you", "Is anyone there?","Hey","Hola", "Hello", "Good day",
#      "Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"
# ])


@app.route("/")
def home():
    return  render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == '__main__':
    app.run(debug=True)
