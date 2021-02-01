import sys


NVP_20210125 = {
    'preheader': 'Plus, the future of urban forestry',
    'article-1__link': 'https://caseytrees.org/2021/01/whats-the-future-of-tree-planting-in-dc/?utm_source=leaflet&utm_medium=email&utm_campaign=conservation',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/01/small-shade-email.png',
    'article-1__heading': 'What’s the future of tree planting in DC?',
    'article-1__description': 'Looking at where we need to go to get to 40%',
    'banner-a__text-1': 'CASEY TREES IS HIRING.',
    'banner-a__text-2': "Casey Trees' is hiring.",
    'banner-a__link': 'https://caseytrees.org/about-us/jobs-internships/',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
    'banner-a__alt-text': "We're hiring!",
    'article-2__link': 'https://caseytrees.org/2021/01/casey-trees-faqs/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/01/faq-email.png',
    'article-2__heading': 'Casey Trees FAQs',
    'article-2__description': 'We’re answering some common questions',
    'article-3__link': 'https://caseytrees.org/2021/01/the-nine-lives-of-christmas-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=rsh',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/12/christmas-trees-email.png',
    'article-3__heading': 'The Nine Lives of Christmas Trees',
    'article-3__description': 'They’re not all destined for the woodchipper',
    'banner-b__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    'banner-b__text-1': 'Garden Club of America Scholarship', 
    'banner-b__text-2': 'Garden Club of America Scholarship', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca_v2.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile-2.png',
    'banner-b__alt-text': 'Urban Forestry Student Scholarship sponsored by the Garden Club of America',
}

NVP = NVP_20210125
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
