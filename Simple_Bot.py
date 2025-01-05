from tkinter import *
import datetime

root = Tk()

def send():
    send = "Me : " + message.get()
    txt.insert(END, "\n"+send)
    greet = ['Bonjour','bonjour','Hello', 'salut', 'Salut', 'Hey', 'hey','...']
    nom = ['nom','comment tu t\'appelles','c\'est quoi ton nom', '...']
    if message.get() in greet:
        txt.insert(END, "\n" + "Bot : Bonjour, comment puis-je vous aider?")
    elif 'heure' in message.get():
        heure = datetime.datetime.now().strftime("%H:%M:%S")
        txt.insert(END, "\n" + "Bot : il est " + heure)
    elif message.get() in nom:
        txt.insert(END, "\n" + "Bot : Je m'appelle Jarvis")
    
    else :
        txt.insert(END, "\n" + "Bot : Je ne comprends pas...")
    message.delete(0, END)




txt = Text(root, font=("signika", 13), fg='white', bg='black')
txt.grid(row=0, column=0, columnspan=2)
message = Entry(root, width=100)
message.grid(row=1, column=0)
send = Button(root, text="send", command=send).grid(row=1, column=1)

root.title("Jarvis")
root.mainloop()