quiz_questions = {
    "Which of the following is an example of open-source software?": {
        "A": "Microsoft windows",
        "B": "Adobe photoshop",
        "C": "Linux",
        "D": "Apple macOS",
        "Answer": "C"
    },
    "What is the term for the  processing of finding and fixing errors in software code?": {
        "A": "debugging",
        "B": "testing",
        "C": "deployment",
        "D": "maintenance",
        "Answer": "A"
    },
    " Which programming language is known for its use in web development and is often used for client- side scripting?": {
        "A": "java",
        "B": "python",
        "C": "java script",
        "D": "C++",
        "Answer": "C"
    }
}

def quiz():
    score = 0
    for question, options in quiz_questions.items():
        print(question)
        for option, value in options.items():
            if option != "Answer":
                print(f"{option}: {value}")
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == options["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {options['Answer']}.\n")
    print(f"Quiz over! Your final score is {score} out of {len(quiz_questions)}.")

if __name__ == "__main__":
    quiz()
