import sys


NVP_20200803 = {
    'preheader': 'and how the “streatery” phenomenon is good for trees and greenspace',
    'article-1__link': 'https://caseytrees.org/2020/08/tree-sources-for-schoolkids/?utm_source=leaflet&utm_medium=email&utm_campaign=store',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/junior_urban_forestor_guide-browser.jpg',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/junior_urban_forestor_guide-responsive.jpg',
    'article-1__heading': 'Tree-sources for School Kids',
    'article-1__description': 'Our Junior Urban Forester booklets, usually only available through our summer camp programs, are now for sale!',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_dontwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/WWA_dontwater-responsive.png',
    'watering__alt-text': 'We have finally had rain and we will have some more this week! No need to water this week.',
    'article-2__link': 'https://caseytrees.org/2020/08/streateries/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': 'streaeries in adams morgan',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/streateries-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/streateries-email.png',
    'article-2__heading': 'What are Streateries and Why They’re Good for Urban Trees and Greenspace',
    'article-2__description': 'What the push outside by businesses and people means for District greenspace - and what you can do about it.',
    'article-3__link': 'https://caseytrees.org/2020/08/which-is-which-magnolia-edition/?utm_source=leaflet&utm_medium=email&utm_campaign=residential',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/magnolia-species-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/magnolia-species-email.png',
    'article-3__heading': 'Which is Which: Magnolia Edition',
    'article-3__description': 'How to tell between the Southern, Saucer, Star, Sweetbay, or Loebner magnolias.',
    'banner__link': 'https://caseytrees.org/farm',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm-responsive.png',
    'banner__alt-text': 'curious about our tree farm?',
}

NVP = NVP_20200803
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
