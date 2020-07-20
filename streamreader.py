import sys


NVP_20200720 = {
    'preheader': 'PREHEADER',
    'article-1__link': 'https://caseytrees.org/2020/07/were-growing-cherry-trees-for-the-national-parks-service/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': 'little cherry blossom buds ',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/cherries-browser-email.jpg',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/cherries-browser-email.jpg',
    'article-1__heading': 'We’re Growing Cherry Trees for the National Parks Service',
    'article-1__description': 'Coming soon to a Memorial Park near you - Casey Tree Farm cherries!',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/07/five-late-blooming-trees-to-spice-up-your-summer/?utm_source=leaflet&utm_medium=email&utm_campaign=rsh',
    'article-2__alt-text': 'a crepe myrtle!',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/late-bloom-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/late-bloom-email.png',
    'article-2__heading': 'Five Late Blooming Trees to Spice Up Your Summer',
    'article-2__description': 'Because who says all the beautiful blooms are in the spring!',
    'article-3__link': 'https://caseytrees.org/2020/07/which-is-which-dogwood-edition/?utm_source=leaflet&utm_medium=email&utm_campaign=rsh',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/dogwood-browser-emali.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/dogwood-email.png',
    'article-3__heading': 'Which is Which: Dogwood Edition',
    'article-3__description': 'Tips on how to differentiate between trees at the species level!',
    'banner__link': 'https://caseytrees.org/farm',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm-responsive.png',
    'banner__alt-text': 'curious about our tree farm?',
}

NVP = NVP_20200720
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
