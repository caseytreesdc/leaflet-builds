import sys


NVP_20210510 = {
    'preheader': "and the top 10 trees of 2020!",
    'article-1__link': 'https://caseytrees.org/2021/05/celebrating-asian-american-and-pacific-islander-aapi-heritage-month-through-cherry-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-1__alt-text': 'the "Japanese Lantern" statue at the Tidal Basin, lighted during the Cherry Blossom festival.',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/05/aapi-cherry-blossoms-email.png',
    'article-1__heading': 'Celebrating Asian American and Pacific Islander (AAPI) Heritage Month through Cherry Trees',
    'article-1__description': 'Our city’s claim to fame is thanks to a Japanese gift of friendship',
    # 'banner-a__link': 'https://caseytrees.org/2021/05/cicada-resources/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    # 'banner-a__alt-text': 'Weekly Watering Alert: Water and Cicada Resources',
    # 'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-and-cicada.png',
    # 'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-and-cicada.png',
    # 'banner-a__text-1': 'Weekly Watering Alert: Water',
    # 'banner-a__text-2': 'Cicada Resources',
    'banner-ss__link-left' : 'https://caseytrees.org/take-action/water/',
    'banner-ss__alt-left' : 'Weekly Watering Alerts: Must Water',
    'banner-ss__image-left' : 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    'banner-ss__link-right' : 'https://caseytrees.org/2021/05/cicada-resources/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'banner-ss__alt-right' : 'Cicada Updates',
    'banner-ss__image-right' : 'https://caseytrees.org/wp-content/uploads/2021/05/cicada_leaflet.png',
    'article-2__link': 'https://caseytrees.org/2021/05/what-are-dcs-trees-worth/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-2__alt-text': 'The Washington Monument across the water with someone wake boarding by.',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/08/intl-day-of-forests-19-email.png',
    'article-2__heading': 'What are DC’s Trees Worth?',
    'article-2__description': 'The literal, monetary value of trees and some quantifiable impacts',
    'article-3__link': 'https://caseytrees.org/2021/05/top-10-most-wanted-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': 'flowering residential tree in front of row houses',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/05/top-ten-residential-trees-email.png',
    'article-3__heading': 'Top 10 Most Wanted Trees',
    'article-3__description': 'The good kind! Here are our most popularly planted trees of the past year',
    'banner-b__link': 'https://caseytreesdc.github.io/treereportcard2020/',
    'banner-b__alt-text': "The 13th Annual Tree Report Card: The State of DC's Trees in 2020",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/trc2020_leaflet.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/trc2020_leaflet.png',
    'banner-b__text-1': 'TRC', 
    'banner-b__text-2': '2020',
}

NVP = NVP_20210510
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
