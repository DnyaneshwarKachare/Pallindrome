
import tkinter as tk
from tkinter import messagebox
from collections import deque


# ================= FUNCTIONS =================

def check_stack():
    text = entry.get().strip()

    if text == "":
        messagebox.showwarning("Input Required", "Please enter a word or string.")
        return

    stack = []

    # Push characters into stack
    for ch in text:
        stack.append(ch)

    reverse = ""

    # Pop characters from stack
    while stack:
        reverse += stack.pop()

    if text.lower() == reverse.lower():
        result_label.config(
            text="✓ PALINDROME",
            fg="#00e676"
        )
    else:
        result_label.config(
            text="✗ NOT A PALINDROME",
            fg="#ff5252"
        )

    process_label.config(
        text=f"Original : {text}\n"
             f"Reverse  : {reverse}\n\n"
             f"Stack follows: LIFO (Last In First Out)"
    )


def check_queue():
    text = entry.get().strip()

    if text == "":
        messagebox.showwarning("Input Required", "Please enter a word or string.")
        return

    queue = deque()

    # Enqueue characters
    for ch in text:
        queue.append(ch)

    reverse = ""

    # Remove characters from queue
    while queue:
        reverse += queue.pop()

    if text.lower() == reverse.lower():
        result_label.config(
            text="✓ PALINDROME",
            fg="#00e676"
        )
    else:
        result_label.config(
            text="✗ NOT A PALINDROME",
            fg="#ff5252"
        )

    process_label.config(
        text=f"Original : {text}\n"
             f"Reverse  : {reverse}\n\n"
             f"Queue follows: FIFO (First In First Out)"
    )


def clear_all():
    entry.delete(0, tk.END)
    result_label.config(
        text="Result will appear here",
        fg="#ffffff"
    )
    process_label.config(
        text="Choose Stack or Queue to check your string."
    )


# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("Palindrome Checker | Stack & Queue")
root.geometry("850x650")
root.resizable(False, False)

# Background
root.configure(bg="#101820")


# ================= HEADER =================

header = tk.Frame(
    root,
    bg="#101820"
)
header.pack(fill="x", pady=(25, 5))

title = tk.Label(
    header,
    text="PALINDROME CHECKER",
    font=("Segoe UI", 28, "bold"),
    bg="#101820",
    fg="#00e5ff"
)
title.pack()

subtitle = tk.Label(
    header,
    text="Implementation using Stack & Queue",
    font=("Segoe UI", 12),
    bg="#101820",
    fg="#b0bec5"
)
subtitle.pack(pady=5)


# ================= INPUT CARD =================

input_card = tk.Frame(
    root,
    bg="#1b2838",
    highlightbackground="#26394d",
    highlightthickness=1
)
input_card.pack(
    padx=80,
    pady=25,
    fill="x"
)

input_title = tk.Label(
    input_card,
    text="Enter Word or String",
    font=("Segoe UI", 14, "bold"),
    bg="#1b2838",
    fg="#ffffff"
)
input_title.pack(pady=(20, 10))

entry = tk.Entry(
    input_card,
    font=("Segoe UI", 18),
    width=35,
    justify="center",
    bg="#26394d",
    fg="#ffffff",
    insertbackground="#00e5ff",
    relief="flat"
)
entry.pack(
    ipady=10,
    pady=(0, 20)
)

# Press Enter to check using Stack
entry.bind("<Return>", lambda event: check_stack())


# ================= BUTTONS =================

button_frame = tk.Frame(
    root,
    bg="#101820"
)
button_frame.pack(pady=5)

stack_button = tk.Button(
    button_frame,
    text="STACK",
    font=("Segoe UI", 12, "bold"),
    width=18,
    height=2,
    bg="#00bcd4",
    fg="#ffffff",
    activebackground="#00acc1",
    activeforeground="#ffffff",
    relief="flat",
    cursor="hand2",
    command=check_stack
)
stack_button.grid(row=0, column=0, padx=10)

queue_button = tk.Button(
    button_frame,
    text="QUEUE",
    font=("Segoe UI", 12, "bold"),
    width=18,
    height=2,
    bg="#7c4dff",
    fg="#ffffff",
    activebackground="#651fff",
    activeforeground="#ffffff",
    relief="flat",
    cursor="hand2",
    command=check_queue
)
queue_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Segoe UI", 12, "bold"),
    width=18,
    height=2,
    bg="#455a64",
    fg="#ffffff",
    activebackground="#37474f",
    activeforeground="#ffffff",
    relief="flat",
    cursor="hand2",
    command=clear_all
)
clear_button.grid(row=0, column=2, padx=10)


# ================= RESULT CARD =================

result_card = tk.Frame(
    root,
    bg="#1b2838"
)
result_card.pack(
    padx=80,
    pady=25,
    fill="x"
)

result_title = tk.Label(
    result_card,
    text="RESULT",
    font=("Segoe UI", 11, "bold"),
    bg="#1b2838",
    fg="#90a4ae"
)
result_title.pack(pady=(15, 5))

result_label = tk.Label(
    result_card,
    text="Result will appear here",
    font=("Segoe UI", 22, "bold"),
    bg="#1b2838",
    fg="#ffffff"
)
result_label.pack(pady=5)

process_label = tk.Label(
    result_card,
    text="Choose Stack or Queue to check your string.",
    font=("Segoe UI", 11),
    bg="#1b2838",
    fg="#b0bec5",
    justify="center"
)
process_label.pack(pady=(5, 20))


# ================= FOOTER =================

footer = tk.Label(
    root,
    text="DSA Mini Project • Stack & Queue",
    font=("Segoe UI", 9),
    bg="#101820",
    fg="#607d8b"
)
footer.pack(side="bottom", pady=12)


# ================= START APPLICATION =================

root.mainloop()

