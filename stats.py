def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(file_path): 
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_unique_characters(text):
    text = text.lower()
    unique_chars = {}
    for char in text:
        if char != '' and not char.isspace():
            unique_chars[char] = unique_chars.get(char, 0) + 1
    return unique_chars

def sort_unique_characters(unique_chars):
    unique_chars = [{"char": char, "num": num} for char, num in unique_chars.items()]
    unique_chars.sort(reverse=True, key=sort_on)
    return unique_chars

def sort_on(items):
    return items["num"]