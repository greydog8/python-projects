import random

print("welcome to the magic eight ball")


while True:
    print("ask me a question")

    question = input(">")
    aswners = ["yes." , "no." , "maby."]
    aswner = random.choice(aswners)
    print(aswner)



