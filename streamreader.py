import sys


NVP_20210329 = {
    'preheader': '#ArborDayDelivered Merch: the Latest and Greatest in Casey Trees Style',
    'article-1__link': 'https://caseytrees.org/2021/04/did-you-see-the-arbordaydelivered-merch-packs/?utm_source=leaflet&utm_medium=email&utm_campaign=canopyawards',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/04/hatv_v2.gif',
    'article-1__heading': 'Did You See the #ArborDayDelivered Merch Packs?',
    'article-1__description': 'Support us if you don’t within the meal delivery zone and get sweet swag',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/cf568424-cf67-40f9-808b-cdcde7a60f26',
    'banner-a__alt-text': 'Run 4 Mother Earth 5K',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_earth-day-5k.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_earth-day-5k-mobile.png',
    'banner-a__text-1': 'Run', 
    'banner-a__text-2': '4 Mother Earth', 
    'article-2__link': 'https://caseytrees.org/2021/04/casey-trees-testifies-on-dc-agency-performance/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/12/heritage-trees-email.png',
    'article-2__heading': 'Casey Trees Testifies on DC Agency Performance',
    'article-2__description': 'We commented on the performance of 12 different agencies, but asked for three main things. Here’s what they are.',
    'article-3__link': 'https://caseytrees.org/2021/04/tree-id-walks-in-april-and-may/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/04/tree-walk-2021-email.png',
    'article-3__heading': 'Tree ID Walks in April and May',
    'article-3__description': 'Join Casey Trees staff to learn key characteristics of the trees that make up our urban canopy',
    'banner-b__link': '',
    'banner-b__alt-text': "Save the Date, Arbor Day, April 30, 2021",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_canopy-awards-save-the-date-teaser-v2.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_canopy-awards-save-the-date-teaser-mobile-v2.png',
    'banner-b__text-1': 'We Are',
    'banner-b__text-2': 'Hiring',
}

NVP = NVP_20210329
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
