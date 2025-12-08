import tkinter as tk
from tkinter import scrolledtext, filedialog

# ----------- GUI SETUP -----------
root = tk.Tk()
root.title("Chat Klient")
root.geometry("600x500")
root.configure(bg="#e6e6fa")

# Chatvisning
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="white", fg="black")
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state=tk.NORMAL)

# Indtastningsfelt + send-knapper
msg_frame = tk.Frame(root, bg="#d8bfd8")
msg_frame.pack(fill=tk.X, padx=10, pady=5)

msg_entry = tk.Entry(msg_frame, font=("Arial", 12))
msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

send_btn = tk.Button(msg_frame, text="Send", width=8, bg="#0078D7", fg="black",
                     command=)
send_btn.pack(side=tk.LEFT)

connect_btn = tk.Button(root, text="🔌 Forbind til server", command=connect_to_server, bg="#e0e0e0")
connect_btn.pack(pady=5)

# Start GUI
root.mainloop()
