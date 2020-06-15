import sys


NVP_20200518 = {
    'preheader': 'Juneteenth, and Summer in DC',
    'article-1__link': 'https://caseytrees.org/2020/06/socially-distant-nature-based-ways-to-mark-juneteenth/?utm_source=leaflet&utm_medium=email&utm_campaign=blog',
    'article-1__alt-text': 'Juneteenth',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/06/juneteenth-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/juneteenth-responsive.png',
    'article-1__heading': 'Socially Distant, Nature Based Ways to Mark Juneteenth',
    'article-1__description': 'And some history if you’re unfamiliar with the holiday.',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/06/bees-n-trees-celebrate-pollinator-week-with-these-helpful-trees-2/?utm_source=leaflet&utm_medium=email&utm_campaign=blog',
    'article-2__alt-text': 'pollinator week',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/06/pollinator-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/pollinator-responsive.png',
    'article-2__heading': 'Bees n Trees: Celebrate Pollinator Week with These Helpful Trees',
    'article-2__description': "National Pollinator Week is a time to celebrate pollinators and spread the word about what you can do to protect them.",
    'article-3__link': 'https://caseytrees.org/2020/06/parks-are-back-open-revisit-their-history-and-trees-with-our-storymaps/?utm_source=leaflet&utm_medium=email&utm_campaign=blog',
    'article-3__alt-text': 'History and Trees with Our Storymaps',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/06/parks-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/06/parks-responsive.png',
    'article-3__heading': 'Parks are Back Open, Revisit their History and Trees with Our Storymaps!',
    'article-3__description': "A win-win-win for trees, parks, and people.",
    'banner__link': 'https://www.tfaforms.com/4826832',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/leaflet-youth-programs-2020.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/leaflet-youth-programs-2020.png',
    'banner__alt-text': 'youth programs survey',
}

NVP = NVP_20200518
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
