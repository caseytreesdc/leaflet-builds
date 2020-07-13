import sys


NVP_20200713 = {
    'preheader': 'and a look into the green infrastructure at our HQ',
    'article-1__link': 'https://caseytrees.org/2020/07/did-you-see-popvilles-list-of-the-best-park-garden-small-forest-in-dc-to-sit-and-read-all-day/?utm_source=leaflet&utm_medium=email&utm_campaign=mediamention',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/popville-getaway-300.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/popville-getaway-email.png',
    'article-1__heading': 'Did you see PoPville’s list of the “best park/garden/small forest in DC to sit and read all day?”',
    'article-1__description': 'Do you have any additions?',
    'watering__link': 'https://caseytrees.org/take-action/water/?utm_source=leaflet&utm_medium=email&utm_campaign=wateringalert',
    'watering__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater.png',
    'watering__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/05/WWA_mustwater-responsive.png',
    'watering__alt-text': 'Young trees need plenty of water this week.',
    'article-2__link': 'https://caseytrees.org/2020/07/17-straight-days-above-90-degrees-water-your-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/04/water-email.jpg',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/04/water-resplonsive.jpg',
    'article-2__heading': '17 Straight Days Above 90 Degrees = Water Your Trees!',
    'article-2__description': "Yes, we recommend watering even though there have been downpours. Consistent, slow watering is key!",
    'article-3__link': 'https://caseytrees.org/2020/07/green-features-at-casey-trees-hq/?utm_source=leaflet&utm_medium=email&utm_campaign=rsh',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/caseytrees-hq-160.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/07/caseytrees-hq-email.png',
    'article-3__heading': 'Green Features at Casey Trees HQ',
    'article-3__description': 'Did you know our headquarters in Brookland features a fruit bearing rain garden and a green roof?',
    'banner__link': 'https://caseytrees.org/farm',
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm.png',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/07/Leaflet-ad_farm-responsive.png',
    'banner__alt-text': '',
}

NVP = NVP_20200713
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
