import json

def load_stopwords(stopword_file):
    """
    Load stopwords from a file into a set.
    """
    try:
        with open(stopword_file, 'r', encoding='utf-8') as f:
            stopwords = {line.strip().lower() for line in f if line.strip()}
        print(f"Loaded {len(stopwords)} stopwords from {stopword_file}.")
        return stopwords
    except Exception as e:
        print(f"An error occurred while loading stopwords: {e}")
        return set()

def remove_stopwords_from_reviews(input_file, output_file, stopword_file):
    """
    Removes stopwords from the 'text' field in reviews and writes cleaned reviews to a new file.
    """
    try:
        stopwords = load_stopwords(stopword_file)
        
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            count = 0
            for line in infile:
                count += 1
                review = json.loads(line)  # Parse the JSON line
                text = review.get('text', '')
                words = text.split()
                cleaned_text = ' '.join(word for word in words if word.lower() not in stopwords)
                review['text'] = cleaned_text  # Update the review text
                outfile.write(json.dumps(review) + '\n')  # Write the cleaned review

                if count % 10000 == 0:  # Progress update every 10k reviews
                    print(f"Processed {count} reviews so far.")

        print(f"Processing completed: {count} reviews cleaned and written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
stopword_file = "stopword_list.txt"  # File containing stop words
input_file = "filtered_reviews.json"  # File containing non-empty reviews
output_file = "cleaned_reviews.json"  # Output file for cleaned reviews

remove_stopwords_from_reviews(input_file, output_file, stopword_file)
