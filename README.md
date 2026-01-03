# PyQuizzer

A command-line Python quiz application that loads questions from a JSON file and quizzes the user interactively with multiple-choice and true/false questions.

## Features
- Loads questions from an external JSON file.
- Supports multiple-choice and true/false question types.
- Tracks user score and provides feedback.
- Randomizes questions and answer options.

## Requirements
- Python 3.x

## Setup

1. Clone this repository or download `PyQuizzer.py` and `questions.json`.
2. Run the quiz script:
 
   ```bash
   python PyQuizzer.py
How to Add Questions

Edit the questions.json file. Each question should have:

"question": The question text.

"type": Either "multiple_choice" or "true_false".

"options": (Only for multiple_choice) List of possible answers.

"answer": The correct answer as a string.

Example question:

{
  "question": "What is 2 + 2?",
  "type": "multiple_choice",
  "options": ["3", "4", "5"],
  "answer": "4"
}

Future Improvements

Add timer for each question.

Add difficulty levels.

Save high scores.

Add GUI interface.

License

This project is open-source and free to use.

## Future Improvements
- Question difficulty levels
- Score persistence

---
