import string

# Function to count words in a text, including options to handle punctuation
def count_words(text):
    # Remove punctuation from the text
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    # Split the text into words using space as the delimiter
    words = cleaned_text.split()
    # Return the number of words and the list of words
    return len(words), words

# Function to get user input and handle errors
def get_user_input():
    while True:
        # Prompt the user to enter a sentence or paragraph
        text = input("Please enter a sentence or paragraph: ").strip()
        # Check if the input is empty
        if text:
            return text
        else:
            print("Error: Input cannot be empty. Please try again.")

# Function to calculate additional statistics
def calculate_statistics(words):
    # Count the number of unique words
    unique_words = len(set(words))
    # Calculate the average word length
    average_length = sum(len(word) for word in words) / len(words)
    return unique_words, average_length

# Function to display the results
def display_results(word_count, unique_words, average_length):
    print(f"\nWord Count: {word_count}")
    print(f"Unique Words: {unique_words}")
    print(f"Average Word Length: {average_length:.2f} characters")

# Function to display the ASCII Welcome banner
def display_welcome_banner():
    print(r"""
 __        __   _                            _         __        __   ____     _____    _____    _____   ____         _   _  _______   _____  _____
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   \ \      / /  /    \   |     \  |     \  / ____| /    \ |   | |  |  | |__  __| | ____| |    \
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   \ \ /\ / /   |     |  |  _  /  |      | | |     |    | |   | | `\  |    | |   | |____ | _ /
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   \ V  V /    |     |  | | \ \  |      | | |____ |    | |   | | |\  |    | |   | |____ | |\ \
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/     \_/\_/     \____/   |_|  \_\ |_____/  \_____| \____/ \___/ |_| \_|    |_|   |______||_| \_\
    """)
    print("Welcome to the Enhanced Word Counter Program!\n")

# Main function to run the Word Counter program
def main():
    # Display the ASCII welcome banner
    display_welcome_banner()
    
    # List to store multiple inputs
    all_texts = []
    
    while True:
        # Get user input
        user_input = get_user_input()
        all_texts.append(user_input)
        
        # Count the words and get the list of words
        word_count, words = count_words(user_input)
        
        # Calculate statistics
        unique_words, average_length = calculate_statistics(words)
        
        # Display the results
        display_results(word_count, unique_words, average_length)
        
        # Ask the user if they want to enter another text
        choice = input("\nWould you like to analyze another text? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
    
    # Combine all texts for overall statistics
    combined_text = " ".join(all_texts)
    overall_word_count, overall_words = count_words(combined_text)
    overall_unique_words, overall_average_length = calculate_statistics(overall_words)
    
    # Display overall results
    print("\nFinal Summary of All Texts:")
    display_results(overall_word_count, overall_unique_words, overall_average_length)
    print("Thank you for using the Word Counter Program!")

# Entry point of the program
if __name__ == "__main__":
    main()
