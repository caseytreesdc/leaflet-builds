import sys


NVP_20200413 = {
    'preheader': 'Like our new leaflet look?',
    'article-1__link': 'https://caseytrees.org/2020/04/for-the-future/?utm_source=leaflet&utm_medium=email&utm_campaign=membership',
    'article-1__alt-text': '#blossombracket finals!',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/cherry-blossom-bracket-article-one.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/bracket-mobile.png',
    'article-1__heading': 'For the future...',
    'article-1__description': '. ...while finding joy in the present. And what that has to do with trees.',
    'button-1__text': 'New Virtual Tree ID Class!',
    'button-1__link': 'https://caseytrees.org/2020/04/virtual-classes-post/?utm_source=leaflet&utm_medium=email&utm_campaign=class',
    'button-2__text': 'Sign Up Now',
    'button-2__link': 'https://caseytrees.org/2020/04/virtual-classes-post/?utm_source=leaflet&utm_medium=email&utm_campaign=class',
    'article-2__link': 'https://caseytrees.org/2020/04/winner-of-cherry-blossom-bracket/?utm_source=leaflet&utm_medium=email&utm_campaign=spring',
    'article-2__alt-text': 'arbor day quiz!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/citscimonth-article-two.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/citiscimonth-responsive.jpg',
    'article-2__heading': 'Winner of Cherry Blossom Bracket',
    'article-2__description': 'drumroll please...',
    'article-3__link': 'https://caseytrees.org/2020/04/weve-added-to-ou…trees-of-d-c-map/?utm_source=leaflet&utm_medium=email&utm_campaign=maps',
    'article-3__alt-text': 'our maps pics ALT TEXT',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/arbordayquiz-email-browser.jpg',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/arbordayquiz-email-mobile.jpg',
    'article-3__heading': 'We’ve Added to Our Blossoming Trees of D.C. Map!',
    'article-3__description': ' Featuring freshly added favorites like Lindens, Redbuds, and Tulip Trees.',
    'button-3__link': 'https://connect.clickandpledge.com/w/Form/76e310e2-e233-46b8-9cf6-c6995b4c5d97?trk=arbordayquiz',
    'button-3__text': "DONATE TO HELP SUPPORT D.C.'s TREES!"
}

NVP = NVP_20200413
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

