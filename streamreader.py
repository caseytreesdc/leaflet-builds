import sys


NVP_20201013 = {
    'preheader': 'and we are the champions!',
    'article-1__link': 'https://caseytrees.org/2020/10/pandemic-planting-progress/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/stocking-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/stocking-email.png',
    'article-1__heading': 'Pandemic Planting Progress',
    'article-1__description': 'Even with a lean staff and enhanced safety protocols, citywide tree planting - through the work of the city’s Urban Forestry Division and us here at Casey Trees - is up! But what will it take to get to our canopy goal?',
    'watering__link': 'https://caseytrees.maps.arcgis.com/apps/webappviewer/index.html?id=c7c2a30d5c95440b8316b12c7add426d',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_fall-color-map.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_fall-color-map-mobile.png',
    'watering__alt-text': 'View our fall color map.',
    'article-2__link': 'https://caseytrees.org/2020/10/2020-champion-tree-register/?utm_source=leaflet&utm_medium=email&utm_campaign=treeinventory',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/nuttall-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/nuttall-email.png',
    'article-2__heading': '2020 Champion Tree Register',
    'article-2__description': 'And where to find DC’s Champion Tree.',
    'article-3__link': 'https://caseytrees.org/2020/10/oaktober-chestnut-oak/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/chestnuut-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/chestnuut-email.png',
    'article-3__heading': 'Oaktober: Chestnut Oak',
    'article-3__description': 'We’re celebrating Oaktober by highlighting some of the Oak species we can plant for free as part of our residential planting programs.',
    'banner__link': 'https://caseytrees.org/plant/residential-planting/',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_rsh.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_rsh-mobile.png',
    'banner__alt-text': 'Want free trees for your home?',
}

NVP = NVP_20201013
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
