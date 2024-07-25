import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Extended language mapping dictionary
language_map = {
    "english": "en",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "kannada": "kn",
    "chinese": "zh-cn",
    "japanese": "ja",
    "hindi": "hi",
    "portuguese": "pt",
    "russian": "ru",
    "arabic": "ar",
    "bengali": "bn",
    "turkish": "tr",
    "italian": "it",
    "dutch": "nl",
    "swedish": "sv",
    "norwegian": "no",
    "danish": "da",
    "polish": "pl",
    "czech": "cs",
    "greek": "el",
    "hebrew": "he",
    "thai": "th",
    "vietnamese": "vi",
    "indonesian": "id",
    "malay": "ms",
    "filipino": "tl",
    "ukrainian": "uk",
    "serbian": "sr",
    "croatian": "hr",
    "slovak": "sk",
    "estonian": "et",
    "latvian": "lv",
    "lithuanian": "lt",
    "swahili": "sw",
    "hungarian": "hu",
    "finnish": "fi",
    "irish": "ga",
    "scottish": "gd",
    "welsh": "cy",
    "catalan": "ca",
    "basque": "eu",
    "galician": "gl",
    "latin": "la"
}

def get_language_code(language_name):
    return language_map.get(language_name.lower(), None)

def translate_text():
    # Get the input text
    text = original_text.get("1.0", tk.END).strip()
    
    # Get the target language
    target_language = target_language_var.get()
    target_language_code = get_language_code(target_language)
    
    if not target_language_code:
        translated_text.set("Sorry, the language is not supported.")
        return

    # Perform the translation
    try:
        translated = translator.translate(text, dest=target_language_code)
        translated_text.set(translated.text)
    except Exception as e:
        translated_text.set(f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Text Translator")

# Create and place widgets
tk.Label(root, text="Enter text to translate:").pack(pady=10)
original_text = tk.Text(root, height=10, width=50)
original_text.pack(pady=10)

tk.Label(root, text="Select target language:").pack(pady=10)
target_language_var = tk.StringVar()
target_language_menu = ttk.Combobox(root, textvariable=target_language_var)
target_language_menu['values'] = list(language_map.keys())
target_language_menu.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

tk.Label(root, text="Translated text:").pack(pady=10)
translated_text = tk.StringVar()
translated_text_box = tk.Entry(root, textvariable=translated_text, width=50)
translated_text_box.pack(pady=10)

# Start the GUI event loop
root.mainloop()
