import sys


NVP_20210524 = {
    'preheader': 'and Essential Tree Care Items.',
    'article-1__link': 'https://caseytrees.org/2021/05/fostering-stewardship-on-kingman-heritage-islands/?utm_source=leaflet&utm_medium=email&utm_campaign=programming',
    'article-1__alt-text': 'filming with our education team at Kingman and Heritage Islands',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/05/css-kingman-videos-email.png',
    'article-1__heading': 'Fostering Stewardship on Kingman & Heritage Islands',
    'article-1__description': 'Our work on the Community Stormwater Solutions Grant and our work collaborating to improve  our waterways',
    'banner-ss__link-left' : 'https://caseytrees.org/take-action/water/',
    'banner-ss__alt-left' : 'Weekly Watering Alerts: Must Water',
    'banner-ss__image-left' : 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    'banner-ss__link-right' : 'https://caseytrees.org/2021/05/cicada-resources/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'banner-ss__alt-right' : 'Cicada Updates',
    'banner-ss__image-right' : 'https://caseytrees.org/wp-content/uploads/2021/05/cicada_leaflet.png',
    'article-2__link': 'https://caseytrees.org/2021/05/essential-tree-care-items/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-2__alt-text': 'Watering a young tree with a big bucket!',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/04/water-resplonsive.jpg',
    'article-2__heading': 'Essential Tree Care Items',
    'article-2__description': 'The people, places, and things that will keep your trees in tip top shape',
    'article-3__link': 'https://caseytrees.org/2021/05/closing-out-mental-health-month-with-ideas-for-tree-based-breaks/?utm_source=leaflet&utm_medium=email&utm_campaign=store',
    'article-3__alt-text': 'the sun shining through trees',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/05/mental-health-month-break-2021-email.png',
    'article-3__heading': 'Closing Out Mental Health Month with Ideas for Tree-Based Breaks',
    'article-3__description': 'To close out Mental Health Month, we’re sharing some tree and nature based ideas for a brain break.',
    'banner-b__link': 'https://casey-trees.myshopify.com/',
    'banner-b__alt-text': "The 13th Annual Tree Report Card: The State of DC's Trees in 2020",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/03/Leaflet-ad_browse-our-new-store-mobile.png',
    'banner-b__text-1': 'TRC', 
    'banner-b__text-2': '2020',
}

NVP = NVP_20210524
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
