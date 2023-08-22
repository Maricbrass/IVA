import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')


with open('dialogs.txt', 'r', encoding='utf-8') as file:
    dataset = file.readlines()

while True:
    user_input = input("You: ")
    tokens = word_tokenize(user_input)
    
    responses = []

    for line in dataset:
        if user_input.lower() in line.lower():
            responses.append(line)

    if responses:
        response = responses[0]  
    else:
        response = "I'm not sure how to respond to that."

    print("Chatbot:", response)
