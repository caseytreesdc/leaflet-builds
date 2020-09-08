import sys


NVP_20200831 = {
    'preheader': 'Plus, a fall forecast.',
    'article-1__link': 'https://caseytrees.org/2020/09/a-frontline-fall-forecast/?utm_source=leaflet&utm_medium=email&utm_campaign=staff',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/member-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/member-email.png',
    'article-1__heading': 'A Frontline Fall Forecast',
    'article-1__description': 'We’re following safety precautions while continuing to carry out our mission. Which in the Fall means planting trees!',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'We had some rain, but our trees still need water!.',
    'article-2__link': 'https://caseytrees.org/2020/09/the-monetary-value-of-dcs-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=itreeeco',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/intl-day-of-forests-19-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/intl-day-of-forests-19-email.png',
    'article-2__heading': 'The Monetary Value of DC’s Trees',
    'article-2__description': 'They’re so much more than a pretty face.',
    'article-3__link': 'https://caseytrees.org/2020/09/were-hiring-an-urban-forester-and-an-urban-forester-crew-chief/?utm_source=leaflet&utm_medium=email&utm_campaign=jobs',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/hiring-2018-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/hiring-2018-email.png',
    'article-3__heading': 'We’re Hiring an Urban Forester and an Urban Forester Crew Chief',
    'article-3__description': 'Could it be you?',
    'banner__link': 'https://casey-trees-dc.square.site/product/face-mask-dc-flag/87?cs=true',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner__alt-text': 'Get a Casey Trees Mask! Protect Yourself, Protect others, Protect Our Urban Forester',
}

NVP = NVP_20200831
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
