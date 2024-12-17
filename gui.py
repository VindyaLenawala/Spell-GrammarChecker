import tkinter as tk
from tkinter import messagebox
from spell_checker import spell_checker, load_dictionary, sort_dictionary_file
from grammar_checker import grammar_checker

# Function to process input text
def process_text():
    input_text = text_input.get("1.0", tk.END).strip()
    dictionary = load_dictionary()
    words = input_text.split()

    corrected_words = []
    spell_errors = []
    grammar_errors = []

    # Spell Checking
    for word in words:
        if word not in dictionary:
            suggestions = spell_checker(word, dictionary)
            if suggestions:
                corrected_words.append(suggestions[0])  # Auto-correct to first suggestion
                spell_errors.append(f"'{word}' corrected to '{suggestions[0]}'")
            else:
                corrected_words.append(word)
        else:
            corrected_words.append(word)

    # Grammar Checking
    grammar_errors = grammar_checker(input_text)

    # Display Results
    corrected_text = " ".join(corrected_words)
    spell_output.config(state='normal')
    spell_output.delete("1.0", tk.END)
    spell_output.insert(tk.END, corrected_text)
    spell_output.config(state='disabled')

    errors_output.config(state='normal')
    errors_output.delete("1.0", tk.END)
    if spell_errors or grammar_errors:
        errors_output.insert(tk.END, "Spell Errors:\n" + "\n".join(spell_errors) + "\n\n")
        errors_output.insert(tk.END, "Grammar Errors:\n" + "\n".join(grammar_errors))
    else:
        errors_output.insert(tk.END, "No errors found.")
    errors_output.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("Sinhala Grammar and Spell Checker")

# Input Text Area
tk.Label(root, text="Enter Text:").pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Process Button
process_button = tk.Button(root, text="Check Text", command=process_text)
process_button.pack()

# Corrected Text Output
tk.Label(root, text="Corrected Text:").pack()
spell_output = tk.Text(root, height=5, width=50, state='disabled', bg="#e8e8e8")
spell_output.pack()

# Errors Output
tk.Label(root, text="Errors and Suggestions:").pack()
errors_output = tk.Text(root, height=10, width=50, state='disabled', bg="#f8d7da")
errors_output.pack()

# Sort dictionary on startup
sort_dictionary_file()

# Run the GUI
root.mainloop()
