import sys


NVP_20210305 = {
    'preheader': "#PeakBloom will be here before you know it too",
    'article-1__link': 'https://caseytrees.org/2021/03/brood-x-is-on-its-way/?utm_source=leaflet&utm_medium=email&utm_campaign=phenology',
    'article-1__alt-text': '2 Cicadas on a branch',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/02/brood-x-cicada-email.png',
    'article-1__heading': 'Brood X is on its way',
    'article-1__description': 'You get a front row seat to one of nature’s most remarkable phenomenons',
    'banner-a__link': '',
    'banner-a__alt-text': "Happy International Women's Day",
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_canopy-awards-save-the-date-teaser-v2.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_canopy-awards-save-the-date-teaser-mobile-v2.png',
    'banner-a__text-1': 'Foresters to Recognize!', 
    'banner-a__text-2': "INTERNATIONAL WOMEN'S DAY 2021", 
    'article-2__link': 'https://caseytrees.org/2021/03/nps-predicts-an-april-peak-bloom/?utm_source=leaflet&utm_medium=email&utm_campaign=phenology',
    'article-2__alt-text': 'more blooms',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/03/peak-bloom-email.png',
    'article-2__heading': 'So is Peak Bloom',
    'article-2__description': 'You get a front row seat to another one of our city’s most remarkable phenomenons',
    'article-3__link': 'https://caseytrees.org/2021/03/tree-rainbow-yellow-and-green-blooms/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': 'yellow and green blooms',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/03/tuliptree-email.png',
    'article-3__heading': 'Tree Rainbow: Yellow and Green Blooms',
    'article-3__description': 'Bring the rainbow to your yard with our free trees!',
    'banner-b__link': 'https://caseytrees.org/2017/03/run-world-famous-female-foresters/',
    'banner-b__alt-text': '',
    'banner-b__image-browser': '',
    'banner-b__image-responsive': '',
    'banner-b__text-1': 'Foresters to Recognize!',
    'banner-b__text-2': "INTERNATIONAL WOMEN'S DAY 2021",
}

NVP = NVP_20210305
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
