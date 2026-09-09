"""
Simple Quiz App
----------------
A multiple-choice quiz game that tracks your score
and saves your best score to a file.
"""

import json
import os
import random

HIGH_SCORE_FILE = "high_score.json"

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is this quiz written in?",
        "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
        "answer": "B"
    },
    {
        "question": "What does 'len()' do in Python?",
        "options": ["A) Deletes a list", "B) Returns length", "C) Sorts a list", "D) Adds items"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) /* */"],
        "answer": "C"
    },
    {
        "question": "What data type is used for True/False values?",
        "options": ["A) int", "B) str", "C) bool", "D) float"],
        "answer": "C"
    },
]


def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            return json.load(f).get("high_score", 0)
    return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        json.dump({"high_score": score}, f)


def run_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    score = 0

    print("\n=== QUIZ TIME ===")
    print(f"Answer {len(questions)} questions. Type A, B, C, or D.\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(f"   {option}")

        answer = input("Your answer: ").strip().upper()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"You scored {score}/{len(questions)}")
    return score, len(questions)


def main():
    high_score = load_high_score()
    print(f"Current high score: {high_score}")

    while True:
        score, total = run_quiz()

        if score > high_score:
            print("🎉 New high score!")
            high_score = score
            save_high_score(high_score)
        else:
            print(f"High score remains: {high_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()