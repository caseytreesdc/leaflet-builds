import sys


NVP_20200803 = {
    'preheader': 'and August is Tree Check Month!',
    'article-1__link': 'https://caseytrees.org/2020/08/keep-your-drinks-and-dcs-trees-cool-with-our-custom-yetis/?utm_source=leaflet&utm_medium=email&utm_campaign=store',
    'article-1__alt-text': 'the casey trees x yeti with a pitcher of lemonade!',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/yeti-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/yeti-email.png',
    'article-1__heading': 'Keep Your Drinks (and DC’s Trees!) Cool with Our Custom Yetis',
    'article-1__description': 'Another tree-riffic addition to our store.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Even with the bit of rain, trees need more water this week.',
    'article-2__link': 'https://caseytrees.org/2020/08/garden-centers-and-nurseries-of-the-dmv/?utm_source=leaflet&utm_medium=email&utm_campaign=caseytreefarm',
    'article-2__alt-text': 'blues skies at the farm',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/farm-rebate-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/farm-rebate-email.png',
    'article-2__heading': 'Our Favorite Tree Nursery in the DMV',
    'article-2__description': 'and how to get $100 back when you plant a tree.',
    'article-3__link': 'https://caseytrees.org/2020/08/august-is-tree-check-month-2/?utm_source=leaflet&utm_medium=email&utm_campaign=feeforservice',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/tree-check-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/08/tree-check-email.png',
    'article-3__heading': 'August is Tree Check Month',
    'article-3__description': 'See something concerning? Our arborists are available!',
    'banner__link': 'https://casey-trees-dc.square.site/product/junior-urban-forester-package/85?cs=true',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Leaflet-ad_TREEWISE.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/Leaflet-ad_TREEWISE.png',
    'banner__alt-text': 'at-home learning for kids',
}

NVP = NVP_20200803
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
