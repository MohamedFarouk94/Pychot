import tkinter as tk
import threading
import asyncio
import argparse
from tkinter import scrolledtext
from set import OUTPUT_Q
from get import INPUT_Q
from client import main


GLOBAL_COUNTER = 0


def parse_args():
    parser = argparse.ArgumentParser(description="Run the chat GUI with authentication.")
    parser.add_argument('username', type=str, help='Username for authentication')
    parser.add_argument('password', type=str, help='Password for authentication')
    return parser.parse_args()


def on_send():
    message = input_field.get()
    INPUT_Q.append(message)
    # print(f'"{message}" is appended successfully in INPUT_Q')
    input_field.delete(0, tk.END)


def run_asyncio_loop(ARG):
    asyncio.set_event_loop(asyncio.new_event_loop())  # Create a new event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ARG)


async def check_incoming_messages():
    global GLOBAL_COUNTER

    while True:
        while not OUTPUT_Q:
            await asyncio.sleep(0.1)
        # print("SOMETHING FOUND IN OUTPUT_Q")
        response = OUTPUT_Q.pop(0)
        response = eval(response)
        username = response['username']
        message = response['message']
        username = 'You' if username == args.username else username
        color = 'blue' if username == 'You' else 'red'
        chat_box.tag_configure(f'message_tag_{GLOBAL_COUNTER}', foreground=color)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f'{username}: {message}\n', f'message_tag_{GLOBAL_COUNTER}')
        chat_box.config(state=tk.DISABLED)
        GLOBAL_COUNTER += 1


# Getting username and password
args = parse_args()
print(args.username)

# Create the main window
root = tk.Tk()
root.title(f'room1 - {args.username}')

# Create a scrollable text box (read-only)
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a frame to hold the input field and button
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10, fill=tk.X)

# Create the input field
input_field = tk.Entry(input_frame, width=80)
input_field.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill=tk.X)

# Create the send button
send_button = tk.Button(input_frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT)

# Start the asyncio loop in a separate thread
thread1 = threading.Thread(target=run_asyncio_loop, args=(check_incoming_messages(),), daemon=True)
thread1.start()

# Running client.main()
thread2 = threading.Thread(target=asyncio.run, args=(main(args.username, args.password),), daemon=True)
thread2.start()

# Start the Tkinter main loop
root.mainloop()
