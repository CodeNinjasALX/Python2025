import random

question = input("what you wanna ask the 8 ball?")
randNom = random.randint(1,8)

if randNom == 1:
    print("ask again later")
    print("you asked me: " + question)
elif randNom == 2:
    print("you asked me" + question)
    print("go away")
elif randNom == 3:
    print("you asked me" + question)
    print("no")
elif randNom == 4:
    print("yes" + question)
    print("maybe")
elif randNom == 5:
    print("you asked me" + question)
    print("ask again in 13 seconds")
elif randNom == 6:
    print("you asked me" + question)
    print(" ")
elif randNom == 7:
    print("you asked me" + question)
    print("ask the person next to you if the like the floor, thats your answer")
elif randNom == 8:
    print("you asked me" + question)
    print("yes if you like donuts")