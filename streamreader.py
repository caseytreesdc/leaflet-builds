import sys


NVP_2021213 = {
    'preheader': "One of the best investments in urban infrastructure you can make",
    'article-1__link': 'https://caseytrees.org/2021/12/all-i-want-for-christmas-is-tree-memes/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/12/12.13_memes-leaflet-email.jpg',
    'article-1__heading': 'All I Want For Christmas is Tree Memes',
    'article-1__description': 'An updated look at our favorite and most popular memes',
    'banner-a__link': 'https://connect.clickandpledge.com/w/Form/446220bb-4a7a-4225-8b33-39cd133877c1?trk=EOYEmail5&utm_source=listemail&utm_medium=email-5&utm_campaign=eoy2021',
    'banner-a__alt-text': 'Support Casey Trees this giving season. Donate Now',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/12/Leaflet-button_give-desktop.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/12/Leaflet-button_give-mobile.png',
    'article-2__link': 'https://caseytrees.org/2021/12/the-gift-that-keeps-on-giving-urban-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-2__alt-text': "people enjoying a walk under a canopy on both sides of a path",
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/07/summer-care-2021-email.png',
    'article-2__heading': 'The Gift that Keeps on Giving: Urban Trees',
    'article-2__description': 'From improving air quality, lower temperatures, absorbing stormwater and providing mental health benefits, trees are not just nice to have or nice to look at.',
    'article-3__link': 'https://caseytrees.org/2021/12/one-gift-to-rule-them-all/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-3__alt-text': 'A graphic of DC with the whitehouse',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/12/12.13-story-leaflet-email.jpg',
    'article-3__heading': "For The Person That Has Everything",
    'article-3__description': "One Gift to Rule Them All",
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
