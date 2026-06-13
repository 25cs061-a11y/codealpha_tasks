from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Language mapping
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        if not text:
            messagebox.showwarning(
                "Warning",
                "Please enter text."
            )
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Language Translation Tool")
root.geometry("800x600")

Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold")
).pack(pady=10)

Label(root, text="Enter Text").pack()

input_text = Text(root, height=8, width=80)
input_text.pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Source Language").grid(row=0, column=0)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=20
)
source_lang.set("English")
source_lang.grid(row=1, column=0, padx=20)

Label(frame, text="Target Language").grid(row=0, column=1)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=20
)
target_lang.set("Telugu")
target_lang.grid(row=1, column=1, padx=20)

Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold")
).pack(pady=20)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=8, width=80)
output_text.pack(pady=10)

root.mainloop()