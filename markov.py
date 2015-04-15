from sys import argv
script, filename = argv

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    # takes text from file and creates a list of space delimited strings
    with open(corpus) as original_file:
        root_text = []

        for line in original_file:
            line = line.rstrip().split(" ")
            for word in line:
                root_text.append(word.rstrip())

    dictionary = {}

    # creates dictionary of tuple pairs and subsequent words (values)
    for i in range(len(root_text)-2):
        tuple_pair = (root_text[i], root_text[i+1])
        if tuple_pair not in dictionary:
            dictionary[tuple_pair] = [root_text[i+2]]
        elif tuple_pair in dictionary:
            dictionary[tuple_pair].append(root_text[i+2])
    return dictionary



import random

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #set output text as blank (before we fill it in)
    output_text = ""

    #pick a random key to start
    random_key = random.sample(chains, 1)
    output_text = random_key[0][0] + " " + random_key[0][1]


    #pick a random value associated with that key
    while True:
        random_value = random.choice(chains[random_key[0]])
        output_text = output_text + " " + random_value
        new_tuple = (random_key[0][1], random_value)

        if new_tuple in chains:
            random_key[0] = new_tuple
        else:
            break
            
    return output_text
chains = make_chains(filename)
final_text = make_text(chains)
print final_text

