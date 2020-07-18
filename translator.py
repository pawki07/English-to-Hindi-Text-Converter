import tkinter as tk
from googletrans import Translator

root = tk.Tk()
root.configure(background="green")
root.title("Translator")
root.geometry("300x150")

#Functions
def translation():
    word = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation1 = translator.translate(word, dest = "hi")
    label1 = tk.Label(root, text = f"Translated In Hindi: {translation1.text}", bg="yellow")
    label1.grid(row=2, column=0, sticky="nesw", pady=15)

label = tk.Label(root, text="Enter Text: ")
label.grid(row=0, column=0, sticky="w", padx=32, pady=10)

entry = tk.Entry(root)
entry.grid(row=1, column=0, ipadx=15, padx=33)

button = tk.Button(root, text="Translate", command=translation)
button.grid(row=1, column=2)

root.mainloop()