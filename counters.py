def exact_count(file_name):
    counter=dict()
    with open(file_name,"r") as f:
        for line in f:
            for letter in line:
                if letter.isalpha():
                    counter[letter]= counter.get(letter,0) +1
                    
    return counter