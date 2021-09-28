import sys


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
