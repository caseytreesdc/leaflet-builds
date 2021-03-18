import sys


NVP_20210315 = {
    'preheader': "And an update from our Executive Director",
    'article-1__link': 'https://caseytrees.org/2021/03/a-note-from-executive-director-mark-buscaino/?utm_source=leaflet&utm_medium=email&utm_campaign=executiveupdate',
    'article-1__alt-text': 'a beautiful blossom with large white petals and dark green leaves',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/02/march-cancelled-email.png',
    'article-1__heading': 'A Note From Executive Director, Mark Buscaino',
    'article-1__description': 'An update on spring and Casey Trees',
    'banner-a__link': '',
    'banner-a__alt-text': "Save the Date, Arbor Day 2021, 4/30/21",
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_canopy-awards-save-the-date-teaser-v2.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_canopy-awards-save-the-date-teaser-mobile-v2.png',
    'banner-a__text-1': 'Text 1', 
    'banner-a__text-2': "Text 2", 
    'article-2__link': 'https://caseytrees.org/2021/03/a-phenology-explainer/?utm_source=leaflet&utm_medium=email&utm_campaign=phenology',
    'article-2__alt-text': 'spring leaf index map',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/03/six-leaf-index-daily-anomaly-2021.gif',
    'article-2__heading': 'A Phenology Explainer',
    'article-2__description': 'Phenology, in turn, explains natural phenomena like spring leaf out, cicada emergence and more',
    'article-3__link': 'https://caseytrees.org/2021/03/tree-rainbow-blue-and-purple-blooms/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-3__alt-text': 'blue and purple blooms',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/03/redbud-branch-spring-rainbow-email.png',
    'article-3__heading': 'Tree Rainbow: Blue and Purple Blooms',
    'article-3__description': 'Their common names’ are colors, but neither are blue or purple!',
    'banner-b__link': 'https://caseytrees.org/about-us/jobs-internships/',
    'banner-b__alt-text': "We're hiring!",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
    'banner-b__text-1': 'We Are',
    'banner-b__text-2': "Hiring",
}

NVP = NVP_20210315
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
