import sys
import random

emojis = open("emojipasta.txt").read().splitlines()

emoji_dict = {}

for x in emojis:
    parameters = x.split(" | ")
    emoji_dict[parameters[0]] = parameters[1].split()

if len(sys.argv) == 2:
    text = sys.argv[1]
    words = text.split()

    test_sentence = ""
    emojipasta_alternator = 0

    for x in words:
        lowercase_word = "".join([char.lower() for char in x if char.isalpha()])

        found = 0
        for k, v in emoji_dict.items():
            if lowercase_word in v:
                test_sentence = f"{test_sentence} {x} {chr(int(k))}"
                found = 1
                break

        if found == 0:
            if emojipasta_alternator%4==0:
                test_sentence = f"{test_sentence} {x} {random.choice(["😀","😃","😄","🙂","🙃"])}"
            else:
                test_sentence = f"{test_sentence} {x}"
            emojipasta_alternator += 1

    print(test_sentence.strip())

else:
    print("Error: you need to provide text in quotes!")