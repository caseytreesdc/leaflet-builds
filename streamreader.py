import sys


NVP_20210412 = {
    'preheader': '',
    'article-1__link': 'https://caseytrees.org/2021/04/canopyfest-virtual-runs-in-person-tree-walks-and-a-nature-challenge/?utm_source=leaflet&utm_medium=email&utm_campaign=canopyawards',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2020/10/chestnuut-email.png',
    'article-1__heading': 'CanopyFest: Virtual Runs, In Person Tree Walks, and a Nature Challenge',
    'article-1__description': 'Arbor Day might not be until the end of April, but Casey Trees and friends are celebrating our urban forest all month long. Join us at these April activities!',
    'banner-a__link': 'https://www.canopyfest.org/',
    'banner-a__alt-text': 'Arbor Day Delivered',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_arbor-day-delivered.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_arbor-day-delivered-mobile.png',
    'banner-a__text-1': 'Arbor Day',
    'banner-a__text-2': 'Delivered',
    'article-2__link': 'https://caseytrees.org/2021/04/hiring-business-manager-and-horticulturist/?utm_source=leaflet&utm_medium=email&utm_campaign=jobs',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/08/hiring-2018-email.png',
    'article-2__heading': 'Hiring: Business Manager and Horticulturist ',
    'article-2__description': 'We’re looking for dedicated, talented folks to join our team',
    'article-3__link': 'https://caseytrees.org/2021/04/the-sturdy-steadfast-oak-is-the-perfect-tree-for-troubled-times-why-you-should-plant-them-from-an-expert/?utm_source=leaflet&utm_medium=email&utm_campaign=canopyawards',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/04/sturdy-oak-email.png',
    'article-3__heading': '“The sturdy, steadfast oak is the perfect tree for troubled times” Why You Should Plant Them, from an Expert',
    'article-3__description': 'Sharing a Washington Post article and ways to get your hands on a free Casey Trees oak',
    'banner-b__link': 'https://connect.clickandpledge.com/w/Form/cf568424-cf67-40f9-808b-cdcde7a60f26',
    'banner-b__alt-text': 'Run 4 Mother Earth 5K',
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_earth-day-5k.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/04/Leaflet-ad_earth-day-5k-mobile.png',
    'banner-b__text-1': 'Run', 
    'banner-b__text-2': '4 Mother Earth',
}

NVP = NVP_20210412
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
