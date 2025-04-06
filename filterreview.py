import json

def filter_reviews_by_business_ids(filtered_business_file, reviews_file, output_file):
    """
    Filters reviews that match the business IDs from the filtered business file.
    
    Parameters:
    - filtered_business_file: File containing the filtered businesses (filtered_hotels.json).
    - reviews_file: File containing reviews to be filtered (yelp_academic_dataset_review.json).
    - output_file: Path to the output file for filtered reviews.
    """
    try:
        # Step 1: Load business_ids from filtered hotels
        with open(filtered_business_file, 'r', encoding='utf-8') as f:
            business_ids = {json.loads(line)['business_id'] for line in f}

        # Step 2: Filter reviews by matching business_ids
        with open(reviews_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                review = json.loads(line)  # Parse review JSON
                if review['business_id'] in business_ids:  # Check if business_id matches
                    outfile.write(json.dumps(review) + '\n')  # Write review to output file

        print(f"Filtered reviews have been written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
filtered_business_file = "filtered_hotels.json"  # File with filtered hotels
reviews_file = "yelp_academic_dataset_review.json"  # File containing reviews
output_file = "filtered_reviews.json"  # Output file for filtered reviews

filter_reviews_by_business_ids(filtered_business_file, reviews_file, output_file)
