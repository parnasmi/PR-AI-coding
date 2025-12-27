def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

transcript_content = read_transcript('./transcript.txt')

def print_message(msg):
    for _ in range(10):
        print(msg)

print_message(transcript_content)

