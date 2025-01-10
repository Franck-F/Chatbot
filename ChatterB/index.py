#Today’s tutorial demonstrates how to build your own chatbot using Python!
# Chatbots are one of the most popular applications of artificial intelligence.
# Chatbots are software that utilizes AI and NLP to guide a human to the desired
# outcome as a response to what they want. Chatbots are found in tremendous amounts
# on websites, for customer support, on social media, in applications and countless 
# other platforms.


from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Jarvis", read_only=False,
              logic_adapters=[
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "Sorry I don't have an answer",
                      "maximum_similarity_threshold": 0.9
                  }
                  ])

list_to_train = [
    "hi",
    "hi there",
    "what's your name?",
    "I'm a chabot",
    "how old are you?",
    "I'm ageless!",
    "why are you so sad?",
    "i'm not!",
    "Do you have iphone?",
    "i've everything!",
    "what's your favorite food?",
    "I don't eat",
    "what's your job",
    "I'm here to answer your question",
    "I don't know what you're talking about"
]
list_trainer = ListTrainer(bot)

list_trainer.train()

while True:
    user_response = input("user: ")
    print("Jarvis: " + str(bot.get_response(user_response)))