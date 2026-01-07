import sys
import random

#Open emojipasta.txt to get word-emoji mappings
emojis = open("emojipasta.txt").read().splitlines()

emoji_dict = {}

#Fill dictionary with these mappings
for x in emojis:
    parameters = x.split(" | ")
    emoji_dict[parameters[0]] = parameters[1].split()

#Takes in terminal argument
if len(sys.argv) == 2:
    text = sys.argv[1]
    words = text.split()

    test_sentence = ""
    emojipasta_alternator = 0

    for x in words:
        #Constructs the lowercase and symbolless word for comparison
        lowercase_word = "".join([char.lower() for char in x if char.isalpha()])

        #Checks if the word is in the mappings, and assigns an emoji if so
        found = 0
        for k, v in emoji_dict.items():
            if lowercase_word in v:
                test_sentence = f"{test_sentence} {x} {chr(int(k))}"
                found = 1
                break

        #If no mapping is found, determine if a filler emoji should be added (around every 4 words without emojis)
        if found == 0:
            if emojipasta_alternator%4==0:
                test_sentence = f"{test_sentence} {x} {random.choice(["😀","😃","😄","🙂","🙃"])}"
            else:
                test_sentence = f"{test_sentence} {x}"
            emojipasta_alternator += 1

    print("\n" + test_sentence.strip())

else:

    print("Error: you need to provide text in quotes!")
