import sys


NVP_20200727 = {
    'preheader': 'and trees that are the only host for butterflies 🦋',
    'article-1__link': 'https://caseytrees.org/2020/07/butterflies-and-a-bird-and-their-host-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=blog',
    'article-1__alt-text': 'a cedar waxwing wing perched on a cedar branch',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/butter-birds-email-brwoser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/butter-birds-email.png',
    'article-1__heading': 'Butterflies (and a Bird) and their Host Trees',
    'article-1__description': 'Coming soon to a Memorial Park near you - Casey Tree Farm cherries!',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week, despite the rain!.',
    'article-2__link': 'https://caseytrees.org/2020/07/which-tree-wood-make-the-best-bat/?utm_source=leaflet&utm_medium=email&utm_campaign=random',
    'article-2__alt-text': 'Nationals Staium at Dusk',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/nats2020-email-broswer.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/nats2020-email.png',
    'article-2__heading': 'Which Tree Wood Make the Best Bat?',
    'article-2__description': ' In honor of Nats Opening Day last week, check out what trees make MLB bats!',
    'article-3__link': 'https://caseytrees.org/2020/07/which-is-which-dogwood-edition/?utm_source=leaflet&utm_medium=email&utm_campaign=mediamention',
    'article-3__alt-text': 'pink and white dogwoods',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/dogwood-leaflet-email-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/dogwood-leaflet-email-responsive.png',
    'article-3__heading': 'Which is Which: Dogwood Edition',
    'article-3__description': 'Tips on how to differentiate between trees at the species level!',
    'banner__link': 'https://caseytrees.org/farm',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm-responsive.png',
    'banner__alt-text': 'curious about our tree farm?',
}

NVP = NVP_20200727
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
