import sys


NVP_20211018 = {
    'preheader': 'plus, Urban Forestry Fellowship Now Accepting Applications',
    'article-1__link': 'https://caseytrees.org/2021/10/street-tree-before-afters/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': 'street trees, before and after',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/10/street-tree-before-after-email-1.png',
    'article-1__heading': 'Street Tree Before and Afters',
    'article-1__description': 'A satisfying look at our ever-changing urban landscape.',
    'banner-a__link': 'https://caseytrees.org/plant/#plantitforward',
    'banner-a__alt-text': 'Plant it Forward: Hire Casey Trees',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/10/urban-forestry-fellowship-now-accepting-applications/?utm_source=leaflet&utm_medium=email&utm_campaign=gcascholarship',
    'article-2__alt-text': 'what is a riparian buffer',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/10/gca-2019-email.png',
    'article-2__heading': 'Urban Forestry Fellowship Now Accepting Applications',
    'article-2__description': 'Offset the cost of undergraduate or graduate school research thanks to our partnership with the Garden Club of America',
    'article-3__link': 'https://caseytrees.org/2021/10/riparian-buffer-month/?utm_source=leaflet&utm_medium=email&utm_campaign=feeforservice',
    'article-3__alt-text': 'rock creek parkway and the duke ellington bridg',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/10/riparian-planting-email.png',
    'article-3__heading': 'Riparian Buffer Month',
    'article-3__description': 'Highlighting a riverside project and the importance of building in green buffers to improve our waterways',
    'banner-b__link': 'https://www.eventbrite.com/e/community-tree-planting-oxon-run-park-tickets-181977558777?_eboga=1915616282.1634306680&_ga=2.187267755.2091215710.1634564602-1915616282.1634306680',
    'banner-b__alt-text': "Oxon Run CTP: Team Leaders Needed",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_oxon-run-desktop.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_oxon-run-mobile.png',
}

NVP = NVP_20211018
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
