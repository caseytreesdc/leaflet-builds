import sys


NVP_20200518 = {
    'preheader': 'Rapinoe was a close runner up.',
    'article-1__link': 'https://caseytrees.org/2020/05/urban-tree-world-cup/?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-1__alt-text': 'Urban Tree World Cup',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/urban-tree-world-champ-update.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/urban-tree-world-champ-update.png',
    'article-1__heading': 'Urban Tree World Cup',
    'article-1__description': 'London plane knocked out the Dawn redwood in the knock-out tournament run by the Arboricultural Association during lockdown on Twitter.',
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
    'article-3__link': 'https://caseytrees.org/2020/05/serviceberry-season-is-almost-here/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': 'Serviceberry Season is (almost!) Here',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/serviceberry-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/serviceberry-email.png',
    'article-3__heading': 'Serviceberry Season is (almost!) Here',
    'article-3__description': 'What we’re making with the best berry you’ve never heard about.',
    'banner__link': 'https://www.tfaforms.com/4826832',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/leaflet-youth-programs-2020.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/leaflet-youth-programs-2020.png',
    'banner__alt-text': 'youth programs survey',
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
