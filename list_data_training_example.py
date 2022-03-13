from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


'''
This is an example showing how to train a chat bot using the
ChatterBot ListTrainer.
'''

chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ListTrainer(chatbot)

trainer.train("data/text.json")


# Now let's get a response to a greeting
while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Bot: ", response)
