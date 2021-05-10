import sys


NVP_20210510 = {
    'preheader': "and don’t forget to water young trees!",
    'article-1__link': 'https://caseytrees.org/2021/05/casey-trees-comments-on-the-comp-plan/?utm_source=leaflet&utm_medium=email&utm_campaign=tadvocacy',
    'article-1__alt-text': 'DC skyline',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/05/comp-plan-email.png',
    'article-1__heading': 'Casey Trees comments on the Comp Plan',
    'article-1__description': 'How expanding a zoning designation could benefit trees',
    'banner-a__link': 'https://caseytrees.org/2021/05/cicada-resources/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'banner-a__alt-text': 'Weekly Watering Alert: Water and Cicada Resources',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-and-cicada.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/05/2021-Watering-Alerts_must-water-and-cicada.png',
    'banner-a__text-1': 'Weekly Watering Alert: Water',
    'banner-a__text-2': 'Cicada Resources',
    'banner-ss__link-left' : 'https://caseytrees.org/take-action/water/',
    'banner-ss__alt-left' : 'Weekly Watering Alerts: Must Water',
    'banner-ss__image-left' : 'https://caseytrees.org/wp-content/uploads/2021/05/weekly-watering-alert_must-water-mobile.jpg',
    'banner-ss__link-right' : 'https://caseytrees.org/2021/05/cicada-resources/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'banner-ss__alt-right' : 'Cicada Updates',
    'banner-ss__image-right' : 'https://caseytrees.org/wp-content/uploads/2021/05/cicada_leaflet.png',
    'article-2__link': 'https://caseytrees.org/2021/05/what-grade-did-dc-recieve-for-the-2020-tree-report-card/?utm_source=leaflet&utm_medium=email&utm_campaign=treereportcard',
    'article-2__alt-text': '2020 Tree Report Card',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/05/trc-2020-email.png',
    'article-2__heading': 'What Grade did DC Receive for 2020 Tree Report Card?',
    'article-2__description': 'The only independent assessment of DC’s trees on both public and private lands, the Tree Report Card was released on Arbor Day and DC received a...',
    'article-3__link': 'https://caseytrees.org/2021/05/advocacy-works-soapstone-valley-sewer-reconstruction/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-3__alt-text': 'soapstone in a creek',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/05/soapstone-email.png',
    'article-3__heading': 'Advocacy Works: Soapstone Valley Sewer Reconstruction',
    'article-3__description': 'A big ole win in the advocacy column for Casey Trees and DC’s mature trees',
    'banner-b__link': 'https://casey-trees.myshopify.com/',
    'banner-b__alt-text': 'Merch!',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Leaflet-ad_NEW-MERCH.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/Leaflet-ad_NEW-MERCH.png',
    'banner-b__text-1': 'Merch', 
    'banner-b__text-2': 'Merch',
}

NVP = NVP_20210510
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
