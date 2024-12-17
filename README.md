# Sinhala Grammar and Spell Checker

This is a Sinhala language grammar and spell-checking tool that uses **Levenshtein Distance** for spell correction and rule-based grammar checking. The tool features a simple graphical interface built with Tkinter.

## Features:
- **Spell Checking**:
  - Corrects spelling errors based on a predefined Sinhala dictionary.
  - The dictionary file is maintained in ascending order and duplicates are removed on startup.
- **Grammar Checking**:
  - Detects and corrects grammar mistakes related to subject-verb agreement for **singular** and **plural** subjects:
    - **Singular subject "මම"**: The verb should end with "මි".
    - **Plural subject "අපි"**: The verb should end with "මු".
- **Graphical User Interface**:
  - Allows users to input paragraphs.
  - Displays both **auto-corrections** for spelling and **suggestions** for grammar issues.

---

## Setup Instructions:

Follow these steps to set up and run the project.

### 1. **Clone the Repository**

### 2. **Install Dependencies**:
pip install -r requirements.txt

### 3. **Run the programe**:
python main.py