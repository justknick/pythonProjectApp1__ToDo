import json
# think about the output

with open("../files/section16bonus1-questions.json", 'r') as file:
    # give content as string
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, " - ", alternative)
    user_input = int(input("Enter answer here: "))
    question["user_input"] = user_input

score = 0
for index, question in enumerate(data):
    if question["correct_answer"] == question["user_input"]:
        score = score + 1
    message = (f"Question {index + 1} - Your answer: {question['user_input']}."
               f" Correct answer: {question['correct_answer']}")
    print(message)

print("Your score is ", score, "/", len(data))
