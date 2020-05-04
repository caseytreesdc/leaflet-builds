import sys


NVP_20200427 = {
    'preheader': 'Because there is always something more to learn about trees.',
    'article-1__link': 'https://caseytrees.org/2020/04/message-from-mark/?utm_source=leaflet&utm_medium=email&utm_campaign=blog',
    'article-1__alt-text': 'a message from executive director, mark buscaino',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/perceptions-browser.jpg',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/perceptions-responsive.jpg',
    'article-1__heading': 'A Note From Casey Trees Executive Director, Mark Buscaino',
    'article-1__description': 'While times are challenging, the energy and ideas of Casey Trees and our city remain as creative and strong as ever.',
    'button-1__link': 'https://caseytreesdc.github.io/treereportcard2019/?utm_source=leaflet&utm_medium=email&utm_campaign=trc',
    'button-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-button-1-browser.png',
    'button-1__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-button-1-responsive.png',
    'button-1__alt-text': 'the 2019 Tree Report Card!',
    'button-2__link': 'https://caseytreesdc.github.io/treereportcard2019/?utm_source=leaflet&utm_medium=email&utm_campaign=trc#navmetrics',
    'button-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-button-2-browser.png',
    'button-2__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-button-2-responsive.png',
    'button-2__alt-text': 'Check out our grades!',
    'article-2__link': 'https://caseytrees.org/2020/04/weve-added-to-our-virtual-class-offerings/?utm_source=leaflet&utm_medium=email&utm_campaign=edu',
    'article-2__alt-text': 'We’ve Added to Our Virtual Class Offerings!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/leaflet-treeID-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/leaflet-treeID-resplonsive.png',
    'article-2__heading': 'We’ve Added to Our Virtual Class Offerings!',
    'article-2__description': 'In less than a half hour learn tree tips, tricks, tidbits from the comfort and safety from your own home',
    'article-3__link': 'https://caseytrees.org/2020/04/the-best-thing-to-do-for-urban-trees-this-summer/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'article-3__alt-text': "watering guide",
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/water-browser.jpg',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/water-resplonsive.jpg',
    'article-3__heading': 'The Best Thing To Do For Urban Trees This Summer',
    'article-3__description': 'So simple, so effective, and yet still so needed',
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

