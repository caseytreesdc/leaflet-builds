import sys


NVP_20210726 = {
    'preheader': "and calling all Junior Urban Foresters grades K-5",
    'article-1__link': 'https://caseytrees.org/2021/07/sign-up-for-our-two-tree-walks-with-capital-nature/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'holding a casey trees clipboard and investigating leaves',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/07/summer-2021-email.png',
    'article-1__heading': 'Back Up and Running: Register for an Upcoming Event',
    'article-1__description': 'Tree walks are better with friends',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    # 'banner-a__text-1': 'Weekly Watering Alert',
    # 'banner-a__text-2': 'Water',
    'article-2__link': 'https://caseytrees.org/2021/07/junior-urban-forester-tune-up-this-friday/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-2__alt-text': '2 kids looking at a treewise workbook',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/07/treewise-21-email.png',
    'article-2__heading': ' Junior Urban Forester Tune Up This Friday',
    'article-2__description': 'We’re hosting a livestream tune up for grades K-5 to dust off scientific knowledge and put those tree detective skills to work',
    'article-3__link': 'https://caseytrees.org/2021/07/adding-to-our-arsenal-now-offering-rain-gardens/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': 'the Knollwood rain garden',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/07/knollwood-rain-garden-email.png',
    'article-3__heading': "Adding to our Arsenal: Now Offering Rain Gardens",
    'article-3__description': 'A Citybiz article on our partnership with Knollwood Life Plan Community is a great introduction to our latest offering - rain gardens!',
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
