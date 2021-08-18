import sys


NVP_20210809 = {
    'preheader': 'Coming Soon to Park Near You: DDOT’s Pop Up Arboreta',
    'article-1__link': 'https://caseytrees.org/2021/08/ddots-pop-up-arboreta/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': 'a sign posted on an American Elm (ulmus americana) describing its sawtooth leaves',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/08/ddot-arboretum-email.png',
    'article-1__heading': 'DDOT’s Pop Up Arboreta',
    'article-1__description': 'And experience it for yourself during our Tree Walk with UFD',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water!',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_optional.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_optional-mobile.jpg',
    'article-2__link': 'https://caseytrees.org/2021/08/continuing-education-credits-available-at-the-urban-tree-summit/?utm_source=leaflet&utm_medium=email&utm_campaign=greencitiessummit',
    'article-2__alt-text': 'a stylized gingko and the casey trees and montgomery parks logos',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/07/uts-2021-email-1.png',
    'article-2__heading': 'Continuing Education Credits available at the Urban Tree Summit',
    'article-2__description': 'Grow your knowledge, keep your credentials, and have a great time in September',
    'article-3__link': 'https://caseytrees.org/2021/08/trees-are-feeling-the-heat/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-3__alt-text': 'Dry leaves in the summer hear',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/08/heat-stress-email.png',
    'article-3__heading': 'Trees are Feeling the Heat',
    'article-3__description': 'Lack of water is not the only summertime woe for urban trees.',
    'banner-b__link': 'https://caseytrees.org/urban-tree-summit-2021/',
    'banner-b__alt-text': "Early Access Tickets: Montgomery Parks and Casey Trees Present the Urban Tree Summit",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/08/Leaflet-ad_uts-eb-lastcall.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/08/Leaflet-ad_uts-eb-lastcall-mobile.png',
}

NVP = NVP_20210809
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
