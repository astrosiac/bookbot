book_path = "books/frankenstein.txt"


def main():
    text = get_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    list = alpha_list(letter_count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} found in the document!")
    print()

    for i in list:
        print(f"The {i['char']} character was found {i['num']} times!")

    print("--- End Report ---")


def get_text(path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def count_letters(text):
    letter_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letter_dict:
            letter_dict[letter] += 1

        else:
            letter_dict[letter] = 1
    return letter_dict


def sort_on(d):
    return d["num"]


def alpha_list(text):
    char_list = []
    for i in text:
        if i.isalpha():
            char_list.append({"char": i, "num": text[i]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


main()
