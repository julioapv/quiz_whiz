PAIR_LIMIT = 2 

words_to_learn = {
    "dog": "perro",
    "cat": "gato",
    "fruit": "fruta",
    "water": "agua",
}

incorrect_words = []

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
    user_answer = input("Write 'yes' (study with default pairs) or 'no' (add new pairs): ")
    
    while (user_answer != 'yes') and (user_answer != 'no'):
        user_answer = input("Write 'yes' (study with default pairs) or 'no' (add new pairs): ")
    
    if user_answer == 'yes':
        print("Studying right now...")
    else:
        add_words_to_list()
        print("Studying right now...")
    
def main():
    starter()

main()