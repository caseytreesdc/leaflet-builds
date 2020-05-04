import sys


NVP_20200427 = {
    'preheader': '',
    'article-1__link': 'https://caseytrees.org/2020/05/weekly-watering-alerts-are-here/?utm_source=leaflet&utm_medium=email&utm_campaign=weeklywateringalert',
    'article-1__alt-text': 'Watering Alerts are here!',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/watering-alert-browser.jpg',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/watering-alert-repsonsive.jpg',
    'article-1__heading': 'Weekly Watering Alerts are Here!',
    'article-1__description': 'Young trees need 1.5 inches of rain or 25 gallons of water a week. We’ll let you know whether or not to water them!',
    'watering__link': 'https://caseytrees.org/2020/05/weekly-watering-alerts-are-here/?utm_source=leaflet&utm_medium=email&utm_campaign=weeklywateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_optional.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_optional-responsive.png',
    'watering__alt-text': 'Watering Optional',
    'article-2__link': 'https://caseytrees.org/2020/05/introducing-our-newest-video-series-branch-out/?utm_source=leaflet&utm_medium=email&utm_campaign=staff',
    'article-2__alt-text': 'New short videos',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/ct-videos-browser.jpg',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/ct-videos-responsive.jpg',
    'article-2__heading': 'Branch Out with Casey Trees & Anacostia Riverkeeper',
    'article-2__description': 'Introducing Our Newest Video Series',
    'article-3__link': 'https://caseytrees.org/2020/05/d-c-launches-its-annual-campaign-against-the-smell-of-the-ginkgo-tree/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-3__alt-text': "smell the gingko tree",
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/ginkgo-spray-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/ginkgo-spray-responsive.png',
    'article-3__heading': 'D.C. Launches its Annual Campaign Against the Smell of the Ginkgo Tree',
    'article-3__description': 'Spraying began April 20 and will continue at night. Residents don’t have to move their cars or do anything else.',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/76e310e2-e233-46b8-9cf6-c6995b4c5d97?trk=arbordayquiz',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad-mobile.png',
    'banner__alt-text': 'Plant it Forward',
}

NVP = NVP_20200427
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

