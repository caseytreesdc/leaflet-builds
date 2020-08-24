import sys


NVP_20200817 = {
    'preheader': 'We’re celebrating National Dog Day with a complete canine collection of stories!',
    'article-1__link': 'https://caseytrees.org/2020/08/canopy-cover-at-dog-parks-in-dc/?utm_source=leaflet&utm_medium=email&utm_campaign=gis',
    'article-1__alt-text': 'a lab puppy!',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/dogparks-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/dogparks-email.png',
    'article-1__heading': 'Canopy Cover at Dog Parks in DC',
    'article-1__description': 'Counting down the top 10 puppy play places.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Even with the bit of rain, trees need more water this week.',
    'article-2__link': 'https://caseytrees.org/2020/08/help-trees-survive-the-dog-days-of-summer/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/dogdays-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/dogdays-email.png',
    'article-2__heading': 'Help Trees Survive the Dog Days of Summer',
    'article-2__description': 'Tips on how to help trees make it despite prolonged heat, short and intense rainfall and even lawn maintenance equipment.',
    'article-3__link': 'https://caseytrees.org/2020/08/popular-dogs-as-trees-that-we-can-plant-in-your-yard-for-free/?utm_source=leaflet&utm_medium=email&utm_campaign=residential',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/breedsastrees-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/breedsastrees-email.png',
    'article-3__heading': 'Popular Dogs as Trees (that we can plant in your yard for free!)',
    'article-3__description': 'Which DC tree represents a golden retriever? Or a Corgi?',
    'banner__link': 'https://casey-trees-dc.square.site/product/face-mask-dc-flag/87?cs=true',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner__alt-text': 'Get a Casey Trees Mask! Protect Yourself, Protect others, Protect Our Urban Forester',
}

NVP = NVP_20200817
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
