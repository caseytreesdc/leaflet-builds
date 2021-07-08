import sys


NVP_20210706 = {
    'preheader': " Save Some Green, Protect Something Green",
    'article-1__link': 'https://caseytrees.org/2021/07/early-bird-pricing-for-the-urban-tree-summit-ends-july-9/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/07/uts-2021-email-1.png',
    'article-1__heading': 'Early Bird Pricing for the Urban Tree Summit Ends Friday, July 9',
    'article-1__description': 'Whether joining online or in the field, save on registration!',
    'banner-a__link': 'https://caseytrees.org/take-action/water/',
    'banner-a__alt-text': 'Weekly Watering Alert: Water',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water.jpg',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    'banner-a__text-1': 'Weekly Watering Alert',
    'banner-a__text-2': 'Water',
    'article-2__link': 'https://caseytrees.org/2021/07/lets-give-a-warm-welcome-to-alex-kew-our-communications-and-events-associate/?utm_source=leaflet&utm_medium=email&utm_campaign=staff',
    'article-2__alt-text': 'Alex Kew at the Grand Canyon',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/07/alex-kew-email.png',
    'article-2__heading': 'Let’s Give a Warm Welcome to Alex Kew, Our Communications and Events Associate!',
    'article-2__description': 'A former member of our Tree Operations Crew, she is excited to get back in the field and work aside volunteers.',
    'article-3__link': 'https://caseytrees.org/2021/07/summer-reading-black-woman-in-green/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-3__alt-text': 'Gloria Brown on the book cover wearing a bright hard hat',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/07/black-woman-in-green-email.png',
    'article-3__heading': "Summer Reading: Black Woman in Green",
    'article-3__description': 'Gloria Brown and the Unmarked Trail of Forest Service Leadership',
    'banner-b__link': 'https://caseytrees.org/urban-tree-summit-2021/',
    'banner-b__alt-text': 'Early Bird Tickets on Sale! Urban Tree Summit 2021',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/06/Leaflet-ad_uts-eb.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/06/Leaflet-ad_uts-eb-mobile.png',
    'banner-b__text-1': 'Urban Tree Summit', 
    'banner-b__text-2': 'Twentytwentyone',
}

NVP = NVP_20210706
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
