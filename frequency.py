import json
from collections import Counter
import re

def calculate_word_frequency(input_file, output_file):
    """
    Calculates the frequency of words in the 'text' field of reviews.

    Parameters:
    - input_file: Path to the JSON file containing cleaned reviews.
    - output_file: Path to the output text file for word frequencies.
    """
    word_counter = Counter()

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                review = json.loads(line)  # Parse the JSON line
                text = review.get('text', '')
                # Normalize text: remove non-alphanumeric characters and convert to lowercase
                words = re.findall(r'\b\w+\b', text.lower())
                word_counter.update(words)  # Update word frequency counter

        # Write word frequencies to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for word, count in word_counter.most_common():
                outfile.write(f"{word}: {count}\n")

        print(f"Word frequency analysis completed. Results written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_file = "english_reviews.json"  # Input JSON file with cleaned reviews
output_file = "word_frequencies.txt"  # Output text file for word frequencies

calculate_word_frequency(input_file, output_file)
