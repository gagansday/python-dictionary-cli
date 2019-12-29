import json
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    data = json.load(open("dictionary.json"))

    def getDefinition(word):
        return data[word]

    if word in data:
        return getDefinition(word)
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        word = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % word)
        if yn.upper() == "Y":
            return getDefinition(word)

    return "The word doesn't exist. Please double check the it."


word = input("Enter word: ")
print(translate(word))
