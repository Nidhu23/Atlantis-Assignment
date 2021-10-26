from bs4 import BeautifulSoup
import requests


def get_and_store_all_links_from_given_repo(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    links_dict = {}
    for link in soup.find_all('a'):
        links_dict.update({link.text.lower(): link.get('href')})
    return links_dict


if __name__ == '__main__':
    url = "https://github.com/vinta/awesome-python"
    inp = input("Query? ")
    links = get_and_store_all_links_from_given_repo(url)
    try:
        print("Output {}".format(links[inp]))
    except KeyError:
        print("Sorry No matching link associated with word {} was found, try again".format(inp))
