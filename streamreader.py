import sys


NVP_20200831 = {
    'preheader': 'A book recommendation, a virtual annual meeting, and more exciting, pandemic friendly activities.',
    'article-1__link': 'https://caseytrees.org/2020/08/mac-isa-2020-annual-meeting/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/MAC-ISA-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/MAC-ISA-email.png',
    'article-1__heading': 'MAC-ISA 2020 Annual Meeting ',
    'article-1__description': 'Take advantage of varied and creative programming, CEUs, and networking opportunities during a pandemic.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_optional.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_optional-responsive.png',
    'watering__alt-text': 'We had some rain, water if you need, but trees are hydrated!.',
    'article-2__link': 'https://caseytrees.org/2020/08/black-woman-in-green/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/BWING-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/BWING-email.png',
    'article-2__heading': 'Black Woman in Green',
    'article-2__description': 'Marking the passage of the 19th Amendment, while learning more about our own field.',
    'article-3__link': 'https://caseytrees.org/2020/08/a-new-era-on-12th-street-ne/?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-3__alt-text': 'Gloria Brown and the Inmarked Trail to Forest Service LEadership',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/annex-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/annex-email.png',
    'article-3__heading': 'A New Era on 12th Street NE',
    'article-3__description': 'Looking back before looking forward.',
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
