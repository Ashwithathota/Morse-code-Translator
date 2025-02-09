import tkinter as tk
from tkinter import ttk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ':': '---...', ';': '-.-.-.',
    "'": '.----.', '"': '.-..-.', '[': '.-..-.', ']': '-.-.--',
    '{': '.-..-.', '}': '-.-.--', '!': '-.-.--', '@': '.--.-.',
    '#': '......', '$': '...-..-', '%': '-----', '^': '......',
    '&': '.-...', '*': '......', '_': '..--.-', '+': '.-.-.',
    '=': '-...-', '\\': '.-..-.', '|': '.-..-.', '<': '.-..-.',
    '>': '.-..-.'
}

def convert_to_morse(text):
    """Converts text to Morse code."""
    morse_code = ""
    for letter in text.upper():
        if letter != " ":
            morse_code += MORSE_CODE_DICT.get(letter, ".") + " "
        else:
            morse_code += " / "
    return morse_code.strip()

def convert_to_english(morse):
    """Converts Morse code to text."""
    english_text = ""
    morse_words = morse.split(" / ")
    for word in morse_words:
        morse_letters = word.split()
        for letter in morse_letters:
            for key, value in MORSE_CODE_DICT.items():
                if value == letter:
                    english_text += key
        english_text += " "
    return english_text.strip()

# --- Tkinter GUI Setup ---

window = tk.Tk()
window.title("Morse Code Translator")
window.configure(bg='lightgreen')

# Heading
heading_label = tk.Label(window, text="Welcome to Morse Code Translator", bg='gray', font=('Arial', 12))
heading_label.grid(row=0, column=1, padx=10, pady=10)

# Input Field
input_label = tk.Label(window, text="One Language", bg='orange')
input_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
input_text = tk.Text(window, height=5, width=40)
input_text.grid(row=1, column=1, padx=5, pady=5)
input_text.insert(tk.END, " ")

# Language Selection
from_label = tk.Label(window, text="From Language", bg='orange')
from_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
to_label = tk.Label(window, text="To Language", bg='orange')
to_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')

from_language = ttk.Combobox(window)
from_language['values'] = ("Text", "Morse")
from_language.grid(row=2, column=1, padx=5, pady=5)
from_language.current(0)  # Set default value

to_language = ttk.Combobox(window)
to_language['values'] = ("Morse", "Text")
to_language.grid(row=3, column=1, padx=5, pady=5)
to_language.current(1)  # Set default value

# Output Field
output_label = tk.Label(window, text="Converted Language", bg='orange')
output_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
output_text = tk.Text(window, height=5, width=40)
output_text.grid(row=5, column=1, padx=5, pady=5)

# Buttons
def translate():
    input_data = input_text.get("1.0", tk.END).strip()
    from_lang = from_language.get()
    to_lang = to_language.get()

    if from_lang == to_lang:
        output_data = "Please select different languages for translation."
    elif from_lang == "Text" and to_lang == "Morse":
        output_data = convert_to_morse(input_data)
    elif from_lang == "Morse" and to_lang == "Text":
        output_data = convert_to_english(input_data)
    else:
        output_data = "Invalid selection. Please check the language selection."

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output_data)

def clear_output():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

convert_button = tk.Button(window, text="Convert", command=translate, bg='blue', fg='white')
convert_button.grid(row=4, column=1, padx=5, pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_output, bg='pink')
clear_button.grid(row=6, column=1, padx=5, pady=5)

# Start the GUI
window.mainloop()

