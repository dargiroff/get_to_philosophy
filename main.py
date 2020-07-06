import requests
from bs4 import BeautifulSoup as bs


def get_soup(address):
    req = requests.get(address)
    return bs(req.content, 'lxml')


def get_first_link(soup):
    for paragraph in soup.find('div', {'id': 'bodyContent'}).findAll('p'):
        for hyperlink in paragraph.findAll('a'):
            if hyperlink and hyperlink.get('href').startswith('/wiki/'):
                return hyperlink.get('href')


def get_to_philosophy(starting_url, max_iters=50):
    wiki = 'https://en.wikipedia.org/'
    target_page = wiki + "/wiki/Philosophy"
    current_address = starting_url if "/wiki/" in starting_url else "/wiki/" + starting_url
    print(f'Currently at {current_address}')

    visited_links = list()
    stuck_counter = 0
    for idx in range(max_iters):
        soup = get_soup(current_address)
        current_address = wiki + get_first_link(soup)
        print(f'Currently at {current_address}')
        if current_address in visited_links:
            stuck_counter += 1
            if stuck_counter == 10:
                print('\nWe are stuck in a loop. How philosophical of us!')
                print('\nThe \'Strange Loop\' phenomenon occurs whenever, by moving upwards (or downwards) through\n'
                      'the levels of a hierarchical system, we unexpectedly find ourselves back where we started.\n'
                      '- Douglas Hofstadter')
                return
        visited_links.append(current_address)
        if current_address.lower() == target_page.lower():
            print(f'We have arrived at Philosophy after {idx + 1} iterations')
            return

    print('\nThe maximum number of iterations has been reached')


kermit = 'https://en.wikipedia.org/wiki/Kermit_the_Frog'
dimitar = 'https://en.wikipedia.org/wiki/Dimitar'
reality = 'https://en.wikipedia.org/wiki/Reality'

get_to_philosophy(reality)
