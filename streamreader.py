import sys


NVP_20210426 = {
    'preheader': 'Weekly Watering Alerts are here too',
    'article-1__link': 'https://caseytrees.org/2021/05/order-our-newest-species-guide/?utm_source=leaflet&utm_medium=email&utm_campaign=onlinestore',
    'article-1__alt-text': 'holding up the casey trees species guide',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/04/species-guide-2021-email.png',
    'article-1__heading': 'Order Our Newest Species Guide',
    'article-1__description': 'Just in time for the City Nature Challenge',
    'banner-a__link': '',
    'banner-a__alt-text': 'Weekly Watering Alert: Water',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    'banner-a__text-1': 'Weekly Watering Alert',
    'banner-a__text-2': 'Water',
    'article-2__link': 'https://caseytrees.org/2021/05/weekly-watering-alerts-return-how-and-when-to-water/?utm_source=leaflet&utm_medium=email&utm_campaign=weeklywateringalerts',
    'article-2__alt-text': 'filling up a casey trees watering bag',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/04/weekly-watering-alerts-2021-email.png',
    'article-2__heading': 'Weekly Watering Alerts Return: How and When to Water',
    'article-2__description': 'Consistent watering is crucial for young trees’ establishment. We tell you how, when, and where to water weekly till October.',
    'article-3__link': 'https://caseytrees.org/2021/05/heritage-tree-versus-special-tree/?utm_source=leaflet&utm_medium=email&utm_campaign=treelegislation',
    'article-3__alt-text': 'a tall birch',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/12/heritage-trees-email.png',
    'article-3__heading': 'Heritage Tree versus Special Tree',
    'article-3__description': 'Breaking down the definitions and differences',
    'banner-b__link': 'https://casey-trees.myshopify.com/',
    'banner-b__alt-text': 'Merch!',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store-mobile.png',
    'banner-b__text-1': 'Merch', 
    'banner-b__text-2': 'Merch',
}

NVP = NVP_20210426
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
