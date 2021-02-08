import sys


NVP_20210208 = {
    'preheader': 'and we’re celebrating Black History Month all month long',
    'article-1__link': 'https://caseytrees.org/2021/02/spring-outlook-2/?utm_source=leaflet&utm_medium=email&utm_campaign=phenology',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/02/spring-outlook-2021-email.png',
    'article-1__heading': 'Walk on the Wild Side with the Urban Forestry Division',
    'article-1__description': 'If a groundhog can forecast the weather, so can your friendly neighborhood urban forestry nonprofit.',
    'banner-a__text-1': 'DONATE TODAY',
    'banner-a__text-2': "Donate today",
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/212c9142-dfbb-4801-8e11-d0f1b5810fc0',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
    'banner-a__alt-text': "Donate Today",
    'article-2__link': 'https://caseytrees.org/2021/02/black-history-month-tubman-elementary-school/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/02/tubman-email.png',
    'article-2__heading': 'Black History Month: Tubman Elementary School',
    'article-2__description': 'Who are our planting locations named after? We’re finding out.',
    'article-3__link': 'https://caseytrees.org/2021/02/from-the-archive-presidents-and-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/02/tree-pres-email-2.png',
    'article-3__heading': 'From the Archive: Presidents and Trees',
    'article-3__description': 'This President’s Day, enjoy these fun tidbits about presidents and trees.',
    'banner-b__link': 'https://caseytrees.org/2020/02/love-at-casey-trees/',
    'banner-b__text-1': 'LOVE AT CASEY TREES', 
    'banner-b__text-2': 'WHEN TREES BRING PEOPLE TOGETHER', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social-mobile.png',
    'banner-b__alt-text': 'Follow us on social',
}

NVP = NVP_20210208
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
