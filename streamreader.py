import sys


NVP_20211018 = {
    'preheader': 'plus, setting up a tree for success, don’t leave it to chance!',
    'article-1__link': 'https://caseytrees.org/2021/10/riversmart-rundown-how-to-get-a-free-tree-in-dc/?utm_source=leaflet&utm_medium=email&utm_campaign=riversmarthomes',
    'article-1__alt-text': 'underneath a young tree, with 3 ID tags on a branch',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/10/rsh-rundown-email.png',
    'article-1__heading': 'RiverSmart Rundown: How to Get a Free Tree in DC',
    'article-1__description': 'All the details you never knew you needed about DC’s free tree program',
    'banner-a__link': 'https://caseytrees.org/plant/#plantitforward',
    'banner-a__alt-text': 'Plant it Forward: Hire Casey Trees',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/10/Leaflet-button_plant-it-forward-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/10/urban-leaf-peeping-places/?utm_source=leaflet&utm_medium=email&utm_campaign=fallguide',
    'article-2__alt-text': 'the washington monument across the tidal basin bordered by fall trees',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/09/five-fall-foliage-email.png',
    'article-2__heading': 'Urban Leaf Peeping Places',
    'article-2__description': 'Save yourself the 90 min trek to Shenandoah and stay close to home while soaking up fall colors',
    'article-3__link': 'https://caseytrees.org/2021/10/perks-of-pruning/?utm_source=leaflet&utm_medium=email&utm_campaign=feeforservice',
    'article-3__alt-text': '2 arborists wearing gloves and goggles pruning branches',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/10/pruning-101-email.png',
    'article-3__heading': 'Perks of Pruning',
    'article-3__description': 'Schedule your pruning now, so you and your trees are set up for structurally sound success',
    'banner-b__link': 'http://www.facebook.com/pages/Casey-Trees/58793928339',
    'banner-b__alt-text': "follow us on facebook",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social-mobile.png',
}

NVP = NVP_20211018
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
