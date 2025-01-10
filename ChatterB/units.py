from chatterbot import ChatBot

bot = ChatBot("units", logic_adapter=['chatterbot.logic.UnitConversion'])

while True:
    user_text = input("Ask a question  (unit conversion): ")
    Chatbot_response = str(bot.get_response(user_text))
    print("Jarvis: " + Chatbot_response)