import sys


NVP_20211108 = {
    'preheader': 'plus, witness trees to mark Veteran’s Day',
    'article-1__link': 'https://caseytrees.org/2021/11/big-budget-wins-for-2022/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-1__alt-text': 'cyclists going by fall trees on dc citybikes',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/11/budget-wins-email.png',
    'article-1__heading': 'Big Budget Wins for 2022',
    'article-1__description': 'There is so much helpful tree information on the internet, you simply need to know where to look',
    'banner-a__link': 'https://caseytrees.org/plant/#plantitforward',
    'banner-a__alt-text': 'Plant it Forward: Hire Casey Trees',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/11/ddot-maps-you-may-have-missed/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-2__alt-text': "map of UFD's stree trees",
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/11/ddot-maps-emails.png',
    'article-2__heading': 'DDOT Maps You May Have Missed',
    'article-2__description': 'There is so much helpful tree information on the internet, you simply need to know where to look',
    'article-3__link': 'https://caseytrees.org/2021/11/five-witness-trees-for-veterans-day-3/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-3__alt-text': 'a witness tree',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/11/witness-trees-email.png',
    'article-3__heading': 'Five Witness Trees for Veteran’s Day',
    'article-3__description': 'While they may look like ordinary trees, they have incredible stories to tell',
    'banner-b__link': 'http://www.facebook.com/pages/Casey-Trees/58793928339',
    'banner-b__alt-text': "follow us on facebook",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social-mobile.png',
}

NVP = NVP_20211108
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
