import sys


NVP_20210125 = {
    'preheader': 'and we’re celebrating Black History Month all month long',
    'article-1__link': 'https://caseytrees.org/2021/02/walk-on-the-wild-side-with-the-urban-forestry-division/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/01/wild-side-email.png',
    'article-1__heading': 'Walk on the Wild Side with the Urban Forestry Division',
    'article-1__description': 'Three short stories that show just how far the Urban Forestry Division will go to protect city trees and the wildlife that call them home.',
    'banner-a__text-1': 'CASEY TREES IS HIRING.',
    'banner-a__text-2': "Casey Trees' is hiring.",
    'banner-a__link': 'https://caseytrees.org/about-us/jobs-internships/',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
    'banner-a__alt-text': "We're hiring!",
    'article-2__link': 'https://caseytrees.org/2021/02/black-history-month-turner-elementary-school/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/01/turner-email.png',
    'article-2__heading': 'Black History Month: Turner Elementary School',
    'article-2__description': 'Who are our planting locations named after? We’re finding out',
    'article-3__link': 'https://caseytrees.org/2021/02/anatomy-of-a-street-tree/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/01/street-tree-email.png',
    'article-3__heading': 'Anatomy of a Street Tree',
    'article-3__description': 'Breaking down everyone’s favorite street adornment',
    'banner-b__link': 'https://caseytrees.org/plant/residential-planting/',
    'banner-b__text-1': 'Riversmart Homes', 
    'banner-b__text-2': 'RSH', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_rsh.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_rsh-mobile.png',
    'banner-b__alt-text': 'Want Free Trees for Your Home?',
}

NVP = NVP_20210125
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
