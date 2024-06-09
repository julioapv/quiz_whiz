import random

words_to_learn = {
    "dog": "perro",
    "cat": "gato",
    "fruit": "fruta",
    "water": "agua",
}

random_words_to_learn = {}

incorrect_words = {}

def study_review_list():
    print("In review mode you got inifine tries! :D")
    for key, value in incorrect_words.items():

        answer = input(f"What's the meaning of '{key}'? ")

        while answer != value:
            if answer == "":
                answer = input(f"What's the meaning of '{key}'? ")
                print()
            elif(answer == value):
                print("Correct!")
                print(f"The meaning of '{key}' is '{value}'")
                print()
            else:
                print("Incorrect :(")
                answer = input(f"What's the meaning of '{key}'? ")
                print()

def review_prompt():
    if len(incorrect_words) > 0:
        print("These are the words you got wrong: ")
        for word in incorrect_words:
            print(word)
            
        answer = input("Would you like to study these words? (yes/no) ")
        while (answer != 'yes') and (answer != 'no'):
            answer = input("Would you like to study these words? (yes/no) ")
        
        if answer == 'yes':
            study_review_list()
        else:
            return
    else:
        print("Excellent work, you didn't have any wrong words!")

def study_pairs():
    tries = 3
    
    print("You have to write the Spanish translation for English word you see, make sure to write it correctly. You only have 3 attempts for each word")
    print()
    
    for key, value in words_to_learn.items():

        answer = input(f"What's the meaning of '{key}'? ")
        
        while True:
            if answer == "":
                answer = input(f"What's the meaning of '{key}'? ")
                print()
            elif(answer == value):
                print("Correct!")
                print(f"The meaning of '{key}' is '{value}'")
                print()
                break
            else:
                tries -= 1
                if tries <= 0:
                    print("Incorrect :(")
                    print(f"The meaning of '{key}' is '{value}'")
                    print("Word added for later review...")
                    incorrect_words[key] = value
                    print()
                    break
                print("Incorrect :(")
                print(f"You have {tries} tries left")
                answer = input(f"What's the meaning of '{key}'? ")
                print()
        tries = 3

def is_valid_str(user_input):
    try:
        int(user_input) or float(user_input) or user_input.strip() == ""
        print("Invalid input. Please enter a word (letters only):")
    except ValueError:
            return user_input

def add_words_to_list():
    amount_to_add = input("How many pairs would you like to add today? (just write the number): ")
    pair_limit = 0
    
    while True:
        try:
            amount_to_add = int(amount_to_add)
            break
        except ValueError:
            print("You need to input a number! No letters, empty spaces or float values")
            amount_to_add = input("How many pairs would you like to add today? (just write the number): ")
            print()
                
    pair_limit += amount_to_add
    
    for i in range(pair_limit):
        user_eng_word = input("Enter your word in English: ")
            
        while not is_valid_str(user_eng_word):
            print("Invalid input. Please enter a word (letters only):")
            user_eng_word = input("Please enter a word in English: ")
            print()
            
        user_esp_word = input("Enter the translation in Spanish of the last word: ")
        
        while not is_valid_str(user_esp_word):
            print("Invalid input. Please enter a word (letters only):")
            user_esp_word = input("Please enter the Spanish translation: ")
            print()
        
        words_to_learn[user_eng_word] = user_esp_word
        print()

def starter():
    print("Welcome to Quiz Whiz!")
    user_answer = input("Write 'study' (study with default pairs) or 'add' (add new pairs): ")
    
    while (user_answer != 'study') and (user_answer != 'add'):
        user_answer = input("Write 'study' (study with default pairs) or 'add' (add new pairs): ")
    
    if user_answer == 'study':
        print()
        study_pairs()
    else:
        print()
        add_words_to_list()
        print()
        study_pairs()
    
def main():
    starter()
    review_prompt()
    print("You finished your study session.")

main()