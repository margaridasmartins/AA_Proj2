"""

Project 2 Advanced Algorithmts 2021/22
Margarida Martins

"""

import random
import unicodedata

#Exact counter
def exact_count(file_name):
    counter=dict()
    with open(file_name,"r") as f:
        for line in f:
            for letter in line:
                letter=get_letter(letter)
                if letter.isalpha():
                    counter[letter]= counter.get(letter,0) +1
                    
    return counter

#Approximated counter with fixed probability
def fixed_probability_count(file_name, probability):
    counter=dict()
    with open(file_name,"r") as f:
        for line in f:
            for letter in line:
                letter=get_letter(letter)
                if letter.isalpha() and random.random()<probability:
                    counter[letter]= counter.get(letter,0) +1

    estimated_counts={k: v/probability for k,v in counter.items()}         
    return counter, estimated_counts

#Approximated counter with decreasing probability
def decreasing_probability_count(file_name, prob_func, conver_count):
    counter=dict()
    with open(file_name,"r") as f:
        for line in f:
            for letter in line:
                letter=get_letter(letter)
                if letter.isalpha() and random.random()<prob_func(counter.get(letter,0)):
                    counter[letter]= counter.get(letter,0) +1
    estimated_counts={k: conver_count(v) for k,v in counter.items()}                 
    return counter,estimated_counts

#remove accents
def get_letter(letter):
    return unicodedata.normalize('NFD', letter).encode('ascii', 'ignore').decode()