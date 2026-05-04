# • Write a Python program to count the frequency of each word in a sentence using a dictionary. 




# Function to count the frequency of each word in a sentence
def count_word_frequency(sentence):
    word_frequency = {}
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the frequency of each word
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
            
    return word_frequency
# Main function
def main():
    # Input sentence from the user
    sentence = input("Enter a sentence: ")

    # Count the frequency of each word
    frequency = count_word_frequency(sentence)

    # Display the word frequencies
    print("Word Frequency:")
    for word, count in frequency.items():
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()