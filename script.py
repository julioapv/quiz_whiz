PAIR_LIMIT = 2 

words_to_learn = {
    "dog": "perro",
    "cat": "gato",
    "fruit": "fruta",
    "water": "agua",
}

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
        study_review_list()
    else:
        print("Excellent work, you didn't have any wrong words!")

def study_pairs():
    tries = 3
    
    for key, value in words_to_learn.items():
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
    for i in range(PAIR_LIMIT):
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
    print(words_to_learn)

def starter():
    print("Welcome to Quiz Whiz!")
    user_answer = input("Write 'study' (study with default pairs) or 'add' (add new pairs): ")
    
    while (user_answer != 'study') and (user_answer != 'add'):
        user_answer = input("Write 'yes' (study with default pairs) or 'no' (add new pairs): ")
    
    if user_answer == 'study':
        print("Studying right now...")
        print()
        study_pairs()
    else:
        add_words_to_list()
        print("Studying right now...")
        print()
        study_pairs()
    
def main():
    starter()
    review_prompt()
    print("You finished your study session, good job!")

main()