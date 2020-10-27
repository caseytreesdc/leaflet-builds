import sys


NVP_20201026 = {
    'preheader': 'Plus, how trees, kids, and Casey Trees are resilient.',
    'article-1__link': 'https://caseytrees.org/2020/10/elag/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/elag-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/elag-email.png',
    'article-1__heading': 'Coming Soon to a Classroom Near You: Casey Trees!',
    'article-1__description': 'More on our work through the Environmental Literacy Advancement Grant also known as ELAG.',
    'watering__link': 'https://casey-trees-dc.square.site/',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'watering__alt-text': 'Check out the Casey Trees Online Store!',
    'article-2__link': 'https://caseytrees.org/2020/10/unbe-leaf-ably-creative-costumes-for-halloween/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/halloween-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/halloween-email.png',
    'article-2__heading': 'Unbe-leaf-ably Creative Costumes for Halloween',
    'article-2__description': 'Let’s go all in on holiday joy this year shall we?',
    'article-3__link': 'https://caseytrees.org/2020/10/20460/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/overcup-broswer.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/overcup-email.png',
    'article-3__heading': 'Oaktober: Overcup Oak',
    'article-3__description': 'We’re celebrating Oaktober by highlighting some of the Oak species we can plant for free as part of our residential planting programs.',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/212c9142-dfbb-4801-8e11-d0f1b5810fc0?utm_source=leaflet&utm_medium=email&utm_campaign=membership&trk=leaflet&_ga=2.73358995.129279305.1601908695-656825217.1588074983',
    'banner_text': 'DONATE TODAY',
    'banner__image-browser': '',
    'banner__image-responsive': '',
    'banner__alt-text': '',
}

NVP = NVP_20201026
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
