'''
Emily Cordero
Brother Eisinger
sentences.py 
Prove that you can write functions with parameters and call those functions multiple times with arguments.
'''
import random
quantity = [1,2]
tense = ["past", "present", "future"]
determiner = ''
noun = ''
verb = ''
prepositional_phrase = ''
index = 0

words = ["boy", "girl", "cat", "dog", "bird", "house"]

def main():
    make_sentence(quantity[0], tense[0])
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.")
    make_sentence(quantity[0], tense[1])
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.")
    make_sentence(quantity[0], tense[2])
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.")
    make_sentence(quantity[1], tense[0])
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.")
    make_sentence(quantity[1], tense[1])
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.")
    make_sentence(quantity[1], tense[2])
    print(f"{determiner} {noun} {verb} {prepositional_phrase}.")
    print()
def make_sentence(quantity, tense):
    get_determiner(quantity)
    get_noun(quantity)
    get_verb(quantity,tense)
    get_prepositional_phrase(quantity)
    get_prepositional_phrase(quantity)

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(words)
    print(determiner, end=' ')
    return determiner

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit","woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    #randomly choose a noun and return it
    noun = random.choice(words)
    print(noun, end = ' ')
    return noun

def get_verb(quantity, tense):
    if tense == 'past' and quantity != 1:
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present':
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    verb = random.choice(words)
    print(verb, end = ' ')
    return verb

def get_preposition():
    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(words)
    print(preposition, end = ' ')
    return preposition

def get_prepositional_phrase(quantity):
    if quantity == 1:
        preposition = get_preposition()
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        prepositional_phrase = (f'{preposition} {determiner} {noun}')

    else:
        preposition = get_preposition()
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        prepositional_phrase = (f'{preposition} {determiner} {noun}')
    return prepositional_phrase
main()