def wordcounter(w):
    wordlist = w.split()
    return len(wordlist)
    
def charactercounter(text):
    lowertext = text.lower()
    characters = list(lowertext)
    charactercount = {}
    for character in characters:
        if character in charactercount:
            charactercount[character] += 1
        else: charactercount[character] = 1
    return (charactercount)

def charactercount_to_list(chars):
        unsorted = []
        for char in chars:
            new_dict = {"char": char, "num": chars[char]}
            unsorted.append(new_dict)
        return unsorted

def sort_index(x):
     return x["num"]
