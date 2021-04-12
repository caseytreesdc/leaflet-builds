import sys


NVP_20210329 = {
    'preheader': 'This Arbor Day, we’re delivering the festivities right to your door.',
    'article-1__link': 'https://www.canopyfest.org/?utm_source=leaflet&utm_medium=email&utm_campaign=canopyawards',
    'article-1__alt-text': 'Arbor Day Delivered Ordering is Open',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/04/arborday2021-email.png',
    'article-1__heading': 'Arbor Day Delivered Ordering is Open',
    'article-1__description': 'Don’t miss out on this opportunity to eat delicious food, support your urban canopy and its heroes, celebrate the best day of the year, *and* get a hold of awesome, unique Casey Trees merchandise. ',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/cf568424-cf67-40f9-808b-cdcde7a60f26',
    'banner-a__alt-text': 'Run 4 Mother Earth 5K',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_earth-day-5k.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_earth-day-5k-mobile.png',
    'banner-a__text-1': 'Run', 
    'banner-a__text-2': '4 Mother Earth', 
    'article-2__link': 'https://caseytrees.org/2021/04/casey-trees-talks-to-councilmember-allen/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/10/nuttall-email.png',
    'article-2__heading': 'Casey Trees Talks to Councilmember Allen',
    'article-2__description': 'Hear his thoughts on Heritage trees and the future of tree legislation',
    'article-3__link': 'https://caseytrees.org/2021/04/women-in-forestry-and-the-environment-margaret-pooler/?utm_source=nationalholiday&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/04/margaret-pooler-womens-hist-moth-email.png',
    'article-3__heading': 'Women in Forestry and the Environment: Margaret Pooler',
    'article-3__description': 'Researcher at the US National Arboretum',
    'banner-b__link': 'https://caseytrees.org/about-us/jobs-internships/',
    'banner-b__alt-text': "We're hiring!",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
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
