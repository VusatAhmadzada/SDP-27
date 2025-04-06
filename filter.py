import json

def filter_businesses_with_hotels(input_file, output_file):
    """
    Filters businesses containing 'Hotels' in their categories field and writes each to a new line in the output file.
    
    Parameters:
    - input_file: Path to the input JSON file.
    - output_file: Path to the output JSON file for filtered businesses.
    """
    try:
        # Open the input file and output file with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            # Iterate through each line (assuming each business is a JSON object in a new line)
            for line in infile:
                business = json.loads(line)  # Parse JSON string
                categories = business.get("categories", "")

                # Check if 'Hotels' is in categories
                if categories and "Hotels" in categories:
                    outfile.write(json.dumps(business) + '\n')  # Write JSON object as a single line

            print(f"Filtered businesses have been written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output file paths
input_file_path = "yelp_academic_dataset_business.json"  # Replace with the correct input file path
output_file_path = "filtered_hotels.json"  # Replace with the desired output file path

filter_businesses_with_hotels(input_file_path, output_file_path)
