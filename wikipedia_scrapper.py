import re

from bs4 import BeautifulSoup
import requests


def get_all_paragraphs_from_wikipedia_page(input_url):
    r = requests.get(input_url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find_all('p')


def get_avg_n_letter_word_count_in_paragraphs(paragraphs, no_of_letters):
    words_count = 0

    no_of_paras = len(paragraphs)
    for para in paragraphs:
        all_words = re.findall(r'\w+', para.text)
        words_count += len([i for i in all_words if len(i) == no_of_letters])

    return int(words_count / no_of_paras)


if __name__ == '__main__':
    wikipedia_url = input("Enter a wikipedia page url ")
    paragraphs = get_all_paragraphs_from_wikipedia_page(wikipedia_url)
    three_letter_words_avg = get_avg_n_letter_word_count_in_paragraphs(paragraphs, 3)
    four_letter_words_avg = get_avg_n_letter_word_count_in_paragraphs(paragraphs, 4)
    five_letter_words_avg = get_avg_n_letter_word_count_in_paragraphs(paragraphs, 5)

    print("{} 3 letter words/paragraph".format(three_letter_words_avg))
    print("{} 4 letter words/paragraph".format(four_letter_words_avg))
    print("{} 5 letter words/paragraph".format(five_letter_words_avg))
