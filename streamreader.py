import sys


NVP_20211115 = {
    'preheader': "and a homegrown (literally) Black Friday",
    'article-1__link': 'https://caseytrees.org/2021/11/support-homegrown-change-this-year-give-to-casey-trees-for-givingtuesday/?utm_source=leaflet&utm_medium=email&utm_campaign=eoy',
    'article-1__alt-text': 'under the tree canopy',
    'article-1__image': 'https://caseytrees.org/wp-content/uploads/2021/04/tree-walk-2021-email.png',
    'article-1__heading': 'Support Homegrown Change this Year. Give to Casey Trees for #GivingTuesday',
    'article-1__description': 'Just as every tree planted makes a difference, every dollar donated on #GivingTuesday next week makes a difference. Make your contribution at caseytrees.org/give early or on Tuesday, November 30.',
    'banner-a__link': 'https://caseytrees.org/education/urban-forestry-fellowship/',
    'banner-a__alt-text': 'Urban Forestry Student Scholarship',
    'banner-a__image-browser': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca_v2.png',
    'banner-a__image-responsive': 'https://caseytrees.org/wp-content/uploads/2020/11/Leaflet-ad_gca-mobile-2.png',
    'article-2__link': 'https://caseytrees.org/2021/11/introducingthe-urban-forest-preservation-authority-amendment-act-of-2021/?utm_source=leaflet&utm_medium=email&utm_campaign=advocacy',
    'article-2__alt-text': "a huge scarlet oak special tree",
    'article-2__image': 'https://caseytrees.org/wp-content/uploads/2021/11/dcist-trees-email.png',
    'article-2__heading': 'Introducing…the Urban Forest Preservation Authority Amendment Act Of 2021',
    'article-2__description': 'We’re partnering with Councilmembers Cheh and Allen to strengthen protections for our biggest trees',
    'article-3__link': 'https://caseytrees.org/2021/11/we-get-by-with-a-little-help-from-our-friends/?utm_source=leaflet&utm_medium=email&utm_campaign=citypartner',
    'article-3__alt-text': 'a fall tree lined street leading to one of DCs many roundabouts',
    'article-3__image': 'https://caseytrees.org/wp-content/uploads/2021/11/ufd-thankful-email.png',
    'article-3__heading': "We Get By with a Little Help from Our Friends",
    'article-3__description': 'This year, we’re especially thankful for our partner in urban forestry',
    'banner-b__link': 'http://www.facebook.com/pages/Casey-Trees/58793928339',
    'banner-b__alt-text': "follow us on facebook",
    'banner-b__image-browser': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social.png',
    'banner-b__image-responsive': 'https://caseytrees.org/wp-content/uploads/2021/01/Leaflet-ad_follow-us-on-social-mobile.png',
}

NVP = NVP_20211115
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
