import sys


NVP_20210809 = {
    'preheader': 'and it’s the last call for the virtual Urban Tree Summit',
    'article-1__link': 'https://caseytrees.org/2021/08/virtual-urban-tree-summit-last-call/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'a stylized ginkgo',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/07/uts-2021-email-1.png',
    'article-1__heading': 'Virtual Urban Tree Summit Last Call',
    'article-1__description': 'Earn those CEUs, connect with cool, like minded folks, and join us September 8',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water.',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    'article-2__link': 'https://caseytrees.org/2021/08/trees-for-our-changing-climate/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-2__alt-text': 'a child holding a casey trees clipboard and a pencil looking up at a tree',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/08/near-near-schools-email.png',
    'article-2__heading': 'Nature Near Schools Program',
    'article-2__description': 'Our Greenspace Mapping course will help connect students and teachers to their watershed and its greenspaces',
    'article-3__link': 'https://caseytrees.org/2021/08/we-made-pawpaw-muffins/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': '3 pawpaws in a tree',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/09/pawpaw-party-email.png',
    'article-3__heading': 'We Made Pawpaw Muffins',
    'article-3__description': 'With this regional delicacy planted in your yard, the possibilities are endless',
    'banner-b__link': 'https://caseytrees.org/urban-tree-summit-2021/',
    'banner-b__alt-text': "Tickets: Montgomery Parks and Casey Trees Present the Urban Tree Summit",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/08/Leaflet-ad_uts-tickets.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/08/Leaflet-ad_uts-tickets-mobile.png',
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
