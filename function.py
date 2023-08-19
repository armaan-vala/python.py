def most_frequent(string):
    string = string.lower()
    
    # Create an empty dictionary 
    letter_freq = {}
    
    #counting the frequency
    for letter in string:
        if letter.isalpha():
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
    
    # sorting
    sorted_letters = sorted(letter_freq.keys(), key=lambda x: letter_freq[x], reverse=True)
    
    # Print the letters and their frequencies
    for letter in sorted_letters:
        print(f"{letter} = {letter_freq[letter]:02d}")

# Getting input from user
input_string = input("Please enter a string: ")

# Calling
most_frequent(input_string)
