import sys


NVP_20210104 = {
    'preheader': 'We’re also testifying  in front of the Council',
    'article-1__link': 'https://caseytrees.org/2021/01/were-hiring-5/?utm_source=leaflet&utm_medium=email&utm_campaign=jobs',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/01/hiring-2021-email.jpg',
    'article-1__heading': 'We’re hiring!',
    'article-1__description': 'Positions are available in our Tree Planting and Policy & Land Conservation departments, as well as at our Farm.',
    'banner-a__text-1': 'City Partners in the News: the Kojo Nnamdi Show',
    'banner-a__text-2': "Casey Trees' Partners",
    'banner-a__link': 'https://thekojonnamdishow.org/shows/2021-01-05/achieving-tree-equity-in-the-district',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/09/Leaflet-ad_we-are-hiring-mobile.png',
    'banner-a__alt-text': "We're hiring!",
    'article-2__link': 'https://caseytrees.org/2021/01/we-testified-to-protect-public-heritage-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/12/heritage-trees-email.png',
    'article-2__heading': 'We Testified to Protect Public Heritage Trees',
    'article-2__description': 'How you can help us close legislativative loopholes.',
    'article-3__link': 'https://caseytrees.org/2021/01/to-our-supporters/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/12/eoy-thanks-email.png',
    'article-3__heading': 'To Our Supporters',
    'article-3__description': 'We truly appreciate your generosity, friendship and shared belief that a tree-filled DC is a better place to live, work and play.',
    'banner-b__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    'banner-b__text-1': 'Garden Club of America Scholarship', 
    'banner-b__text-2': 'Garden Club of America Scholarship', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca_v2.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile-2.png',
    'banner-b__alt-text': 'Urban Forestry Student Scholarship sponsored by the Garden Club of America',
}

NVP = NVP_20210104
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
