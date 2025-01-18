import re
from collections import Counter

def create_sample_file(file_name):
    print("The file 'sample.txt' does not exist. Please enter text to create it:")
    with open(file_name, 'w') as file:
        text = input("Enter text: ")
        file.write(text)

def count_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return Counter(words)

def main():
    file_name = "sample.txt"
    if not os.path.exists(file_name):
        create_sample_file(file_name)

    word_counts = count_words(file_name)
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)

    print(f"\nTotal words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", 'w') as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")

    print("\nThe word count report has been saved.")

if __name__ == "__main__":
    import os
    main()
