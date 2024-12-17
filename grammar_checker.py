# Grammar checker for singular and plural subject verbs
def grammar_checker(text):
    corrections = []
    words = text.split()

    for i, word in enumerate(words):
        # Singular subject "මම" -> verb should end with "මි"
        if i > 0 and words[i - 1] == "මම" and not word.endswith("මි"):
            corrections.append(f"'{word}' should end with 'මි' (for singular subject 'මම')")

        # Plural subject "අපි" -> verb should end with "මු"
        if i > 0 and words[i - 1] == "අපි" and not word.endswith("මු"):
            corrections.append(f"'{word}' should end with 'මු' (for plural subject 'අපි')")

    return corrections
