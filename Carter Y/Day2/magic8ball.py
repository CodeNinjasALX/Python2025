import random

question = input("Ask the magic 8 ball a question")
randNum = random.randint(1,8)

if randNum == 1:
    print("you asked me: " + question)
    print("Ask agin later")


