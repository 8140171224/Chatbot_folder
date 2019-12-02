from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#Create a new chat bot
chatbot = ChatBot('Kano Padhiyar')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked.",
    "My name is Kano Padhiyar."
])

response = chatbot.get_response('your name')

print(response)