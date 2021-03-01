import sys


NVP_20210301 = {
    'preheader': 'Some of these trees are even blooming right now!',
    'article-1__link': 'https://caseytrees.org/2021/03/find-spring-blooms-near-you-with-our-blooming-tree-map/?utm_source=leaflet&utm_medium=email&utm_campaign=maps',
    'article-1__alt-text': 'Current blooms',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2020/04/trees-of-note-update-responsive.png',
    'article-1__heading': 'Find Spring Blooms Near You with Our Blooming Tree Map',
    'article-1__description': 'When you open your eyes to all the beautiful blooms DC’s trees offer, you start to see that there is so much more than those delicate white flowers of the Yoshino cherry.',
    'banner-a__link': 'https://www.eventbrite.com/e/native-trees-for-your-garden-and-neighborhood-tickets-141387982261',
    'banner-a__alt-text': 'Register for Native Trees, Presented by Capital Nature',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_capital-nature-event.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_capital-nature-event-mobile.png',
    'banner-a__text-1': 'REGISTER FOR NATIVE TREES:', 
    'banner-a__text-2': 'PRESENTED BY CAPTIAL NATURE', 
    'article-2__link': 'https://caseytrees.org/2021/03/tree-rainbow-red-and-orange-blooms/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-2__alt-text': 'more blooms',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/02/rainbow-red-maple-email.png',
    'article-2__heading': 'Tree Rainbow: Red and Orange Blooms',
    'article-2__description': 'Bring the rainbow to your yard with our free trees!',
    'article-3__link': 'https://caseytrees.org/2021/03/trees-on-structure-and-amazons-hq2/?utm_source=leaflet&utm_medium=email&utm_campaign=store',
    'article-3__alt-text': 'Trees on structures',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/02/HQ2-email.png',
    'article-3__heading': 'Trees on Structures and Amazon’s HQ2',
    'article-3__description': 'We’re way ahead of you Bezos. ',
    'banner-b__link': 'https://casey-trees.myshopify.com/',
    'banner-b__alt-text': 'Browse our new store',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store-mobile.png',
    'banner-b__text-1': 'STORE',
    'banner-b__text-2': 'STORE',
}

NVP = NVP_20210301
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
