import sys


NVP_20210913 = {
    'preheader': 'They’ll go fast people!',
    'article-1__link': 'https://caseytrees.org/2021/09/in-person-fall-events-are-back/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'a pile of shovels!',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/09/summer-treecare-wrap-email.png',
    'article-1__heading': 'In Person Fall Events are Back!',
    'article-1__description': 'Register ASAP, our limited number of spots will go quick!',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/09/make-fall-your-best-season-yet-with-casey-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-2__alt-text': 'a kid playing in the leaves',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/09/fall-email.png',
    'article-2__heading': 'Make Fall Your Best Season Yet with Casey Trees',
    'article-2__description': 'We have everything you need for the best show in town - trees!',
    'article-3__link': 'https://caseytrees.org/2021/09/celebrating-national-hispanic-heritage-month/?utm_source=leaflet&utm_medium=email&utm_campaign=staff',
    'article-3__alt-text': 'Alex Palacios setting up a watering bag',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/09/alex-email.png',
    'article-3__heading': 'Celebrating Hispanic Heritage Month',
    'article-3__description': 'Inspiring the Next Generation of Tree Stewards',
    'banner-b__link': 'https://caseytrees.org/guia-para-el-guardabosques-junior/',
    'banner-b__alt-text': "guias para el guardabosques junior",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/09/Leaflet-button-National-Hispanic-Heritage-Month_desktop.jpg',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/09/Leaflet-button-National-Hispanic-Heritage-Month_mobile.jpg',
}

NVP = NVP_20210913
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
