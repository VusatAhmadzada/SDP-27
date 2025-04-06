import json
from langdetect import detect, DetectorFactory

# Ensure consistent results from the langdetect library
DetectorFactory.seed = 0

def remove_non_english_reviews(input_file, output_file):
    """
    Filters out non-English reviews from the input JSON file.

    Parameters:
    - input_file: Path to the input JSON file with reviews.
    - output_file: Path to the output JSON file with only English reviews.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            count = 0
            filtered_count = 0

            for line in infile:
                count += 1
                review = json.loads(line)
                text = review.get('text', '')

                try:
                    # Detect language and keep only English reviews
                    if detect(text) == 'en':
                        json.dump(review, outfile)
                        outfile.write('\n')
                        filtered_count += 1
                except Exception as e:
                    # Skip reviews where language detection fails
                    print(f"Skipping review {count}: {e}")

                if count % 10000 == 0:  # Progress update every 10k reviews
                    print(f"Processed {count} reviews so far. Filtered {filtered_count} English reviews.")

        print(f"Completed. Filtered {filtered_count} English reviews out of {count} total reviews.")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_file = "cleaned_reviews.json"  # Input JSON file with reviews
output_file = "english_reviews.json"  # Output JSON file with only English reviews

remove_non_english_reviews(input_file, output_file)
