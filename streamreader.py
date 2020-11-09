import sys


NVP_20201109 = {
    'preheader': 'Plus, earn CEUs, and witnesses to history.',
    'article-1__link': 'https://caseytrees.org/2020/11/urban-tree-summit/?utm_source=leaflet&utm_medium=email&utm_campaign=greencitiessummit',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/urbantreesummit-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/urbantreesummit-email.png',
    'article-1__heading': 'Urban Tree Summit',
    'article-1__description': 'For the future health and welfare of our urban and suburban trees.',
    'watering__link': 'https://caseytrees.org/2020/11/dont-keep-this-to-yourself-advocacy-starts-with-sharing-or-a-zoom-class-to-make-difference/',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_aitd.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_aitd-mobile.png',
    'watering__alt-text': 'Check out the Casey Trees Online Store!',
    'article-2__link': 'https://caseytrees.org/2020/11/magical-maples/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/maples-browser-1.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/maples-email.png',
    'article-2__heading': 'Magical Maples',
    'article-2__description': 'True stunners of Autumn.',
    'article-3__link': 'https://caseytrees.org/2020/11/five-witness-trees-for-veterans-day-2/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/witness-trees-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/witness-trees-email.png',
    'article-3__heading': 'Five Witness Trees for Veteran’s Day',
    'article-3__description': 'Witness trees are those considered to have been present, and therefore would have been witness to, at key historical events.',
    'banner__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    # banner_text if the delimited is 10-26-2020
    # banner_image if the delimited is 08-10-2020
    'banner_text': 'DONATE TODAY', 
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile.png',
    'banner__alt-text': '',
}

NVP = NVP_20201109
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
