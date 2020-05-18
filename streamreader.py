import sys


NVP_20200511 = {
    'preheader': 'Discounts on Tree Adoptions continue, plus help collect data!',
    'article-1__link': 'https://caseytreesdc.github.io/ct-videos/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'Casey Trees Remote! ',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/ct-remote-bowesr.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/ct-remote-responsleeve.png',
    'article-1__heading': 'New Your City, Your Trees Class & Other Remote Ways to Engage With Us!',
    'article-1__description': 'For when you are bored in the house and in the house bored.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/05/take-a-survey-on-nature-and-human-well-being-in-times-of-isolation-and-a-global-pandemic/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-2__alt-text': 'a survey on nature and our well-being',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/ubc-forestry-survey-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/ubc-forestry-survey-responsive.png',
    'article-2__heading': 'Take a Survey on Nature and Human Well-Being in Times of Isolation and Global Pandemic',
    'article-2__description': "Help out an old intern's new project!",
    'article-3__link': 'https://caseytrees.org/2020/05/tree-adoptions-are-still-discounted-for-mothers-day/?utm_source=leaflet&utm_medium=email&utm_campaign=store',
    'article-3__alt-text': "smell the gingko tree",
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/mothers-day-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/05/mothers-day-responsive.png',
    'article-3__heading': 'Say What You Need to Say! Tree Adoptions Remain Discounted!',
    'article-3__description': 'Show mom, friends, family, ANYONE how much they mean by sending them a tree adoption that helps plant MORE trees!',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/b7852b67-4119-4738-bb07-db98ef6eaee4?637139852829640420&_ga=2.252713097.1890199852.1589214584-173857063.1587570366?trk=leaflet',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/04/Leaflet-ad-mobile.png',
    'banner__alt-text': 'Plant it Forward',
}

NVP = NVP_20200511
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
