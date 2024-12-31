import random
import time
from colorama import Fore

def generate_question():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    random_operator = random.choice(['+', '-', '*'])
    return num1, num2, random_operator

def check_answer(answer, num1, num2, random_operator):
    if random_operator == '+':
        correct_answer = num1 + num2
    elif random_operator == '-':
        correct_answer = num1 - num2
    elif random_operator == '*':
        correct_answer = num1 * num2

    return float(answer) == correct_answer

def timer_and_score():
    print("Are you asian enough??")
    time.sleep(0.5)
    print("Starting the quiz...")
    time.sleep(1)
    start_time = time.time()
    num_correct = 0
    num_questions = 60
    question_idx = 1

    for _ in range(num_questions):
        num1, num2, random_operator = generate_question()

        print(f"{Fore.WHITE} \n[{question_idx}] {num1} {random_operator} {num2} = ", end="")
        answer = input()

        if check_answer(answer, num1, num2, random_operator):
            num_correct += 1
            print(Fore.GREEN + "Correct!")
        else:
            print(Fore.RED + "Incorrect.")

        # Check if 60 seconds have passed
        if time.time() - start_time >= 60:
            print("Time's up!")
            break

        question_idx += 1

    end_time = time.time()
    total_time = end_time - start_time

    score_percent = (num_correct / num_questions) * 100
    print(f"You got {num_correct} out of {num_questions} correct in {total_time:.2f} seconds.")
    print(f"Your {score_percent:.2f}%. asian enough")

def main():
    timer_and_score()

if __name__ == "__main__":
    main()