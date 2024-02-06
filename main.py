def main():
    file_path = 'github.com/bookbot/Books/frankenstein.txt'
    file_content = text_file(file_path)
    if file_content is not None:
        word_count = count_words(file_content)
        letter_count = count_letters(file_content)
        sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()
        for letter, count in sorted_letter_count:
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

def text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
    return letter_count




main()
