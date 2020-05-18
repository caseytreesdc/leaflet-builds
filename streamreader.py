import sys


NVP_20200518= {
    'preheader': 'Plus, see who won the Urban Tree World Cup',
    'article-1__link': 'https://caseytrees.org/2020/05/go-behind-the-scenes-at-casey-trees-with-tea-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'Go Behind the Scenes at Casey Trees with Tea & Trees!',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/tea-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/tea-responsive.png',
    'article-1__heading': 'Go Behind the Scenes at Casey Trees with Tea & Trees!',
    'article-1__description': 'Get to know Casey Trees staff and fun tree facts in our newest, shortest, video series yet.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_optional.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_optional-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/05/2019-tree-report-card-empowering-future-generations-through-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=treereportcard',
    'article-2__alt-text': 'Empowering future generations through trees.',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/trc-youth-spotlight-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/trc-youth-spotlight-responsive.png',
    'article-2__heading': '2019 Tree Report Card: Empowering Future Generations Through Trees',
    'article-2__description': "When we teach younger generations about the value of trees and green space now, we will ensure that our city’s lush tree filled legacy continues.",
    'article-3__link': 'https://caseytrees.org/2020/05/urban-tree-world-cup/?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-3__alt-text': 'Urban Tree World Cup',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/urban-tree-world-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/urban-tree-world-champ-responsive.png',
    'article-3__heading': 'Urban Tree World Cup',
    'article-3__description': 'London plane knocked out the Dawn redwood in the knock-out tournament run by the Arboricultural Association during lockdown on Twitter.',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/b7852b67-4119-4738-bb07-db98ef6eaee4?637139852829640420&_ga=2.252713097.1890199852.1589214584-173857063.1587570366?trk=leaflet',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad-mobile.png',
    'banner__alt-text': 'Plant it Forward',
}

NVP = NVP_20200518
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
