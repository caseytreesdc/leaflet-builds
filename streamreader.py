import sys


NVP_20201123 = {
    'preheader': 'show some love for the pandemic’s surprising hero - urban trees!',
    'article-1__link': 'https://caseytrees.org/2020/11/10-things-to-do-for-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/10-things-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/10-things-email.png',
    'article-1__heading': '10 Things to Do for Trees',
    'article-1__description': 'Show some love for the pandemic’s surprising hero - urban trees!',
    'banner-a__link': 'https://www.eventbrite.com/e/montgomery-parks-and-casey-trees-tickets-121720670803',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_summit.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_summit-mobile.png',
    'banner-a__alt-text': 'Check out the Casey Trees Fall Colors Map!',
    'article-2__link': 'https://caseytrees.org/2020/11/thankful-for-trees-2/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-2__alt-text': '',
    'article-2__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/thankful-2020-browser1.png',
    'article-2__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/thankful-2020-email.png',
    'article-2__heading': 'Thankful for Trees',
    'article-2__description': 'They’re so much more than a pretty face.',
    'article-3__link': 'https://caseytrees.org/2020/11/which-is-which-sweetgum-edition/?utm_source=leaflet&utm_medium=email&utm_campaign=treerebate',
    'article-3__alt-text': '',
    'article-3__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/sweetgum-browser1.png',
    'article-3__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/sweetgum-email.png',
    'article-3__heading': 'Which is Which: Sweetgum Edition',
    'article-3__description': 'How to know if you’ll have a handful of spiky fruits.',
    'banner__link': 'https://connect.clickandpledge.com/w/Form/2ab97890-387e-4b10-a454-6ab08350e1b8?utm_source=leaflet&utm_medium=email&utm_campaign=eoy&utm_content=email1&trk=givingtuesday1',
    # banner__image-browser/responsive if the delimited is 08-10-2020
    # banner__text if the delimited is 11-26-2020
    'banner__text': 'EOY GRAPHIC/BANNER', 
    'banner__image-browser': 'https://caseytrees.org/wp-content/uploads/2018/02/Tree-Advocates-Gif-4-1.gif',
    'banner__image-responsive': 'https://caseytrees.org/wp-content/uploads/2018/02/Tree-Advocates-Gif-4-1.gif',
    'banner__alt-text': 'Register Now for the Urban Forestry Scholarship',
}

NVP = NVP_20201123
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
