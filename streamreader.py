import sys


NVP_20201102 = {
    'preheader': 'and ideas for a mental health break this week.',
    'article-1__link': 'https://caseytrees.org/2020/11/ideas-for-a-tree-based-mental-health-break/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/fall-mental-break-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/fall-mental-break-email.png',
    'article-1__heading': 'Ideas for a Tree-Based Mental Health Break',
    'article-1__description': 'Days are shorter and darker and the newscycle can be overwhelming. Here are some resources to get up and get out of your head.',
    'watering__link': 'https://caseytreesdc.github.io/ct-farm/',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm-responsive.png',
    'watering__alt-text': 'Check out the Casey Trees Online Store!',
    'article-2__link': 'https://caseytrees.org/2020/11/dont-keep-this-to-yourself-advocacy-starts-with-sharing-or-a-zoom-class-to-make-difference/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/AITD-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/AITD-email.png',
    'article-2__heading': 'Don’t Keep this to Yourself, Advocacy Starts with Sharing',
    'article-2__description': 'Perhaps you have a vocal email chain or Twitter friend? Send them to our upcoming Advocacy in the District class!',
    'article-3__link': 'https://caseytrees.org/2020/11/important-changes-to-dc-leaf-collection/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/leaf-collection-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/10/leaf-collection-email.png',
    'article-3__heading': 'Important Changes to DC Leaf Collection',
    'article-3__description': 'DPW is now asking residents to use paper bags, and not rake leaves into tree boxes.',
    'banner__link': 'https://caseytrees.maps.arcgis.com/apps/webappviewer/index.html?id=c7c2a30d5c95440b8316b12c7add426d',
    'banner_text': 'DONATE TODAY',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_fall-color-map.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_fall-color-map-mobile.png',
    'banner__alt-text': '',
}

NVP = NVP_20201102
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
