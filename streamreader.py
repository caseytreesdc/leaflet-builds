import sys


NVP_20210119 = {
    'preheader': 'Since inauguration won’t have people lining the streets due to safety reasons, we’re taking a look at what lines Penn Ave year round - trees!',
    'article-1__link': 'https://caseytrees.org/2021/01/pennsylvania-ave-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=citizenscience',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/01/penn-ave-trees-email.png',
    'article-1__heading': 'Pennsylvania Ave Trees',
    'article-1__description': 'For safety reasons Pennsylvania Ave NW won’t be filled with as many spectators this inauguration, the street is always lined with trees.',
    'banner-a__text-1': 'CASEY TREES IS HIRING.',
    'banner-a__text-2': "Casey Trees' is hiring.",
    'banner-a__link': 'https://caseytrees.org/about-us/jobs-internships/',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
    'banner-a__alt-text': "We're hiring!",
    'article-2__link': 'https://caseytrees.org/2021/01/urban-forestry-podcasts/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/01/podcasts-langdon-email.png',
    'article-2__heading': 'Urban Forestry Podcasts',
    'article-2__description': 'and which one Casey Trees was featured on!',
    'article-3__link': 'https://caseytrees.org/2021/01/time-is-running-out-to-apply-for-the-urban-forestry-fellowship/?utm_source=leaflet&utm_medium=email&utm_campaign=gca-scholarships',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/01/gca-2019-last-call-email.png',
    'article-3__heading': 'Time is Running Out to Apply for the Urban Forestry Fellowship',
    'article-3__description': 'A week left to get those applications for $7,500 in.',
    'banner-b__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    'banner-b__text-1': 'Garden Club of America Scholarship', 
    'banner-b__text-2': 'Garden Club of America Scholarship', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca_v2.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile-2.png',
    'banner-b__alt-text': 'Urban Forestry Student Scholarship sponsored by the Garden Club of America',
}

NVP = NVP_20210119
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
