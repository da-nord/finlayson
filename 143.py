from collections import Counter
import re

# Define the file path
file_path = r'f:\ccc.txt'

# Function to count words and their frequencies
def count_words(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            print(file.readlines()[:10])  # Print the first 10 lines

        
        # Use regex to find words, convert to lowercase, and remove punctuation
        #words = re.findall(r'\b\w+\b', text.lower())
        words = re.findall(r"[a-zA-Z']+", text)
        
        # Count the frequency of each word
        word_count = Counter(words)
        
        # Sort words by frequency and return
        sorted_word_count = word_count.most_common()
        return sorted_word_count

    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the word frequencies
word_frequencies = count_words(file_path)

# Print the results
if word_frequencies:
    for word, count in word_frequencies:
        print(f"{word}: {count}")