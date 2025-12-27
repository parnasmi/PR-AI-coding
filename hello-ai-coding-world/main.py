def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

transcript_content = read_transcript('./transcript.txt')

def count_word_frequencies(text):
    word_counts = {}
    words = text.split()
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

word_frequencies = count_word_frequencies(transcript_content)

def print_word_frequencies(word_counts):
    for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"'{word}': {'#' * count}")

print_word_frequencies(word_frequencies)

