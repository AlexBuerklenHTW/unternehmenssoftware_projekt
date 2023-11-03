import tkinter as tk
from tkinter import Text, Scrollbar
import openai

# Set your OpenAI API key here
file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

root = tk.Tk()
root.title("ChatGPT Chat GUI")

# Create a frame for the chat
chat_frame = tk.Frame(root)
chat_frame.grid(row=0, column=0, padx=10, pady=10)

# Create a label for Person 1
left_person_label = tk.Label(chat_frame, text="Person 1", font=("Arial", 12, "bold"))
left_person_label.grid(row=0, column=0, sticky='w')

# Create a Text widget for the speech bubbles
chat_history = Text(chat_frame, height=10, width=40, wrap=tk.WORD)
chat_history.grid(row=1, column=0, columnspan=2, sticky='w')
chat_history.config(state=tk.DISABLED)

# Create a log section
log_frame = tk.Frame(root)
log_frame.grid(row=1, column=0, padx=10, pady=10)

log_label = tk.Label(log_frame, text="Chat Log", font=("Arial", 12, "bold"))
log_label.pack()

log_text = Text(log_frame, height=10, width=40, wrap=tk.WORD)
log_text.pack()

log_scrollbar = Scrollbar(log_frame, command=log_text.yview)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=log_scrollbar.set)
log_text.config(state=tk.DISABLED)

# Function to update the chat history
def update_chat_history(sender, message):
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"{sender}: {message}\n\n")
    chat_history.see(tk.END)
    chat_history.config(state=tk.DISABLED)

# Function to log a message
def log_message(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)
    log_text.config(state=tk.DISABLED)

# Function to send a message and get a response from the ChatGPT API
def send_message(event=None):
    message = user_input.get()
    if message:
        update_chat_history("Person 1", message)
        user_input.delete(0, tk.END)

        # Make a request to the ChatGPT API
        response = generate_response(message)
        update_chat_history("Person 2", response)

        log_message(f"Person 1: {message}")
        log_message(f"Person 2: {response}")

# Function to interact with the ChatGPT API
def generate_response(message):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Person 1: {message}\nPerson 2:",
            max_tokens=50,  # Adjust as needed
            stop=None  # You can specify stop conditions
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Create an input field for sending messages
user_input = tk.Entry(chat_frame, width=40)
user_input.grid(row=2, column=0, sticky='w')
user_input.bind("<Return>", send_message)

# Create a button to send messages
send_button = tk.Button(chat_frame, text="Send", command=send_message)
send_button.grid(row=2, column=1, sticky='e')

# Start the main loop
root.mainloop()