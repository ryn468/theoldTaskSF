dictionary = []
people = int(input("How many people will take this survery?"))
for x in range(people):
    question = ["What is your name?", "How old are you?"]
    keys = ["name", "age"]

    survey = {}

    for item in range(len(question)):
        answer = input(question(item))
        survey[keys[item]] = answer

    dictionary.append(survey)

print(dictionary)
