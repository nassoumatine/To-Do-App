# In this code I learnt how to work with one or multiple data structures in python
# the user will be asked Multiple choice questions

import json
import time

with open("question.json", 'r') as file:
    content = file.read()

data = json.loads(content)  # To change the content type from str to a list because question.json was initially a list

for question_dict in data:
    print(question_dict["question_text"])
    for index, alternative in enumerate(question_dict["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question_dict["user_choice"] = user_choice

score = 0
for index, question_dict in enumerate(data):
    if question_dict["user_choice"] == question_dict["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} {result} - Your answer: {question_dict['user_choice']}, " \
              f"{index + 1} - Correct answer: {question_dict['correct_answer']}"
    print(message)

print(f"{score}/{len(data)}")
