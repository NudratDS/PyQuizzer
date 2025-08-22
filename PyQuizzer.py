import json
import random

# JSON file to load questions from
QUESTIONS_FILE = 'questions.json'

def load_questions(filename):
    """Load quiz questions from a JSON file."""
    try:
        with open(filename, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Questions file '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")
        return []

def ask_question(q):
    """Ask a single question and return True if answered correctly."""
    print("\n" + q['question'])
    
    if q['type'] == 'multiple_choice':
        options = q['options']
        # Shuffle options so the answer is not always in the same place
        random.shuffle(options)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                answer = int(input("Your answer (number): "))
                if 1 <= answer <= len(options):
                    break
                else:
                    print("Invalid option number.")
            except ValueError:
                print("Please enter a number.")

        # Check if the selected option matches the correct answer
        if options[answer - 1] == q['answer']:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
            return False

    elif q['type'] == 'true_false':
        while True:
            answer = input("Your answer (True/False): ").strip().lower()
            if answer in ['true', 'false', 't', 'f']:
                break
            else:
                print("Please answer True or False.")
        correct_answer = q['answer'].lower()
        if answer.startswith(correct_answer[0]):
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
            return False
    else:
        print("Unknown question type.")
        return False

def run_quiz():
    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        return

    print(f"Loaded {len(questions)} questions.")
    score = 0
    total = len(questions)

    # Shuffle questions for randomness
    random.shuffle(questions)

    for q in questions:
        if ask_question(q):
            score += 1

    print(f"\nQuiz complete! Your score: {score} / {total}")
    percent = (score / total) * 100
    print(f"Percentage: {percent:.2f}%")

def main():
    print("--- Welcome to PyQuizzer ---")
    run_quiz()
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
