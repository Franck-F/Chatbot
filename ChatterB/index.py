#Today’s tutorial demonstrates how to build your own chatbot using Python!
# Chatbots are one of the most popular applications of artificial intelligence.
# Chatbots are software that utilizes AI and NLP to guide a human to the desired
# outcome as a response to what they want. Chatbots are found in tremendous amounts
# on websites, for customer support, on social media, in applications and countless 
# other platforms.


from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Jarvis", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

list_to_train = {
    "hi",
    "hi there",
    "what's your name?",
    "I'm a chabot",
    "how old are you?",
    "I'm ageless!"
}
list_trainer = ListTrainer(bot)

list_trainer.train()

user_response = input("user: ")
bot_response = printbot.get_response(user_response)