#2 names
#2 adjectives
#4 nouns
#1 famous person

# Inputs
name = input("Enter a name: ")
name2 = input("Enter a name: ")
adj = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
noun = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter a noun: ")
noun4 = input("Enter a noun: ")
famous = input("Enter the name of a famous person: ")

# Story
story = f"""
One day, {name} and {name2} were walking through a {adj} forest, looking for the legendary {noun}.
Suddenly, they stumbled upon a hidden {noun2} buried beneath a pile of leaves.
It was glowing with a {adj2} light.

Excited, they picked it up and realized it was actually a magical {noun3}.
Just then, {famous} appeared out of nowhere, holding a {noun4}, and said:
"You two have finally found it... the world will never be the same again."

They looked at each other and smiled, ready for whatever adventure lay ahead.
"""

# Output
print("\nHere's your Mad Libs story:\n")
print(story)
