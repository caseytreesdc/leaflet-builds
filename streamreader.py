import sys


NVP_20200413 = {
    'preheader': 'Celebrating the city’s most cherished cherry!',
    'article-1__link': 'https://caseytrees.org/2020/04/for-the-future/?utm_source=leaflet&utm_medium=email&utm_campaign=membership',
    'article-1__alt-text': 'kids planting trees',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/for-the-future-browser.jpg',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/for-the-future-responsive.jpg',
    'article-1__heading': 'For the future...',
    'article-1__description': '...while finding joy in the present. And what that has to do with trees.',
    'button-1__link': 'https://littlesesameadventures.com/pages/earthday5k#',
    'button-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ads-03-browser.png',
    'button-1__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ads-03-responsive.png',
    'button-1__alt-text': '#RUNFORMOTHEREARTH with Little Sesame and Republic Restoratives',
    'button-2__link': 'https://littlesesameadventures.com/pages/earthday5k',
    'button-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ad-02-browser.png',
    'button-2__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ad-02-responsive.png',
    'button-2__alt-text': 'Regeister Here - Earth Day Virtual 5k',
    'article-2__link': 'https://caseytrees.org/2020/04/winner-of-cherry-blossom-bracket/?utm_source=leaflet&utm_medium=email&utm_campaign=spring',
    'article-2__alt-text': 'blossom bracket winner!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/cherry-blossom-winner-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/cherry-blossom-winner-responsive.png',
    'article-2__heading': 'Winner of Cherry Blossom Bracket ',
    'article-2__description': 'drumroll please...',
    'article-3__link': 'https://caseytrees.org/2020/04/weve-added-to-our-blossoming-trees-of-d-c-map/?utm_source=leaflet&utm_medium=email&utm_campaign=membership',
    'article-3__alt-text': "We've added more trees to our Blossoming Trees of DC.",
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/trees-of-note-browser-copy.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/trees-of-note-update-responsive.png',
    'article-3__heading': 'We’ve Added to Our Blossoming Trees of D.C. Map!',
    'article-3__description': ' Featuring freshly added favorites like Lindens, Redbuds, and Tulip Trees.',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/76e310e2-e233-46b8-9cf6-c6995b4c5d97?trk=arbordayquiz',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad-mobile.png',
    'banner__alt-text': 'Plant it Forward',
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

