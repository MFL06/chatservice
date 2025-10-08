import tkinter as tk
from tkinter import scrolledtext, filedialog

# ----------- FUNKTIONER -----------
def send_message():
    msg = msg_entry.get()
    if msg:
        chat_box.insert(tk.END, f"Dig: {msg}\n")
        msg_entry.delete(0, tk.END)
        # Her kan I tilføje: send_besked_til_server(msg)

def send_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        filename = filepath.split("/")[-1]
        chat_box.insert(tk.END, f"[Fil valgt] {filename}\n")
        # Her kan I tilføje: send_fil_til_server(filepath)

def connect_to_server():
    chat_box.insert(tk.END, "[INFO] Forsøger at forbinde til server...\n")
    # Her kan I tilføje: opret_forbindelse()

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
                     command=send_message)
send_btn.pack(side=tk.LEFT)

# Fil- og forbindelsesknapper
file_btn = tk.Button(root, text="📎 Send fil", command=send_file, bg="#e0e0e0")
file_btn.pack(pady=5)

connect_btn = tk.Button(root, text="🔌 Forbind til server", command=connect_to_server, bg="#e0e0e0")
connect_btn.pack(pady=5)

# Start GUI
root.mainloop()
