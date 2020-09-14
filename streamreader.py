import sys


NVP_20200914 = {
    'preheader': 'Where to find, and how to identify, beloved fall foliage right outside your door!',
    'article-1__link': 'https://caseytrees.org/2020/09/a-frontline-fall-forecast/?utm_source=leaflet&utm_medium=email&utm_campaign=staff',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/fall-colors-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/fall-colors-email.png',
    'article-1__heading': 'We Updated our Fall Colors Map',
    'article-1__description': 'With data you can do a lot of things, but we made a Fall Color map to help you make the most of fall foliage without even leaving the city - or your neighborhood!',
    'watering__link': 'https://caseytrees.org/2020/09/we-updated-our-fall-colors-map/?utm_source=leaflet&utm_medium=email&utm_campaign=maps',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'We had some rain, but our trees still need water!.',
    'article-2__link': 'https://caseytrees.org/2020/09/tree-dedications-are-still-on-for-fall/?utm_source=leaflet&utm_medium=email&utm_campaign=dedication',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/member-callout-browsers.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/member-callout-email.png',
    'article-2__heading': 'Tree Dedications are Still on for Fall',
    'article-2__description': 'An opportunity for you to plant a tree in honor of a loved one',
    'article-3__link': 'https://caseytrees.org/2020/09/viva-los-arboles/?utm_source=leaflet&utm_medium=email&utm_campaign=nationalholiday',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/hispanic-heritage-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/hispanic-heritage-email.png',
    'article-3__heading': 'Viva los Árboles',
    'article-3__description': 'From September 15 to October 15, National Hispanic Heritage Month celebrates the histories, cultures, and contributions of our ancestors from Spain, Mexico, the Caribbean and the Americas',
    'banner__link': 'https://casey-trees-dc.square.site/product/face-mask-dc-flag/87?cs=true',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner__alt-text': 'Get a Casey Trees Mask! Protect Yourself, Protect others, Protect Our Urban Forester',
}

NVP = NVP_20200914
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
