import sys


NVP_20211018 = {
    'preheader': 'plus, indigenous uses of our beloved trees',
    'article-1__link': 'https://caseytrees.org/2021/11/dcs-urban-forestry-division-by-the-numbers/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'fall trees in front of DC rowhouses',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/10/ufd-numbers-street-tree-email.png',
    'article-1__heading': 'DC’s Urban Forestry Division by the Numbers',
    'article-1__description': 'Want to know how many trees UFD plants or cares for? How about where? Look no further.',
    'banner-a__link': 'https://caseytrees.org/plant/#plantitforward',
    'banner-a__alt-text': 'Plant it Forward: Hire Casey Trees',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/11/casey-trees-tips-tricks-mulch/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': '2 people mulching a tree ',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/11/mulch-email-2.png',
    'article-2__heading': 'Casey Trees’ Tips & Tricks: Mulch ',
    'article-2__description': 'What is a mulch volcano and why are they deadly',
    'article-3__link': 'https://caseytrees.org/2021/11/for-indigenous-peoples-month-learn-more-about-indigenous-uses-of-our-beloved-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': 'people rowing a birch bark canoe courtesy of the Minnesota Historical Society',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/11/dugout-canoe-email.png',
    'article-3__heading': 'For Indigenous Peoples Month, Learn More About Indigenous Uses of Our Beloved Trees',
    'article-3__description': 'From food to shelter to medicine.',
    'banner-b__link': 'http://www.facebook.com/pages/Casey-Trees/58793928339',
    'banner-b__alt-text': "follow us on facebook",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social-mobile.png',
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
