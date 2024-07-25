def count_words(text):
    """
    Count the number of words in the given text.
    
    Parameters:
    text (str): The input text provided by the user.
    
    Returns:
    int: The number of words in the text.
    """
    # Split the text by spaces to get the words
    words = text.split()
    
    # Return the length of the list which is the word count
    return len(words)

def main():
    """
    Main function to run the word counter program.
    """
    print("Word Counter Program")
    print("-------------------")
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty string. Please try again.")
    else:
        # Count the words in the input
        word_count = count_words(user_input)
        
        # Display the word count
        print(f"The number of words in the input text is: {word_count}")

if __name__ == "__main__":
    main()
