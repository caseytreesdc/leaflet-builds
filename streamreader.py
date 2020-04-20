import sys


NVP_20200420 = {
    'preheader': 'by sending your friends and loved ones a goofy Arbor Day greeting',
    'article-1__link': 'https://caseytreesdc.github.io/treereportcard2019/',
    'article-1__alt-text': 'the Tree Report Card 2019',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/leaflet-trc-story-browser.jpg',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/leaflet-trc-story-responsive.jpg',
    'article-1__heading': 'For our Members, The Tree Report Card',
    'article-1__description': "The State of D.C.'s trees in 2019. Happy Arbor Day!",
    'button-1__link': 'https://littlesesameadventures.com/pages/earthday5k#',
    'button-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ads-03-browser.png',
    'button-1__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ads-03-responsive.png',
    'button-1__alt-text': '#RUNFORMOTHEREARTH with Little Sesame and Republic Restoratives',
    'button-2__link': 'https://littlesesameadventures.com/pages/earthday5k',
    'button-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ad-02-browser.png',
    'button-2__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-5k-ad-02-responsive.png',
    'button-2__alt-text': 'Register Here - Earth Day Virtual 5k',
    'article-2__link': 'https://caseytrees.org/2020/04/spring-cleaning-your-house-and-the-earth/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': 'spring cleaning!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/spring-cleaning-2020-email-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/spring-cleaning-2020-article-responsive.png',
    'article-2__heading': 'Spring Cleaning Your House and The Earth',
    'article-2__description': 'Everything connected, which our Earth (and COVID-19) showcases',
    'article-3__link': 'https://caseytrees.org/2020/04/celebrating-the-emancipation-oak-this-emancipation-day/?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-3__alt-text': "We've added more trees to our Blossoming Trees of DC.",
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/emancipation-oak-article-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/emancipation-oak-article-responsive.png',
    'article-3__heading': 'Celebrating the Emancipation Oak this Emancipation Day',
    'article-3__description': 'A (giant) piece of American history in D.C.’s backyard',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/76e310e2-e233-46b8-9cf6-c6995b4c5d97?trk=arbordayquiz',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad-mobile.png',
    'banner__alt-text': 'Plant it Forward',
}

NVP = NVP_20200420
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

