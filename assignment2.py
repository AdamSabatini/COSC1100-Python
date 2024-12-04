# File Name: assignment2.py
# Date: 2023 - 11 - 17
# Author: Adam Sabatini
# Brief Description: allow the user to encode a piece of text using a cipher,
# or to decode the text using the same cipher and allow an option to exit the program.

# Declartion
# libraries
import string

# Constants
ENCODE_OPTION = 1
DECODE_OPTION = 2
EXIT_OPTION = 3

# Lists
emoji = ("\U0001F4AF", "\U0001F620", "\U0001F34E", "\U0001F34C", "\U0001F426", "\U0001F9E0", "\U0001F68C", "\U0001F697", "\U0001F955", "\U0001F408",
         "\U0001F44F", "\U0001F976", "\U0001F36A", "\U0001F415", "\U0001F95A", "\U0001F41F", "\U0001F98A", "\U0001F600", "\U00002764", "\U0001F40E", 
         "\U0001F975", "\U0001F5FA", "\U0001F44C", "\U0001F622", "\U0001F6CC", "\U0001F332", "\U0001F9DF")

words = ("100","angry", "apple", "banana", "bird", "brain", "bus", "car", "carrot", "cat",
         "clap", "cold", "cookie", "dog", "egg", "fish", "fox", "happy", "heart", "horse",
         "hot", "map", "ok", "sad", "sleep", "tree", "zombie")

# Variables
user_input = 0
encode_print = 0
decode_print = 0 

# Functions
# https://blog.enterprisedna.co/python-remove-punctuation-from-string/#:~:text=To%20remove%20punctuation%20from%20a,new%20string%20excluding%20punctuation%20marks.
def remove_punctuation(input_text):
    """create a function to remove the punctuation from the users input"""
    # Make an empty string to hold the new string without punctuation
    no_punctuation = ""
    for characters in input_text:
        # if the character isnt a punctuation character add it to the new variable no_punctuation
        if characters not in string.punctuation:
            no_punctuation += characters
    return no_punctuation

def encode (emoji_list, word_list):
    """create function that encodes the users inputted message"""
    # create empty string variable
    encoded_string = " "
    # get the input from the user
    input_from_user = input("Please enter the text to encode: ")
    # call upon the remove_punctuation function to remove the punctuation from input_from_user
    input_from_user = remove_punctuation(input_from_user)
    # create a list from the users input using .split and store it in user_input_list
    user_input_list = input_from_user.split()
    # create a for loop to loop through all the words from the user_input_list
    for word_index in range (len(user_input_list)):
        # create a for loop to loop through the index for the words list
        for translation_index in range (len(word_list)):
            # if the word in the user_input_list equals a word in the words list enter the if statement
            if user_input_list[word_index].lower() == word_list[translation_index]:
               # replace the word in the user_input_list with the corresponding emoji 
               user_input_list[word_index] = emoji_list[translation_index]
        # add the user_input_list to the empty encoded_string variable    
        encoded_string += user_input_list[word_index] + " "
    # return the encoded_string variable
    return (encoded_string)

def decode (emoji_list, word_list):
    """create function that decodes the users inputted message"""
    # create empty string variable
    decoded_string = " "
    # get the input from the user
    input_from_user = input("Please enter the text to decode: ")
    # call upon the remove_punctuation function to remove the punctuation from input_from_user
    input_from_user = remove_punctuation(input_from_user)
    # create a list from the users input using .split and store it in user_input_list
    user_input_list = input_from_user.split()
    # create a for loop to loop through all the words from the user_input_list
    for word_index in range (len(user_input_list)):
        # create a for loop to loop through the index for the emoji list
        for translation_index in range (len(emoji_list)):
            # if the word in the user_input_list equals an emoji in the emoji list enter the if statement
            if user_input_list[word_index].lower() == emoji_list[translation_index]:
               # replace the emoji in the user_input_list with the corresponding word
               user_input_list[word_index] = word_list[translation_index]
        # add the user_input_list to the empty decoded_string variable
        decoded_string += user_input_list[word_index] + " "
    # return the decoded_string variable
    return (decoded_string)

# While user_input doesnt equal 3 enter the while loop
while user_input != EXIT_OPTION:
    # display options to user and get the users input
    user_input = input ("\n1) Encode text \n2) Decode text \n3) Exit \nPlease select an opotion between 1 and 3: ")
    # check to see is user_input is an integer
    try: 
        user_input = int(user_input)
        # if user chooses 1 call upon the encode function and print the results to the user
        if user_input == ENCODE_OPTION:
            encode_print = encode(emoji,words)
            print("Encoded text: " + encode_print)
        # if user chooses 2 call upon the decode function and print the results to the user
        elif user_input == DECODE_OPTION:
            decode_print = decode(emoji,words)
            print ("Decoded text: " + decode_print)
        # if user chooses 3 exit the program with no buffer
        elif user_input == EXIT_OPTION:
                exit()
        # else the user enters an invalid input display an error message
        else:
            print ("\nERROR: A number outside the range has been entered. Please enter 1, 2 or 3")
    # except the user enters an invalid input display an error message
    except ValueError:
        print ("\nERROR: An invalid input was entered. Please enter 1, 2 or 3")