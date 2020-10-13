import sys


NVP_20201005 = {
    'preheader': 'and happy Oaktober!',
    'article-1__link': 'https://caseytrees.org/2020/10/take-our-dc-parks-challenge/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/ready2play-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/ready2play-email.png',
    'article-1__heading': 'Take our DC Parks Challenge',
    'article-1__description': 'Help Plan the Future of DC Parks!',
    'watering__link': 'https://caseytrees.maps.arcgis.com/apps/webappviewer/index.html?id=c7c2a30d5c95440b8316b12c7add426d',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_fall-color-map.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/10/Leaflet-ad_fall-color-map-mobile.png',
    'watering__alt-text': 'View our fall color map.',
    'article-2__link': 'https://caseytrees.org/2020/10/feelin-hot-hot-hot-2020-weekly-watering-alert-wrap-up/?utm_source=leaflet&utm_medium=email&utm_campaign=weeklywateringalert',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/wwa-wrapup-2020-browser.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/wwa-wrapup-2020-email.png',
    'article-2__heading': 'Feelin’ Hot, Hot, Hot: 2020 Weekly Watering Alert Wrap Up',
    'article-2__description': 'TL;DR there was so much watering this summer.',
    'article-3__link': 'https://caseytrees.org/2020/10/oaktober-bur-oak/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/10/bur-oak-browser.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/09/bur-oak-email.png',
    'article-3__heading': 'Oaktober: Bur Oak',
    'article-3__description': 'We’re celebrating Oak-tober by highlighting some of the Oak species we can plant for free as part of our residential planting programs.',
    'banner__link': 'https://casey-trees-dc.square.site/product/face-mask-dc-flag/87?cs=true',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner__alt-text': 'Get a Casey Trees Mask! Protect Yourself, Protect others, Protect Our Urban Forester',
}

NVP = NVP_20201005
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
