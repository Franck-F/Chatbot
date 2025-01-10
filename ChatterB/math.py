from chatterbot import ChatBot

bot = ChatBot("Math", logic_adapter=["chatterbot.logic.MathematicalEvaluation"])

print("--------------------------Math Chatbot--------------------------")

while True:
    user_text = input("Type the math equation that you want to solve: ")
    print("Jarvis: " + str(bot.get_response(user_text)))