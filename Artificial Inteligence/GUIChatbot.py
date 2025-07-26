from tkinter import Tk, Text, Entry, Button, END

# Function to handle user input and generate bot response
def send():
    user_message = e.get()
    text.insert(END, "\nYou: " + user_message)

    # Predefined responses
    if user_message.lower() == 'hi':
        text.insert(END, "\nBot: hello")
    elif user_message.lower() == 'hello':
        text.insert(END, "\nBot: hi")
    elif user_message.lower() == 'how are you?':
        text.insert(END, "\nBot: I'm fine, and you?")
    elif user_message.lower() == 'Im fine too':
        text.insert(END, "\nBot: Nice to hear that")
    else:
        text.insert(END, "\nBot: Sorry, I didn't get it.")

# GUI setup
root = Tk()
root.title('Simple Python Chatbot')

# Chat display area
text = Text(root, bg='light blue', width=80, height=20)
text.grid(row=0, column=0, columnspan=2)

# User input field
e = Entry(root, width=80)
e.grid(row=1, column=0)

# Send button
send_btn = Button(root, text='Send', bg='blue', fg='white', width=20, command=send)
send_btn.grid(row=1, column=1)

# Start the GUI event loop
root.mainloop()