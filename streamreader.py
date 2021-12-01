import sys


NVP_20211129 = {
    'preheader': "You give, they match. We’re trying to raise $5,000 for DC’s trees - will you help?",
    'article-1__link': 'https://caseytrees.org/2021/11/tomorrow-your-chance-to-make-a-difference-for-dcs-trees/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': 'shade trees with building peeking through',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/06/medium-shade-tree-email.png',
    'article-1__heading': 'Tomorrow. Your Chance to Make a Difference for DC’s Trees.',
    'article-1__description': 'You give, they match, DC’s trees win. #GivingTuesday is tomorrow!',
    'banner-a__link': 'https://caseytrees.org/give',
    'banner-a__alt-text': 'Give on giving tuesday',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/11/Giving-Tuesday_gt-email-leaf.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/11/Giving-Tuesday_gt-email-leaf.png',
    'article-2__link': 'https://caseytrees.org/2021/11/casey-trees-online-advocacy-portal/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': "a logo of a laptop and a loudspeaker",
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/11/advocacy-portal_emal.png',
    'article-2__heading': 'Casey Trees Online Advocacy Resources',
    'article-2__description': 'Classes on everything you need to demystify DC government and speak for trees - in your own home on your own time',
    'article-3__link': 'https://caseytrees.org/2021/11/from-casey-trees-to-the-urban-forestry-division/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-3__alt-text': 'Maddy McPhee: Urban Forester Ward 1',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/11/maddy-ufd-email.png',
    'article-3__heading': "We Love Working with Old Friends",
    'article-3__description': 'One of the reasons we work so well with UFD? Their arborist is a former employee!',
    'banner-b__link': 'http://www.facebook.com/pages/Casey-Trees/58793928339',
    'banner-b__alt-text': "follow us on facebook",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social-mobile.png',
}

NVP = NVP_20211129
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
