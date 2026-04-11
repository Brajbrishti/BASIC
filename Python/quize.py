# import random

# def generate_question():
#     operations = ['+', '-', '*', '/']
#     op = random.choice(operations)

#     num1 = random.randint(10, 99)
#     num2 = random.randint(1, 9)

#     # Avoid decimal answers for division
#     if op == '/':
#         num1 = num2 * random.randint(2, 12)

#     if op == '+':
#         correct = num1 + num2
#     elif op == '-':
#         correct = num1 - num2
#     elif op == '*':
#         correct = num1 * num2
#     else:
#         correct = num1 // num2

#     return num1, num2, op, correct


# def generate_options(correct):
#     options = [correct]

#     while len(options) < 4:
#         wrong = correct + random.randint(-10, 10)
#         if wrong != correct and wrong not in options:
#             options.append(wrong)

#     random.shuffle(options)
#     return options


# def quiz():
#     score = 0
#     total_questions = 5

#     for i in range(total_questions):
#         num1, num2, op, correct = generate_question()
#         options = generate_options(correct)

#         print(f"\nQuestion {i+1}: {num1} {op} {num2} = ?")

#         for idx, option in enumerate(options):
#             print(f"{idx+1}. {option}")

#         try:
#             choice = int(input("Enter your choice (1-4): "))
#             if options[choice-1] == correct:
#                 print("Correct!")
#                 score += 1
#             else:
#                 print(f"Wrong! Correct answer is {correct}")
#         except:
#             print("Invalid input!")

#     print(f"\nYour final score: {score}/{total_questions}")


# if __name__ == "__main__":
#     quiz()
