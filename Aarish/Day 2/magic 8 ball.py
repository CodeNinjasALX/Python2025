import random

question = input("Ask the magic 8 ball a question")
randNum = random.randint(1,8)

if randNum == 1:
    print("You asked me: " + question)
    print("Yes")
elif randNum == 2:
    print("You asked me: " + question)
    print("Ask again later")
elif randNum == 3:
    print("You asked me: " + question)
    print("Not likely")
elif randNum == 4:
    print("You asked me: " + question)
    print("Aint no way bro asked me this")
elif randNum == 5:
    print("You asked me: " + question)
    print("Be for real now")
elif randNum == 6:
    print("You asked me: " + question)
    print("Hell naw")
elif randNum == 7:
    print("You asked me: " + question)
    print("Yes")
elif randNum == 8:
    print("You asked me: " + question)
    print("Bruh")