import sys


NVP_2021213 = {
    'preheader': "Despite recent temps, winter’s here",
    'article-1__link': 'https://caseytrees.org/2021/12/fall-2021-season-wrap-up/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': 'a diverse crowd at a recent planting event with shovels',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/12/2021-wrap-up-email.png',
    'article-1__heading': 'Fall 2021 Season Wrap Up',
    'article-1__description': 'Seasonal reflection from the Casey Trees team',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/446220bb-4a7a-4225-8b33-39cd133877c1?trk=EOYEmail8&utm_source=listemail&utm_medium=email-8&utm_campaign=eoy2021',
    'banner-a__alt-text': 'Support Casey Trees this giving season. Donate Now',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/12/Leaflet-button_give-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/12/Leaflet-button_give-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/12/winters-here-five-evergreen-trees-to-id-in-dc/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-2__alt-text': "winter holly with thorny leaves and red berries",
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/11/winter-tree-id-holly-email.png',
    'article-2__heading': "Five Evergreen Trees to ID in DC",
    'article-2__description': 'Evergreen trees add color and beauty to our winter landscapes. Learn how to identify some common ones in DC',
    'article-3__link': 'https://caseytrees.org/2021/12/its-beginning-to-look-a-bit-like-winter/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-3__alt-text': 'Two people with safety protective gear and vests carefully prune a tree',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/10/pruning-101-email.png',
    'article-3__heading': "It’s Beginning to Look A Bit Like Winter",
    'article-3__description': "Tips for trees at your own front door.",
    'banner-b__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    'banner-b__alt-text': 'Urban Forestry Student Scholarship',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca_v2.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile-2.png',
}

NVP = NVP_2021213
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
