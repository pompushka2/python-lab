import re

def analyze_words(word_list):
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1

    most_popular_word = word_list[0]
    longest_word = word_list[0]
    shortest_word = word_list[0]

    for word in word_count:
        if word_count[word] > word_count[most_popular_word]:
            most_popular_word = word

    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word

    return most_popular_word, longest_word, shortest_word

text = input("Введите текст: ")
raw_words = re.split(r"[, .:;!?]", text.lower())

total_words = len(raw_words)
print(f"\nОбщее количество слов в тексте: {total_words}")

most_pop, longest, shortest = analyze_words(raw_words)
print(f"Самое частое слово: '{most_pop}'")
print(f"Самое длинное слово: '{longest}'")
print(f"Самое короткое слово: '{shortest}'")

filtered_words = [w for w in raw_words if len(w) >= 3]

most_pop_f, longest_f, shortest_f = analyze_words(filtered_words)
print(f"\ОТ 3 СИМВОЛОВ")
print(f"Самое частое слово: '{most_pop_f}'")
print(f"Самое длинное слово: '{longest_f}'")
print(f"Самое короткое слово: '{shortest_f}'")
