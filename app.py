import tkinter as tk
import requests

API_URL = "http://10.74.68.152:8000"

user_name = "" # starts empty until login or signup

# ---------- FUNCTIONS ----------
def send_message_gui():
    sender = fra_var.get()
    receiver = til_var.get()
    message = message_var.get()

    if not sender or not receiver or not message:
        print("Please fill all fields.")
        return

    try:
        response = requests.post(
            f"{API_URL}/send_message",
            json={
                "message": message,
                "reciever": receiver,
                "sender": sender
            }
        )
        if response.status_code == 200:
            print("Message sent:", response.text)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Could not reach server:", e)


# ---------- GUI ----------
root = tk.Tk()
root.geometry("600x300")
root.title("Message Sender")

fra_var = tk.StringVar()
til_var = tk.StringVar()
message_var = tk.StringVar()

tk.Label(root, text="From:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=fra_var, width=25).grid(row=0, column=1, pady=5)

tk.Label(root, text="To:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=til_var, width=25).grid(row=1, column=1, pady=5)

tk.Label(root, text="Message:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=message_var, width=40).grid(row=2, column=1, pady=5)

tk.Button(root, text="Send", command=send_message_gui, width=20).grid(row=3, column=1, pady=15)

root.mainloop()
