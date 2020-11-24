import sys


NVP_20201124 = {
    'preheader': 'show some love for the pandemic’s surprising hero - urban trees!',
    'article-1__link': 'https://caseytrees.org/2020/11/10-things-to-do-for-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': '',
    'article-1__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/10-things-browser.png',
    'article-1__image-mobile': 'https://caseytrees.org/wp-content/uploads/2020/11/10-things-email.png',
    'article-1__heading': '10 Things to Do for Trees',
    'article-1__description': 'Show some love for the pandemic’s surprising hero - urban trees!',
    'banner-a__text-1': 'Urban Tree Summit Dec. 2nd',
    'banner-a__text-2': 'REGISTER NOW',
    'banner-a__link': 'https://www.eventbrite.com/e/montgomery-parks-and-casey-trees-tickets-121720670803',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_summit.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_summit-mobile.png',
    'banner-a__alt-text': '',
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
    'banner-b__link': 'https://www.eventbrite.com/e/advocacy-in-the-district-tickets-128900213007',
    'banner-b__text': '', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2018/02/Tree-Advocates-Gif-4-1.gif',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2018/02/Tree-Advocates-Gif-4-1.gif',
    'banner-b__alt-text': 'AITD',
}

NVP = NVP_20201124
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
