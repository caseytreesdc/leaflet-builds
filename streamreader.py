import sys


NVP_20210601 = {
    'preheader': "and don't forget Dad!",
    'article-1__link': 'https://caseytrees.org/2021/06/need-a-fathers-day-gift/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'dads and kids',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/06/fathers-day-21-email.png',
    'article-1__heading': 'Need a Father’s Day Gift?',
    'article-1__description': 'Symbolically adopting a tree makes an easy, everlasting gift',
    'banner-ss__link-left' : 'https://caseytrees.org/take-action/water/',
    'banner-ss__alt-left' : 'Weekly Watering Alerts: Watering Optional',
    'banner-ss__image-left' : 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_optional-mobile.jpg',
    'banner-ss__link-right' : 'https://caseytrees.org/2021/05/cicada-resources/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'banner-ss__alt-right' : 'Cicada Updates',
    'banner-ss__image-right' : 'https://caseytrees.org/wp-content/uploads/2021/05/cicada_leaflet.png',
    'article-2__link': 'https://caseytrees.org/2021/06/these-trees-get-you-100/?utm_source=leaflet&utm_medium=email&utm_campaign=rebate',
    'article-2__alt-text': 'row houses and the tree crowns',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/06/tree-rebate-email.png',
    'article-2__heading': 'These Trees Get You $100',
    'article-2__description': 'Among countless other benefits from Oaks and more',
    'article-3__link': 'https://caseytrees.org/2021/06/ornamental-trees-well-plant-for-free/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': 'an ornalmental dogwood',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/05/dogwood-ornamental-rsh-email.png',
    'article-3__heading': "Trees We’ll Plant for Free",
    'article-3__description': 'So many choices, so little time. These showstoppers deliver',
    'banner-b__link': 'https://caseytrees.org/urban-tree-summit-2021/',
    'banner-b__alt-text': "Early Access Tickets: Montgomery Parks and Casey Trees Present the Urban Tree Summit",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/06/Leaflet-ad_uts-eb.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/06/Leaflet-ad_uts-eb-mobile.png',
    'banner-b__text-1': 'TRC', 
    'banner-b__text-2': '2020',
}

NVP = NVP_20210601
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
