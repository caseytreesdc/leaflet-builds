import sys


NVP_20201214 = {
    'preheader': 'and Greenery Collection in the District starts Jan 11',
    'article-1__link': 'https://caseytrees.org/2021/01/an-urban-tree-summit-recap/?utm_source=leaflet&utm_medium=email&utm_campaign=greencitiesummit',
    'article-1__alt-text': '',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/01/uts-recap-email.png',
    'article-1__heading': 'An Urban Tree Summit Recap',
    'article-1__description': 'Together with Montgomery Parks, we held our first virtual summit! Here’s what went down',
    'banner-a__text-1': 'BLANK',
    'banner-a__text-2': 'BLANK',
    'banner-a__link': 'https://caseytrees.org/',
    'banner-a__image-browser': '',
    'banner-a__image-responsive': '',
    'banner-a__alt-text': '',
    'article-2__link': 'https://caseytrees.org/2021/01/holiday-greenery-collection-in-dc-starts-january-11/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-2__alt-text': '',
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2020/12/greenery-collection-email.png',
    'article-2__heading': 'Holiday Greenery Collection in DC Starts January 11',
    'article-2__description': 'If you’re ready to part with your tree, wreath, or greens, here’s how',
    'article-3__link': 'https://caseytrees.org/2021/01/from-the-archives-winter-tree-care/?utm_source=leaflet&utm_medium=email&utm_campaign=treecare',
    'article-3__alt-text': '',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2020/12/winter-tree-care-email.png',
    'article-3__heading': 'From the Archives: Winter Tree Care',
    'article-3__description': 'They may be dormant, but that doesn’t mean you can’t help out trees',
    'banner-b__link': 'https://connect.clickandpledge.com/w/Form/2ab97890-387e-4b10-a454-6ab08350e1b8?utm_source=leaflet&utm_medium=email&utm_campaign=eoy&utm_content=email7B&trk=eoy10',
    'banner-b__text-1': 'BLANK', 
    'banner-b__text-2': 'BLANK', 
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/08/Mask_Ad_1.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/08/MaskAd2-responsive.png',
    'banner-b__alt-text': '',
}

NVP = NVP_20201214
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
