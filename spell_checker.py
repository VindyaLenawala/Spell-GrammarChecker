from Levenshtein import distance as levenshtein_distance

DICTIONARY_FILE = "dictionary.txt"

# Sort the dictionary file
def sort_dictionary_file():
    try:
        with open(DICTIONARY_FILE, 'r', encoding='utf-8') as file:
            words = file.readlines()

        # Remove duplicates and sort
        sorted_words = sorted(set(word.strip() for word in words if word.strip()))

        # Write back sorted words
        with open(DICTIONARY_FILE, 'w', encoding='utf-8') as file:
            for word in sorted_words:
                file.write(word + '\n')

    except FileNotFoundError:
        open(DICTIONARY_FILE, 'w').close()

# Load dictionary
def load_dictionary():
    with open(DICTIONARY_FILE, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file if word.strip())

# Spell checker using Levenshtein distance
def spell_checker(word, dictionary):
    suggestions = []
    for dict_word in dictionary:
        dist = levenshtein_distance(word, dict_word)
        if dist <= 2:  # Allow up to 2 edits
            suggestions.append(dict_word)
    return suggestions
