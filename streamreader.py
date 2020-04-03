import sys


NVP_20200407 = {
    'article-1__link': 'https://caseytrees.org/2020/04/its-the-final-countdown/?utm_source=leaflet&utm_medium=email&utm_campaign=spring',
    'article-1__alt-text': '#blossombracket finals!',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/cherry-blossom-bracket-article-one.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/bracket-mobile.png',
    'article-1__heading': 'It’s the FInal Countdown...',
    'article-1__description': '...of our Cherry Blossom Bracket. Find out who the top two are and vote for your favorite!',
    'button-1__link': '',
    'button-1__text': 'Our Classes Have Gone Virtual!',
    'button-2__link': '',
    'button-2__text': 'Your City Your Trees',
    'article-2__link': 'https://caseytrees.org/2020/04/lets-kick-off-arbor-month-with-a-lil-quiz-on-its-history/?utm_source=leaflet&utm_medium=email&utm_campaign=citizenscience',
    'article-2__alt-text': 'arbor day quiz!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/arbordayquiz-email-browser.jpg',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/arbordayquiz-email-mobile.jpg',
    'article-2__heading': ' April is Citizen Science Month',
    'article-2__description': 'We’re here to tell you all about what citizen science is and why it’s a great activity for our physically distant world these days.',
    'article-3__link': 'https://caseytrees.org/2020/04/april-is-citizen-science-month/?utm_source=leaflet&utm_medium=email&utm_campaign=citizenscience',
    'article-3__alt-text': 'april is citizen science month',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/citscimonth-article-two.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/citiscimonth-responsive.jpg',
    'article-3__heading': 'Let’s Kick Off Arbor Month with a Lil Quiz on its History',
    'article-3__description': 'To start, let’s learn the history of Arbor Day and how it came to be.',
    'button-3__link': 'https://www.google.com',
    'button-3__text': 'HERE WILL GO AN AD'
}

NVP = NVP_20200407
#


def replacekeys(line):
    # built-in dictionary method that returns a list of its (key, value) tuple pairs
    for name, value in NVP.items():
        line = line.replace(f'%%{name}%%', value)

    return line


# read redirected standard input line by line

for line in sys.stdin:
    # stdout is redirected to > filename.html
    print(replacekeys(line), end='')

