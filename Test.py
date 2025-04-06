import os

def load_word_frequencies(freq_file):
    word_freq = {}
    with open(freq_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(': ')
            if len(parts) == 2:
                word, freq = parts
                word_freq[word] = int(freq)
    return word_freq

def process_sensory_file(sensory_file, word_freq):
    sensory_word_counts = {}
    with open(sensory_file, 'r', encoding='utf-8') as f:
        for word in f:
            word = word.strip().lower()
            if word in word_freq:
                sensory_word_counts[word] = word_freq[word]
    return sensory_word_counts

def write_output(sensory_file, sensory_word_counts):
    output_file = f"{os.path.splitext(sensory_file)[0]}_frequencies.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, freq in sorted(sensory_word_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{word}: {freq}\n")
    print(f"Generated {output_file}")

def main():
    freq_file = "word_frequencies.txt"
    sensory_files = ["sight.txt", "taste.txt", "touch.txt", "smell.txt", "sound.txt"]
    
    word_freq = load_word_frequencies(freq_file)
    
    for sensory_file in sensory_files:
        if os.path.exists(sensory_file):
            sensory_word_counts = process_sensory_file(sensory_file, word_freq)
            write_output(sensory_file, sensory_word_counts)
        else:
            print(f"File {sensory_file} not found!")

if __name__ == "__main__":
    main()
