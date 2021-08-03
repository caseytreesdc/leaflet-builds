import sys


NVP_20210726 = {
    'preheader': "And did we hit our goal of watering 1.5k trees?",
    'article-1__link': 'https://caseytrees.org/2021/08/urban-tree-summit-agenda-is-here/?utm_source=leaflet&utm_medium=email&utm_campaign=greencitiessummit',
    'article-1__alt-text': 'a stylized gingko',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/07/uts-2021-email-1.png',
    'article-1__heading': 'Urban Tree Summit Agenda is Here',
    'article-1__description': 'Early bird pricing ends August 13',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Optional',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_optional.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_optional-mobile.png',
    # 'banner-a__text-1': 'Weekly Watering Alert',
    # 'banner-a__text-2': 'Water',
    'article-2__link': 'https://caseytrees.org/2021/08/1500-raised-1500-trees-watered-1-soaked-casey-trees-employee/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': 'watering 1500 trees!',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/08/1500-trees-email.png',
    'article-2__heading': '$1,500 Raised, 1,500 Trees Watered, 1 Soaked Employee',
    'article-2__description': 'We put out the call: if we raise $1,500 and water 1,500 trees in one day, we’ll water a Casey Trees employee. See what happened next.',
    'article-3__link': 'https://caseytrees.org/2021/08/what-to-do-when-a-storm-rolls-through/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-3__alt-text': 'a huge broken branch from the storms',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/08/Pre-and-post-storm-resources-email.png',
    'article-3__heading': "What To Do When a Storm Rolls Through",
    'article-3__description': 'Resources for before and after',
    'banner-b__link': 'https://caseytrees.org/urban-tree-summit-2021/',
    'banner-b__alt-text': "Early Access Tickets: Montgomery Parks and Casey Trees Present the Urban Tree Summit",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/06/Leaflet-ad_uts-eb.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/06/Leaflet-ad_uts-eb-mobile.png',
    # 'banner-b__text-1': 'follow us on social', 
    # 'banner-b__text-2': 'Social',
}

NVP = NVP_20210726
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
