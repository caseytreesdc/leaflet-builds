import sys


<<<<<<< HEAD
NVP_20210927 = {
    'preheader': 'The Urban Forestry Division has a treasure trove of maps for residents',
    'article-1__link': 'https://caseytrees.org/2021/09/casey-trees-headquarters-street-tree-tour/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': 'casey trees headquarters',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/09/street-tree-tour-email.png',
    'article-1__heading': 'Casey Trees Headquarters Street Tree Tour',
    'article-1__description': 'The Urban Forestry Division has been hard at work outside and creating valuable resources for the public!',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/09/urban-tree-summit-2021-recap-back-and-better-than-before/?utm_source=leaflet&utm_medium=email&utm_campaign=urbantreesummit',
    'article-2__alt-text': 'a crowd gathered at langdon park',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/09/uts-recap-2021-email.png',
    'article-2__heading': 'Urban Tree Summit 2021 Recap: Back and Better than Before',
    'article-2__description': 'Hear our favorite parts of each session',
    'article-3__link': 'https://caseytrees.org/2021/09/treewise-2021-summer-recap/?utm_source=leaflet&utm_medium=email&utm_campaign=treewise',
    'article-3__alt-text': 'what i enjoy outside is the wonderful trees and leafs - a drawing of a red maple with markers',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/09/treewise-summer-2021-recap-email.png',
    'article-3__heading': 'TreeWise 2021 Summer Recap',
    'article-3__description': 'We were so thankful to be back in person with the next generation of tree stewards',
    'banner-b__link': 'https://caseytrees.org/guia-para-el-guardabosques-junior/',
    'banner-b__alt-text': "guias para el guardabosques junior",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/09/Leaflet-button-National-Hispanic-Heritage-Month_desktop.jpg',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/09/Leaflet-button-National-Hispanic-Heritage-Month_mobile.jpg',
}

NVP = NVP_20210927
=======
NVP_20211018 = {
    'preheader': 'plus, Urban Forestry Fellowship Now Accepting Applications',
    'article-1__link': 'https://caseytrees.org/2021/10/street-tree-before-afters/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': 'street trees, before and after',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/10/street-tree-before-after-email-1.png',
    'article-1__heading': 'Street Tree Before and Afters',
    'article-1__description': 'A satisfying look at our ever-changing urban landscape.',
    'banner-a__link': 'https://caseytrees.org/plant/#plantitforward',
    'banner-a__alt-text': 'Plant it Forward: Hire Casey Trees',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/10/urban-forestry-fellowship-now-accepting-applications/?utm_source=leaflet&utm_medium=email&utm_campaign=gcascholarship',
    'article-2__alt-text': 'what is a riparian buffer',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/10/gca-2019-email.png',
    'article-2__heading': 'Urban Forestry Fellowship Now Accepting Applications',
    'article-2__description': 'Offset the cost of undergraduate or graduate school research thanks to our partnership with the Garden Club of America',
    'article-3__link': 'https://caseytrees.org/2021/10/riparian-buffer-month/?utm_source=leaflet&utm_medium=email&utm_campaign=feeforservice',
    'article-3__alt-text': 'rock creek parkway and the duke ellington bridg',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/10/riparian-planting-email.png',
    'article-3__heading': 'Riparian Buffer Month',
    'article-3__description': 'Highlighting a riverside project and the importance of building in green buffers to improve our waterways',
    'banner-b__link': 'https://www.eventbrite.com/e/community-tree-planting-oxon-run-park-tickets-181977558777?_eboga=1915616282.1634306680&_ga=2.187267755.2091215710.1634564602-1915616282.1634306680',
    'banner-b__alt-text': "Oxon Run CTP: Team Leaders Needed",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_oxon-run-desktop.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_oxon-run-mobile.png',
}

NVP = NVP_20211018
>>>>>>> develop
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
